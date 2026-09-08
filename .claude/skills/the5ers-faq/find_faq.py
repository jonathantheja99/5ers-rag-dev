#!/usr/bin/env python3
"""Pull whole FAQ articles out of the compiled knowledge base.

grep alone gives you a line number, not the article it sits in. This finds the
matching `### Heading` blocks and prints each one complete, with its source URL
and last-updated date, so an answer can be grounded and cited.

Usage:
    python find_faq.py consistency rule         # articles matching all terms
    python find_faq.py --any payout withdrawal  # articles matching any term
    python find_faq.py --list drawdown          # headings only
    python find_faq.py --rules                  # print the verified master KB
"""

import argparse
import re
import sys
from pathlib import Path

KB = Path(__file__).resolve().parents[3] / "knowledge_base" / "faq_data.md"
ARCHIVE_MARKER = "# The5ers Official FAQ Archive (Reference Material)"
MAX_DEFAULT = 6


def load():
    if not KB.exists():
        sys.exit(f"Knowledge base not found at {KB}. Run: python backend/compiler.py")
    return KB.read_text(encoding="utf-8")


def split_articles(text):
    """Return [(heading, body)] for every '### ' article in the archive half."""
    _, marker, archive = text.partition(ARCHIVE_MARKER)
    source = archive if marker else text
    parts = re.split(r"(?m)^### ", source)
    articles = []
    for chunk in parts[1:]:
        heading, _, body = chunk.partition("\n")
        articles.append((heading.strip(), body.rstrip()))
    return articles


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("terms", nargs="*", help="search terms (case-insensitive)")
    ap.add_argument("--any", action="store_true", help="match any term, not all")
    ap.add_argument("--list", action="store_true", help="print matching headings only")
    ap.add_argument("--rules", action="store_true", help="print the verified master KB")
    ap.add_argument("--max", type=int, default=MAX_DEFAULT, help="max articles to print")
    args = ap.parse_args()

    text = load()

    if args.rules:
        head, marker, _ = text.partition(ARCHIVE_MARKER)
        print(head.rstrip() if marker else text)
        return 0

    if not args.terms:
        ap.error("give at least one search term, or use --rules")

    terms = [t.lower() for t in args.terms]
    hits = []
    for heading, body in split_articles(text):
        blob = f"{heading}\n{body}".lower()
        matched = any(t in blob for t in terms) if args.any else all(t in blob for t in terms)
        if matched:
            # Heading matches are the strongest signal; float them up.
            score = sum(t in heading.lower() for t in terms)
            hits.append((score, heading, body))

    if not hits:
        print(f"No articles matched: {' '.join(args.terms)}")
        print("Try fewer terms, or --any, or check --rules for verified policy.")
        return 1

    hits.sort(key=lambda h: -h[0])
    print(f"{len(hits)} article(s) matched: {' '.join(args.terms)}\n")

    if args.list:
        for _, heading, _ in hits:
            print(f"  - {heading}")
        return 0

    for _, heading, body in hits[: args.max]:
        print("=" * 78)
        print(f"### {heading}")
        print(body)
        print()
    if len(hits) > args.max:
        print(f"... {len(hits) - args.max} more. Narrow the terms or raise --max.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
