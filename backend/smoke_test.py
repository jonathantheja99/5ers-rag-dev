"""Ground-truth smoke test for the RAG agent.

Checks that answers agree with the verified operational rules in
the5ers_master_kb.md, and that the DuckDuckGo fallback engages for questions the
knowledge base cannot answer.

Usage:
    python backend/smoke_test.py            # retrieval + answer checks
    python backend/smoke_test.py --fast     # retrieval checks only (no LLM calls)
"""

import argparse
import sys

from agent import MASTER_K, RETRIEVAL_K, TIER_ARCHIVE, TIER_MASTER, RAGAgent

# (question, must mention any of, must NOT claim)
ANSWER_CASES = [
    (
        "Which programs have the consistency rule and which do not?",
        [["summer plan"], ["high stakes"], ["bootcamp"], ["hyper growth"]],
        [],
    ),
    (
        "How is the best trading day defined for the consistency rule?",
        [["net"]],
        [],
    ),
    (
        "Does the Bootcamp maximum loss trail my peak profits?",
        [["static", "does not trail", "not trail"]],
        [],
    ),
    (
        "Is the daily drawdown based on my starting balance or on midnight equity?",
        [["midnight"], ["balance", "equity"]],
        [],
    ),
    (
        "What commission do I pay on NAS100 versus XAUUSD?",
        [["0", "zero", "no commission", "commission-free"], ["percentage", "notional"]],
        [],
    ),
    (
        "How many minimum trading days does the Summer Plan 1-Step evaluation require?",
        [["0", "zero", "no minimum", "one trade", "1 trade"]],
        [],
    ),
]

# Retrieval must surface the verified-policy tier for these, not just archive text.
RETRIEVAL_CASES = [
    ("Which programs have the consistency rule?", ["High Stakes", "Bootcamp"]),
    ("Is the Bootcamp drawdown static or trailing?", ["Bootcamp"]),
]


def check_retrieval(agent) -> int:
    failures = 0
    print("== retrieval ==")
    for question, expected in RETRIEVAL_CASES:
        master = agent._search(question, TIER_MASTER, MASTER_K)
        archive = agent._search(question, TIER_ARCHIVE, RETRIEVAL_K)
        context = agent._retrieve(question)
        missing = [term for term in expected if term not in context]
        ok = bool(master) and not missing
        print(
            f"  [{'PASS' if ok else 'FAIL'}] {question}\n"
            f"         master={len(master)} archive={len(archive)} "
            f"chars={len(context)}"
            + (f" missing={missing}" if missing else "")
        )
        failures += 0 if ok else 1
    return failures


def check_answers(agent) -> int:
    failures = 0
    print("== answers ==")
    for question, required_groups, forbidden in ANSWER_CASES:
        answer = agent.get_answer(question)
        lowered = answer.lower()
        missing = [g for g in required_groups if not any(t in lowered for t in g)]
        leaked = [t for t in forbidden if t in lowered]
        ok = not missing and not leaked
        print(f"  [{'PASS' if ok else 'FAIL'}] {question}")
        if not ok:
            print(f"         missing={missing} forbidden_hit={leaked}")
            print(f"         answer: {answer.strip()[:300]}")
        failures += 0 if ok else 1
    return failures


def check_fallback(agent) -> int:
    """The web-search path must return usable text, not an exception string."""
    print("== duckduckgo fallback ==")
    results = agent.web_search("The5ers prop firm funding programs")
    ok = bool(results) and not results.startswith("Web search failed")
    print(f"  [{'PASS' if ok else 'FAIL'}] web_search returned {len(results)} chars")
    if not ok:
        print(f"         {results[:200]}")
    return 0 if ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fast", action="store_true", help="skip the answer checks (no LLM calls)"
    )
    args = parser.parse_args()

    agent = RAGAgent()
    print(f"agent status={agent.status} chunks={agent.indexed_chunks}\n")
    if not agent.is_ready():
        print("Agent is not ready; cannot run the smoke test.")
        return 1

    failures = check_retrieval(agent)
    failures += check_fallback(agent)
    if not args.fast:
        failures += check_answers(agent)

    print(f"\n{'FAILED' if failures else 'ALL CHECKS PASSED'} ({failures} failure(s))")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
