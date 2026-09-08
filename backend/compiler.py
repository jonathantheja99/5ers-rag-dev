"""Compile the knowledge base into the single source of truth for retrieval.

Concatenation order is load-bearing: the verified rulings in
``the5ers_master_kb.md`` are written FIRST, ahead of the raw official FAQ
archive, so the chunks a vector search returns lead with confirmed policy rather
than older marketing copy.

Usage:
    python backend/compiler.py            # build knowledge_base/faq_data.md
    python backend/compiler.py --check    # verify the output is up to date
"""

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

BACKEND_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BACKEND_DIR.parent

load_dotenv(BACKEND_DIR / ".env")

KB_DIR = Path(
    os.getenv("KNOWLEDGE_BASE_DIR") or (PROJECT_ROOT / "knowledge_base")
).expanduser()

MASTER_KB = KB_DIR / "the5ers_master_kb.md"
OFFICIAL_FAQS = KB_DIR / "the5ers_official_faqs.md"
OUTPUT_PATH = Path(
    os.getenv("KNOWLEDGE_BASE_PATH") or (KB_DIR / "faq_data.md")
).expanduser()

# Priority sources first. Anything appended later is lower-confidence material.
SOURCES = [
    (MASTER_KB, None),
    (
        OFFICIAL_FAQS,
        "# The5ers Official FAQ Archive (Reference Material)\n\n"
        "> The verified operational rules above take precedence over anything in this "
        "section if the two disagree.",
    ),
]


def build() -> str:
    if not MASTER_KB.exists():
        raise SystemExit(
            f"Refusing to compile: {MASTER_KB} is missing. The master KB must lead "
            "faq_data.md, otherwise retrieval will surface marketing text over policy."
        )

    parts = []
    for path, heading in SOURCES:
        if not path.exists():
            print(f"Warning: skipping missing source {path}")
            continue
        if heading:
            parts.append(heading)
        parts.append(path.read_text(encoding="utf-8").strip())
        print(f"  + {path.name}")

    return "\n\n---\n\n".join(parts) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit non-zero if the compiled output differs from the sources",
    )
    args = parser.parse_args()

    print(f"Compiling knowledge base from {KB_DIR}...")
    compiled = build()

    if args.check:
        current = OUTPUT_PATH.read_text(encoding="utf-8") if OUTPUT_PATH.exists() else ""
        if current == compiled:
            print(f"{OUTPUT_PATH.name} is up to date.")
            return 0
        print(f"{OUTPUT_PATH.name} is STALE. Run: python backend/compiler.py")
        return 1

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(compiled, encoding="utf-8")
    print(
        f"Wrote {OUTPUT_PATH} "
        f"({len(compiled.splitlines()):,} lines, {len(compiled):,} chars)."
    )
    print("Restart the backend to re-embed the updated knowledge base.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
