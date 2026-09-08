---
name: the5ers-faq
description: Answer support questions about The5ers prop trading firm — consistency rule, daily and maximum drawdown, payouts and payout caps, withdrawals, commissions and swaps, refunds, and the Summer Plan, High Stakes, Bootcamp, Hyper Growth, ProGrowth and Futures programs. Use whenever someone asks what a rule is, how a limit is calculated, which programs a rule applies to, or what a trader should be told. Answers come from the local knowledge base, not from memory or the web.
---

# The5ers support answers

Answer from `knowledge_base/faq_data.md`. Never answer these questions from
memory — the programs change, and the file is refreshed from the live site.

## How to answer

1. **Read the verified rules first** for anything touching consistency,
   drawdown, payouts, commissions or program scope:

   ```bash
   python .claude/skills/the5ers-faq/find_faq.py --rules
   ```

   That is the master KB (~170 lines) — hand-verified rulings and exact
   formulas. It is the top of `faq_data.md` and it **overrides** anything below it.

2. **Find the specific article(s):**

   ```bash
   python .claude/skills/the5ers-faq/find_faq.py consistency rule    # all terms
   python .claude/skills/the5ers-faq/find_faq.py --any payout withdrawal
   python .claude/skills/the5ers-faq/find_faq.py --list drawdown     # headings only
   ```

   Start with `--list` when a topic is broad, then re-run on the heading that fits.
   Plain `grep -n "^### .*payout" knowledge_base/faq_data.md` works too.

3. **Answer with the exact numbers**, and say which program each figure belongs
   to. Most wrong answers here come from quoting a Futures number for a CFD
   account, or a Summer Plan number for High Stakes.

4. **Cite** the source URL and `_Last updated:_` date printed with each article.

5. **If it is not in the file, say so.** Do not guess and do not substitute
   general prop-firm knowledge. Say what you could not find and suggest the
   trader check with support.

## Rules that override the archive

The archive contains older and marketing phrasings of these same topics. Where
they disagree, this wins:

- **Consistency rule** — `(best trading day NET profit / total net profit) * 100 <= 50%`
  (or the plan's stated threshold). The best day is the best **net** profitable day:
  that day's winning trades minus its losing trades. Net losing days are never the
  best day. Required total profit for payout = `2 x best day net profit`.
  Applies to **Summer Plan (CFD & Futures) and Futures only** — **not** High Stakes,
  Bootcamp, or Hyper Growth. Profit made recovering from drawdown still counts, and
  the metric resets after every approved payout.
- **Daily drawdown / daily pause is DYNAMIC** — calculated from the **higher of
  balance or equity at midnight server time (00:00 GMT+3)**, so the dollar
  allowance grows with the account. **CFD maximum drawdown is STATIC** from the
  initial starting balance. **Futures maximum drawdown is end-of-day trailing**
  off the highest day-end equity.
- **Bootcamp maximum loss is STATIC** (5% evaluation, 4% funded) and never trails
  peak profits. The 3% daily pause applies **only to the funded stage**; there is
  no daily pause during evaluation.
- **Commissions** — Forex flat $4.00 per round lot; indices (NAS100, US30, …)
  $0.00; crypto (BTCUSD) and metals (XAUUSD) percentage-based on notional value
  (`lots x contract size x price x fee%`), so the dollar fee moves with price.
  Indices close 23:50–01:05 EET; triple swap Friday for indices, Wednesday for Forex.
- **Summer Plan** — **zero** minimum trading days ("pass in 1 trade") on both
  1-Step and 2-Step CFD evaluations. Funded payout caps $2,000 per 14-day cycle
  on $100K, $3,000 on $200K. Refunds: 10% Hub credits phase 1, 20% phase 2,
  70% cash on the 3rd payout.

## Keeping the file current

`faq_data.md` is generated. If it looks stale (check the `**Captured:**` date in
the archive section):

```bash
python backend/scraper.py --promote && python backend/compiler.py
```

Never hand-edit `faq_data.md` — edit `knowledge_base/the5ers_master_kb.md` for
verified rules and recompile. `python backend/compiler.py --check` reports whether
the compiled file is current.
