"""Fetch The5ers FAQ articles from the WordPress REST API.

The public HTML pages are JS-rendered and expose neither the article title nor
its category, so this pulls the source of truth instead:

    https://wp.the5ers.com/wp-json/wp/v2/faqs        (post type frequently_questions)
    https://wp.the5ers.com/wp-json/wp/v2/faq_category

That gives every article's title, category, modified date and body HTML in a
handful of requests rather than 200+ page loads, and the ``language`` field
isolates the English set exactly.

Output goes to knowledge_base/scraped/ for review. It deliberately does NOT write
faq_data.md: that file is produced by compiler.py, which keeps the verified rules
of the5ers_master_kb.md at the top. Use --promote to replace the official archive
once a scrape looks right, then re-run compiler.py.

Usage:
    python backend/scraper.py              # write knowledge_base/scraped/...
    python backend/scraper.py --promote    # overwrite the5ers_official_faqs.md
"""

import argparse
import os
import sys
from datetime import date
from pathlib import Path

import requests
from bs4 import BeautifulSoup
import markdownify

PROJECT_ROOT = Path(__file__).resolve().parent.parent
KB_DIR = Path(
    os.getenv("KNOWLEDGE_BASE_DIR") or (PROJECT_ROOT / "knowledge_base")
).expanduser()

API_ROOT = os.getenv("FAQ_API_ROOT", "https://wp.the5ers.com/wp-json/wp/v2")
LANGUAGE = os.getenv("FAQ_LANGUAGE", "en")
PAGE_SIZE = 100
TIMEOUT = 90

OUTPUT_DIR = Path(os.getenv("SCRAPER_OUTPUT_DIR") or (KB_DIR / "scraped"))
OUTPUT_FILE = OUTPUT_DIR / "the5ers_faqs_scraped.md"
PROMOTE_FILE = KB_DIR / "the5ers_official_faqs.md"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
}

UNCATEGORIZED = "Uncategorized"


def _get(path: str, params: dict) -> requests.Response:
    return requests.get(f"{API_ROOT}/{path}", params=params, headers=HEADERS, timeout=TIMEOUT)


def fetch_all(path: str) -> list:
    """Page through a WP collection endpoint until it runs dry."""
    items = []
    for page in range(1, 100):
        response = _get(path, {"per_page": PAGE_SIZE, "page": page})
        if response.status_code != 200:
            break
        batch = response.json()
        if not batch:
            break
        items.extend(batch)
        if len(batch) < PAGE_SIZE:
            break
    return items


def category_names() -> dict:
    """Map faq_category term id -> name."""
    return {term["id"]: term["name"] for term in fetch_all("faq_category")}


def html_to_markdown(html: str) -> str:
    """Convert rendered post HTML to markdown, dropping the site's date banner."""
    soup = BeautifulSoup(html, "html.parser")
    # Escaping turns list bullets into literal "\*" lines, which the previous
    # archive never had and which read badly once retrieved into a prompt.
    text = markdownify.markdownify(
        str(soup),
        heading_style="ATX",
        escape_asterisks=False,
        escape_underscores=False,
        escape_misc=False,
    )

    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        # The body repeats "last update: September 6, 2026"; the heading carries it.
        if stripped.lower().startswith("last update:"):
            continue
        lines.append(line.rstrip())

    # Collapse the runs of blank lines markdownify leaves behind.
    out, blank = [], 0
    for line in lines:
        if line:
            out.append(line)
            blank = 0
        else:
            blank += 1
            if blank == 1:
                out.append("")
    return "\n".join(out).strip()


def build_document(articles: list, categories: dict) -> str:
    grouped = {}
    for article in articles:
        terms = article.get("faq_category") or []
        name = next(
            (categories[t] for t in terms if t in categories), UNCATEGORIZED
        )
        grouped.setdefault(name, []).append(article)

    for entries in grouped.values():
        entries.sort(key=lambda a: a["title"]["rendered"].lower())

    parts = [
        "# The5%ers — FAQs (CFD / Forex)",
        "",
        "**Source:** https://the5ers.com/faqs/  ",
        f"**Captured:** {date.today().isoformat()}  ",
        f"**Articles:** {len(articles)}",
        "",
        "## Contents",
        "",
    ]
    for name in sorted(grouped):
        parts.append(f"- **{name}** ({len(grouped[name])} articles)")
    parts.append("")
    parts.append("---")

    for name in sorted(grouped):
        parts.append("")
        parts.append(f"## {name}")
        for article in grouped[name]:
            title = BeautifulSoup(
                article["title"]["rendered"], "html.parser"
            ).get_text().strip()
            body = html_to_markdown(article["content"]["rendered"])
            if not body:
                continue
            parts.append("")
            parts.append(f"### {title}")
            parts.append("")
            parts.append(f"<{article['link']}>  ")
            parts.append(f"_Last updated: {article.get('modified', '')[:10]}_")
            parts.append("")
            parts.append(body)

    return "\n".join(parts).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--promote",
        action="store_true",
        help=f"write straight to {PROMOTE_FILE.name} instead of the review copy",
    )
    args = parser.parse_args()

    print(f"Fetching FAQ articles from {API_ROOT} ...")
    everything = fetch_all("faqs")
    if not everything:
        print("No articles returned; aborting without writing anything.")
        return 1

    articles = [a for a in everything if str(a.get("language", "")).lower() == LANGUAGE]
    print(f"  {len(everything)} total, {len(articles)} in language '{LANGUAGE}'")
    if not articles:
        print("Language filter matched nothing; aborting without writing anything.")
        return 1

    categories = category_names()
    print(f"  {len(categories)} category terms")

    document = build_document(articles, categories)

    target = PROMOTE_FILE if args.promote else OUTPUT_FILE
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(document, encoding="utf-8")
    print(
        f"Wrote {target} ({len(document.splitlines()):,} lines, {len(document):,} chars)."
    )
    if args.promote:
        print("Now run: python backend/compiler.py")
    else:
        print(f"Review it, then re-run with --promote to replace {PROMOTE_FILE.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
