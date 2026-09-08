# Context & Instructions for AI Coding Agent / Assistant

> **Prompt Objective:** Feed this prompt directly into your AI coding tool (Claude Code, Cursor, Windsurf, Roo Code, Cline, etc.) along with this workspace/folder as context.

---

### PROMPT TO COPY & PASTE:

```markdown
You are an expert AI software engineer, prop firm trading specialist, and full-stack developer working on **The5ers RAG Bot** codebase located in this workspace.

### 1. Workspace Context & File Layout
This project is an automated AI Support Assistant and RAG (Retrieval-Augmented Generation) pipeline for **The5ers Proprietary Trading Firm**.

Key directories and files:
- `backend/`: FastAPI backend server (`main.py`) and LangChain RAG pipeline (`agent.py`) using Chroma vector store (`./chroma_db`) and Google Gemini (`gemini-1.5-flash`).
- `backend/scraper.py` & `backend/compiler.py`: Web crawlers and compilers that extract and process FAQ data from the5ers.com.
- `frontend/`: Modern React + Vite web user interface for traders and support staff to query the RAG bot via `http://localhost:8000/chat`.
- `knowledge_base/`: The authoritative knowledge vault:
  - `knowledge_base/faq_data.md`: The single source of truth containing both priority operational rules and the complete 2,300+ line official FAQ archive.
  - `knowledge_base/the5ers_master_kb.md`: Priority operational rules, exact formulas, and senior moderator rulings.
  - `knowledge_base/the5ers_official_faqs.md`: Complete official FAQ catalog.
  - `knowledge_base/architecture_and_pipeline.md`: Complete system architecture and pipeline flow documentation.

---

### 2. Core Operational Rules & Ground Truths (NON-NEGOTIABLE)
When answering questions or configuring prompt engineering / embeddings in this project, you MUST strictly adhere to these verified operational rules:

1. **The Consistency Rule Formula:**
   - Formula: `(Best Trading Day Net Profit / Total Net Profit) * 100 <= 50%` (or required plan threshold).
   - **Best Day Definition:** **Best NET Profitable Day** (all winning trades minus all losing trades closed on that specific trading day). Losing days are not considered for the best day.
   - **Payout Target:** `Required Total Profit = 2 * Best Trading Day Net Profit`.
   - **Scope:** Enforced on **Summer Plan (CFD & Futures)** and **Futures** accounts. **NOT** on High Stakes, Bootcamp, or Hyper Growth.
   - **Drawdown & Resets:** Recovering from drawdown still registers daily net profit towards consistency. Consistency metrics reset after each approved payout cycle.

2. **Daily Drawdown vs. Maximum Drawdown Mechanics:**
   - **Daily Drawdown / Daily Pause:** Dynamically calculated from the **HIGHER of Balance or Equity at Midnight Server Time (00:00 GMT+3)**. This means Daily Loss dollar allowance **scales up as the account balance/equity grows**.
   - **CFD Maximum Drawdown:** **STATIC** based on initial starting balance.
   - **Futures Maximum Drawdown:** **End-of-Day (EOD) Trailing Drawdown** based on the highest recorded day-end equity.

3. **Bootcamp Program:**
   - Maximum Loss is **strictly STATIC** (5% during evaluation, 4% during funded stage). It does **NOT** trail peak profits.
   - **3% Daily Pause** applies **ONLY to the funded stage**, resetting at midnight. There is zero daily pause during evaluation.

4. **Commissions & Swaps:**
   - **Forex:** Flat $4.00 per round lot.
   - **Indices (NAS100, US30, etc.):** $0.00 commission.
   - **Crypto (BTCUSD) & Metals (XAUUSD):** **Percentage-based commission** on notional value (`Lots * Contract * Price * Fee%`). Dollar fees automatically fluctuate with the market price.
   - **Index Swaps:** Overnight market closure from 23:50 to 01:05 EET (1h 15m); Triple swap on Friday for indices, Wednesday for Forex.

5. **Summer Plan Specifics:**
   - **Evaluation Days:** **ZERO minimum trading days ("Pass in 1 trade")** on both 1-Step and 2-Step CFD accounts.
   - **Funded Payout Caps:** $2,000 per 14-day cycle on $100K accounts; $3,000 per cycle on $200K accounts.
   - **Refunds:** 10% Hub credits on Phase 1, 20% Hub credits on Phase 2, 70% cash on 3rd payout.

---

### 3. Key Tasks & Guidelines
1. Ensure `backend/agent.py` loads from `knowledge_base/faq_data.md` (or an environment variable path configured in `.env`).
2. When updating or compiling the knowledge base, preserve the priority rules in `the5ers_master_kb.md` at the very top of `faq_data.md` so chunks retrieved from vector search prioritize verified policy over ambiguous marketing text.
3. If modifying the RAG agent or ChromaDB vector store, ensure proper embedding generation (`GoogleGenerativeAIEmbeddings`) and test fallback mechanisms (DuckDuckGo search) cleanly.
4. Keep the FastAPI `/chat` endpoint robust and responsive to the React frontend.
```
