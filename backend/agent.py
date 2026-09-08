"""LangChain RAG agent for The5ers support assistant.

Retrieval runs against the compiled knowledge base at
``knowledge_base/faq_data.md`` (override with ``KNOWLEDGE_BASE_PATH``), which is
produced by ``compiler.py`` with the verified rules of ``the5ers_master_kb.md``
written first, ahead of the raw FAQ archive.
"""

import hashlib
import json
import os
import re
import shutil
import time
import warnings
from pathlib import Path

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_chroma import Chroma
from dotenv import load_dotenv

try:  # the duckduckgo_search package was renamed to ddgs
    from ddgs import DDGS
except ImportError:  # pragma: no cover
    from duckduckgo_search import DDGS

# temperature=0 is set deliberately for determinism, but the lite models use fixed
# sampling and re-warn on every single call. Keep the setting, drop the noise.
warnings.filterwarnings(
    "ignore", message=".*uses fixed sampling defaults.*", category=UserWarning
)

BACKEND_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BACKEND_DIR.parent

load_dotenv(BACKEND_DIR / ".env")

# Compiled single source of truth. Resolved relative to the project, never the
# process working directory, so uvicorn can be launched from anywhere.
DEFAULT_KB_PATH = PROJECT_ROOT / "knowledge_base" / "faq_data.md"
KNOWLEDGE_BASE_PATH = Path(
    os.getenv("KNOWLEDGE_BASE_PATH") or DEFAULT_KB_PATH
).expanduser()

CHROMA_DB_PATH = Path(
    os.getenv("CHROMA_DB_PATH") or (BACKEND_DIR / "chroma_db")
).expanduser()

CHAT_MODEL = os.getenv("CHAT_MODEL", "gemini-3.5-flash-lite")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "models/gemini-embedding-001")
COLLECTION_NAME = "the5ers_faq"
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))

# Chunks carry a tier so verified policy is retrieved separately from the far
# bulkier FAQ archive. Position in the file does not influence vector similarity,
# so without this split the 2,300-line archive outvotes the master KB on every
# query - which is exactly how "which programs have the consistency rule?" used
# to come back unanswered.
RETRIEVAL_K = int(os.getenv("RETRIEVAL_K", "5"))
MASTER_K = int(os.getenv("MASTER_K", "3"))
TIER_MASTER = "master"
TIER_ARCHIVE = "archive"

# Routing gate: answer from the knowledge base at or above this relevance, else
# fall back to web search. Measured against this KB, in-domain questions score
# 0.59-0.66 and out-of-domain ones 0.31-0.46, so 0.50 sits in the gap. This
# replaced an LLM yes/no gate that discarded good context on some runs and cost
# a second generate request on every question.
RELEVANCE_THRESHOLD = float(os.getenv("RELEVANCE_THRESHOLD", "0.5"))
# Must match the archive heading written by compiler.py.
ARCHIVE_MARKER = "# The5ers Official FAQ Archive (Reference Material)"

# The free Gemini tier allows 100 embed_content requests per minute and the client
# issues one request per chunk, so indexing is paced instead of fired all at once.
EMBED_BATCH_SIZE = int(os.getenv("EMBED_BATCH_SIZE", "50"))
EMBED_BATCH_PAUSE = float(os.getenv("EMBED_BATCH_PAUSE", "35"))
EMBED_MAX_RETRIES = int(os.getenv("EMBED_MAX_RETRIES", "5"))

# Verified operational rules injected into every grounded answer. The FAQ
# archive contains older / marketing phrasings of these same topics; when the
# retrieved context disagrees with this block, this block wins.
POLICY_PREAMBLE = """\
NON-NEGOTIABLE OPERATIONAL RULES (these override any retrieved text that conflicts):
1. Consistency Rule: (Best Trading Day NET Profit / Total Net Profit) * 100 <= 50% (or the
   plan's stated threshold). The best day is the best NET profitable day (that day's winning
   trades minus its losing trades); net losing days are never the best day. Required total
   profit for payout = 2 x best trading day net profit. Enforced on Summer Plan (CFD &
   Futures) and Futures accounts only - NOT on High Stakes, Bootcamp, or Hyper Growth.
   Profits made while recovering from drawdown still count toward consistency, and the
   metric resets after every approved payout.
2. Daily Drawdown / Daily Pause is DYNAMIC: calculated from the HIGHER of balance or equity
   at midnight server time (00:00 GMT+3), so the dollar allowance scales up as the account
   grows. CFD Maximum Drawdown is STATIC from the initial starting balance. Futures Maximum
   Drawdown is an End-of-Day (EOD) trailing drawdown off the highest day-end equity.
3. Bootcamp: Maximum Loss is strictly STATIC (5% in evaluation, 4% when funded) and never
   trails peak profits. The 3% daily pause applies ONLY to the funded stage and resets at
   midnight; there is no daily pause during evaluation.
4. Commissions: Forex is a flat $4.00 per round lot. Indices (NAS100, US30, etc.) are $0.00.
   Crypto (BTCUSD) and Metals (XAUUSD) are percentage-based on notional value
   (Lots x Contract Size x Price x Fee%), so the dollar fee moves with market price.
   Indices close overnight 23:50-01:05 EET; triple swap lands Friday for indices and
   Wednesday for Forex.
5. Summer Plan: ZERO minimum trading days (pass in 1 trade) on both 1-Step and 2-Step CFD
   evaluations. Funded payout caps are $2,000 per 14-day cycle on $100K accounts and $3,000
   per cycle on $200K accounts. Refunds: 10% Hub credits on Phase 1, 20% Hub credits on
   Phase 2, 70% cash on the 3rd payout."""

NO_ANSWER_MESSAGE = "I cannot answer the question because I lack the necessary data."

CONTEXT_SEPARATOR = "\n\n"

# The user is asking a support question, not requesting an essay, and the React
# client drops the answer straight into a plain <div> - no markdown renderer and
# no pre-wrap - so asterisks and headings arrive on screen as literal junk and
# line breaks collapse. Short ASCII prose is the only shape that renders well.
# _plain_text() enforces what this asks for.
ANSWER_STYLE = """\
HOW TO ANSWER:
- The user wants the answer itself. Lead with it in the first sentence. No greeting, no
  restating the question, no "based on the context", no closing offer of more help.
- Keep it short: 2 to 4 sentences, under 80 words. One paragraph.
- Stay strong on substance. Include the exact number, formula, or program name whenever it
  is what makes the answer correct, and name the plan a rule applies to.
- Use simple everyday words and short sentences. If a trading term is unavoidable, explain
  it in a few words the first time.
- Write plain text only: ordinary letters, digits, and basic punctuation. No markdown, no
  asterisks, no bullet points, no headings, no emoji, no special symbols. Write "x" for
  times, "<=" for at most, and a plain hyphen for a dash.
- Never mention the context, the knowledge base, the FAQ, or that anything was retrieved."""


def _as_text(response) -> str:
    """Normalize an LLM response to plain text.

    Current Gemini models return ``.content`` as a list of content blocks rather
    than a string, so prefer ``.text`` and fall back to joining the blocks.
    """
    text = getattr(response, "text", None)
    if isinstance(text, str):
        return str(text)

    content = getattr(response, "content", response)
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text", ""))
        return "".join(parts)
    return str(content)


# Typographic characters the model reaches for that the plain-text bubble cannot
# render as intended, mapped to their ASCII equivalents.
_UNICODE_FIXES = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'",
    "“": '"', "”": '"', "„": '"',
    "–": "-", "—": "-", "―": "-", "−": "-", "­": "",
    "…": "...", " ": " ", " ": " ", " ": " ", "​": "",
    "•": "-", "·": "-", "⁃": "-", "●": "-", "▪": "-",
    "→": "->", "⇒": "=>", "≤": "<=", "≥": ">=",
    "×": "x", "÷": "/", "≈": "~", "≠": "!=", "°": " degrees",
}


def _plain_text(text: str) -> str:
    """Flatten a model answer into simple one-paragraph ASCII prose.

    ANSWER_STYLE asks the model for this; the frontend renders `answer` as raw
    text, so anything the model slips through anyway - bold markers, bullets,
    smart quotes, emoji - would reach the user as visible noise. Cheap insurance.
    """
    for fancy, plain in _UNICODE_FIXES.items():
        text = text.replace(fancy, plain)

    text = re.sub(r"```[a-zA-Z]*", "", text)  # fenced code blocks
    text = re.sub(r"^\s{0,3}#{1,6}\s*", "", text, flags=re.M)  # headings
    text = re.sub(r"^\s{0,3}>\s?", "", text, flags=re.M)  # block quotes
    text = re.sub(r"^\s{0,3}[-*+]\s+", "", text, flags=re.M)  # bullet markers
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text, flags=re.S)  # bold
    text = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"\1", text, flags=re.S)  # italics
    text = text.replace("`", "")
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)  # markdown links

    # Emoji and any other stray symbol: dropped rather than mangled.
    text = "".join(ch for ch in text if ch.isascii())

    # No pre-wrap in the bubble, so newlines would silently become spaces in the
    # browser anyway. Do it here so the API and the UI agree on the answer.
    text = re.sub(r"\s*\n\s*", " ", text)
    return re.sub(r"[ \t]{2,}", " ", text).strip()


def _retry_delay(message: str):
    """Pull the server-suggested backoff out of a Gemini 429 payload."""
    match = re.search(r"retry in ([0-9.]+)s", message) or re.search(
        r"retryDelay['\"]?:\s*['\"]?([0-9.]+)s", message
    )
    if not match:
        return None
    return min(float(match.group(1)) + 2, 120)


class RAGAgent:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY", "")
        self.vectorstore = None
        self.llm = None
        self.embeddings = None
        self.status = "uninitialized"
        self.indexed_chunks = 0
        if self.api_key:
            self._init_agent()
        else:
            self.status = "missing_api_key"

    # ------------------------------------------------------------------ setup

    def _init_agent(self):
        self.llm = ChatGoogleGenerativeAI(
            model=CHAT_MODEL, google_api_key=self.api_key, temperature=0
        )
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model=EMBEDDING_MODEL, google_api_key=self.api_key
        )

        if not KNOWLEDGE_BASE_PATH.exists():
            print(
                f"Warning: knowledge base not found at {KNOWLEDGE_BASE_PATH}. "
                "Run backend/compiler.py to build it. Answers will fall back to web search."
            )
            self.status = "missing_knowledge_base"
            return

        fingerprint = self._fingerprint()
        if self._fingerprint_matches(fingerprint):
            # Same source and same chunking config: reuse the persisted vectors
            # instead of re-embedding (and duplicating) the whole KB on boot.
            self.vectorstore = Chroma(
                collection_name=COLLECTION_NAME,
                embedding_function=self.embeddings,
                persist_directory=str(CHROMA_DB_PATH),
            )
            self.indexed_chunks = self.vectorstore._collection.count()
            print(f"Reusing persisted vector store ({self.indexed_chunks} chunks).")
        else:
            self.vectorstore = self._build_vectorstore()
            self._write_fingerprint(fingerprint)

        self.status = "ready"

    def _load_chunks(self) -> list:
        """Split the compiled knowledge base into policy and archive tiers.

        compiler.py writes the master KB first, then ARCHIVE_MARKER, then the raw
        FAQ archive. That boundary is recorded as chunk metadata so retrieval can
        guarantee verified policy reaches the context window.
        """
        text = KNOWLEDGE_BASE_PATH.read_text(encoding="utf-8")
        head, marker, tail = text.partition(ARCHIVE_MARKER)
        sections = [(head, TIER_MASTER)]
        if marker:
            sections.append((marker + tail, TIER_ARCHIVE))
        else:
            print(
                "Warning: archive marker not found in the knowledge base; indexing "
                "everything as verified policy. Re-run backend/compiler.py."
            )

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
        )
        chunks = []
        for body, tier in sections:
            doc = Document(
                page_content=body,
                metadata={"source": KNOWLEDGE_BASE_PATH.name, "tier": tier},
            )
            chunks.extend(splitter.split_documents([doc]))
        return chunks

    def _build_vectorstore(self) -> Chroma:
        chunks = self._load_chunks()
        self.indexed_chunks = len(chunks)

        tiers = {}
        for chunk in chunks:
            tier = chunk.metadata["tier"]
            tiers[tier] = tiers.get(tier, 0) + 1

        # Wipe first: adding to an existing collection would stack duplicate
        # copies of every chunk on each rebuild.
        if CHROMA_DB_PATH.exists():
            shutil.rmtree(CHROMA_DB_PATH, ignore_errors=True)
        CHROMA_DB_PATH.mkdir(parents=True, exist_ok=True)

        print(
            f"Embedding {len(chunks)} chunks from {KNOWLEDGE_BASE_PATH.name} "
            f"(tiers: {tiers})..."
        )
        store = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=self.embeddings,
            persist_directory=str(CHROMA_DB_PATH),
        )
        self._add_in_batches(store, chunks)
        return store

    def _add_in_batches(self, store: Chroma, chunks: list) -> None:
        total = len(chunks)
        for start in range(0, total, EMBED_BATCH_SIZE):
            self._add_batch(store, chunks[start : start + EMBED_BATCH_SIZE])
            done = min(start + EMBED_BATCH_SIZE, total)
            print(f"  embedded {done}/{total} chunks")
            if done < total:
                time.sleep(EMBED_BATCH_PAUSE)

    def _add_batch(self, store: Chroma, batch: list) -> None:
        for attempt in range(1, EMBED_MAX_RETRIES + 1):
            try:
                store.add_documents(batch)
                return
            except Exception as e:
                message = str(e)
                rate_limited = "RESOURCE_EXHAUSTED" in message or "429" in message
                if not rate_limited or attempt == EMBED_MAX_RETRIES:
                    raise
                delay = _retry_delay(message) or EMBED_BATCH_PAUSE * attempt
                print(
                    f"  rate limited, retrying in {delay:.0f}s "
                    f"(attempt {attempt}/{EMBED_MAX_RETRIES})"
                )
                time.sleep(delay)

    def _fingerprint(self) -> dict:
        digest = hashlib.sha256(KNOWLEDGE_BASE_PATH.read_bytes()).hexdigest()
        return {
            "source": str(KNOWLEDGE_BASE_PATH),
            "sha256": digest,
            "chunk_size": CHUNK_SIZE,
            "chunk_overlap": CHUNK_OVERLAP,
            "embedding_model": EMBEDDING_MODEL,
            "collection": COLLECTION_NAME,
            "schema": 2,
        }

    @property
    def _fingerprint_file(self) -> Path:
        return CHROMA_DB_PATH / "kb_fingerprint.json"

    def _fingerprint_matches(self, fingerprint: dict) -> bool:
        try:
            stored = json.loads(self._fingerprint_file.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return False
        return stored == fingerprint

    def _write_fingerprint(self, fingerprint: dict) -> None:
        try:
            self._fingerprint_file.write_text(
                json.dumps(fingerprint, indent=2), encoding="utf-8"
            )
        except OSError as e:
            print(f"Warning: could not persist index fingerprint: {e}")

    def is_ready(self) -> bool:
        return self.status == "ready"

    # ------------------------------------------------------------------ tools

    def web_search(self, query: str) -> str:
        """Fallback tool to search the web using DuckDuckGo."""
        print(f"Performing web search for: {query}")
        try:
            results = DDGS().text(query, max_results=3) or []
        except Exception as e:
            return f"Web search failed: {e}"

        formatted = []
        for r in results:
            if not isinstance(r, dict):
                continue
            title = (r.get("title") or "").strip()
            body = (r.get("body") or r.get("snippet") or "").strip()
            href = r.get("href") or r.get("url") or ""
            if body:
                formatted.append(f"Title: {title}\nURL: {href}\nBody: {body}")
        return CONTEXT_SEPARATOR.join(formatted)

    def _search(self, query: str, tier, k: int) -> list:
        """Return [(document, relevance_score)] for one tier."""
        if not self.vectorstore or k <= 0:
            return []
        kwargs = {"filter": {"tier": tier}} if tier else {}
        try:
            return self.vectorstore.similarity_search_with_relevance_scores(
                query, k=k, **kwargs
            )
        except Exception as e:
            print(f"Retrieval failed (tier={tier}): {e}")
            return []

    def _retrieve(self, query: str):
        """Lead the context with verified policy, then add archive detail.

        Returns (context, best_relevance) so the caller can decide between a
        grounded answer and the web fallback without a second model call.
        """
        scored = self._search(query, TIER_MASTER, MASTER_K) + self._search(
            query, TIER_ARCHIVE, RETRIEVAL_K
        )
        if not scored:  # index predates tier metadata, or the filter matched nothing
            scored = self._search(query, None, MASTER_K + RETRIEVAL_K)
        if not scored:
            return "", 0.0
        context = CONTEXT_SEPARATOR.join(doc.page_content for doc, _ in scored)
        return context, max(score for _, score in scored)

    # ----------------------------------------------------------------- answer

    def get_answer(self, query: str) -> str:
        if not self.api_key:
            return (
                "Error: GEMINI_API_KEY is not set. "
                "Please provide a Google Gemini API Key in the backend/.env file."
            )

        context, relevance = self._retrieve(query)

        if context and relevance >= RELEVANCE_THRESHOLD:
            prompt = f"""\
You are a support agent for The 5ers proprietary trading firm. A trader has asked one
question and wants the answer, plainly and briefly.

{POLICY_PREAMBLE}

{ANSWER_STYLE}

Answer the question using the retrieved context below. Be exact with numbers, formulas, and
which programs a rule applies to. If the context does not contain the answer, say so in one
sentence rather than guessing.

Context:
{context}

Question: {query}

Answer:"""
            return _plain_text(_as_text(self.llm.invoke(prompt)))

        # Fallback: nothing relevant in the knowledge base, try the open web.
        print(f"Relevance {relevance:.3f} below {RELEVANCE_THRESHOLD}; falling back.")
        web_context = self.web_search(f"The 5ers {query}")
        if not web_context or web_context.startswith("Web search failed"):
            return NO_ANSWER_MESSAGE

        fallback_prompt = f"""\
You are a support agent for The 5ers proprietary trading firm. A trader has asked one
question and wants the answer, plainly and briefly.

{POLICY_PREAMBLE}

{ANSWER_STYLE}

The internal FAQ did not contain the answer, so a web search was performed. Answer using the
search results below. If they do not contain the answer, reply with exactly:
"{NO_ANSWER_MESSAGE}"

Web Search Results:
{web_context}

Question: {query}

Answer:"""
        return _plain_text(_as_text(self.llm.invoke(fallback_prompt)))
