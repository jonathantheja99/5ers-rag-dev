# The5ers Master Knowledge Base & Operational Reference (Chat Primary Knowledge)

> **Location:** `C:\Users\USER\.gemini\antigravity\scratch\the5ers_master_kb.md`  
> **Synced With:** `C:\Users\USER\Documents\Obsidian Vault\5ers RAG\faq_data.md`  
> **Status:** Verified Active Knowledge Base for Support Chat Inquiries.

---

## 1. The Consistency Rule (Detailed Mechanics & Formulas)

### Core Rule & Scope
* **Which accounts have the Consistency Rule?**
  * **Summer Plan (CFD & Futures)**: Enforces the **50% Consistency Rule**.
  * **Futures Programs**: Enforce consistency requirements (typically 40% or 50% depending on plan).
* **Which accounts DO NOT have the Consistency Rule?**
  * **High Stakes (Classic & New)**: **No consistency percentage rule** on evaluation or funded stages.
  * **Bootcamp**: **No consistency percentage rule**.
  * **Hyper Growth**: **No consistency percentage rule**.

### Official Calculation Formula
$$\text{Consistency Percentage} = \left( \frac{\text{Best Trading Day Net Profit}}{\text{Total Net Profit}} \right) \times 100 \le 50\%$$

* **Numerator (Best Trading Day):** 
  * Defined as the **Best NET Profitable Day** (all winning trades minus all losing trades closed on that specific trading day).
  * Net losing days are not considered for the "best day."
* **Denominator (Total Net Profit):**
  * The cumulative net profit generated across all profitable days (or profit above starting balance).
* **Target Payout Threshold:**
  $$\text{Required Total Profit} = 2 \times \text{Best Trading Day Net Profit}$$

### Drawdown & Consistency Interaction
* **Recovering from Drawdown:**
  * When an account is in drawdown (e.g. balance at $94K or $99K on a $100K account), winning trades taken to recover the account still establish a daily net profit for consistency.
  * To be eligible for a payout, the account must be back in net profit (above the initial balance) and satisfy the 50% consistency condition.
* **Resetting After Payout:**
  * The Consistency Rule **resets after every approved payout**.
  * For the subsequent 14-day cycle, the consistency metrics recalculate fresh based on new trading performance.
  * Unwithdrawn profits that remain in the account continue to buffer the static maximum loss.

---

## 2. Summer Plan Specifications (CFD & Futures)

### CFD 1-Step (Growth)
* **Evaluation Target:** 10% profit target.
* **Minimum Trading Days:** **0 days ("Pass in 1 trade")** — can pass in a single day/trade.
* **Daily Loss Limit:** 3% (calculated from midnight balance/equity).
* **Maximum Loss Limit:** 6% **STATIC** from initial starting balance.
* **Leverage:** 1:100.
* **Consistency Rule:** 50% (applies during both Evaluation and Funded phases).
* **Funded Stage Payouts:**
  * Minimum withdrawal: **$250**.
  * Maximum payout cap: **$2,000 per 14-day cycle**.
  * 10% target on funded stage is strictly for **account scaling**, not a payout requirement.

### CFD 2-Step
* **Evaluation Targets:** Phase 1: 8% | Phase 2: 5%.
* **Minimum Trading Days:** **0 days ("Pass in 1 trade")**.
* **Daily Loss Limit:** 5% (calculated from midnight balance/equity).
* **Maximum Loss Limit:** 10% **STATIC** from initial starting balance.
* **Leverage:** 1:100.
* **Consistency Rule:** 50% (applies to both Evaluation phases and Funded phase).
* **Payout Caps:**
  * **$100K Account:** Up to **$2,000 per 14-day cycle**.
  * **$200K Account:** Up to **$3,000 per 14-day cycle**.
* **News Restriction:**
  * Holding open positions over high-impact (red folder) news is **allowed**.
  * Opening new market orders or executing pending limit/stop orders within **2 minutes before or 2 minutes after** high-impact news on the affected currency/index is **prohibited** (soft breach: profits removed, loss retained, account stays active).

### Futures Summer Plan
* **Drawdown Model:** **End-of-Day (EOD) Trailing Drawdown** (4%), calculated at daily market close.
* **Commission:** Commission rebate model applied.
* **Weekend Holding:** Not permitted on Futures Swing accounts (all positions must be closed by 4:50 PM ET Friday).

### Summer Plan Refund Structure
* **Phase 1 Pass:** 10% of entry fee returned as **Hub Credits**.
* **Phase 2 Pass:** 20% of entry fee returned as **Hub Credits**.
* **3rd Payout:** Remaining 70% returned as **withdrawable cash**.

---

## 3. High Stakes Program

### Evaluation Parameters
* **Phase 1:** 8% Profit Target | 5% Daily Loss | 10% Max Static Loss.
* **Phase 2:** 5% Profit Target | 5% Daily Loss | 10% Max Static Loss.
* **Minimum Profitable Days:** **3 separate trading days** with at least **0.5% net profit** each (required to pass Phase 1 and Phase 2).
* **Funded Phase:** No minimum trading days; no consistency percentage rule.

### Account Allocation & Scaling Slots
* **Active Starting Account Limits:**
  * Maximum 4 active High Stakes accounts simultaneously:
    * Up to 3 × $5K accounts
    * Up to 2 × $10K accounts
    * 1 × $25K account
    * 1 × ($50K OR $100K) account
* **Scaling Independence:**
  * Scaling an account up to higher balances (e.g. $25K scaling to $40K, $50K, up to $500K) **does NOT count against other initial purchasing slots**.
  * A trader with a scaled $25K account is still 100% eligible to purchase and hold a separate $100K account.
* **Scaling Payout Mechanics:**
  * Each time the 10% scaling target is reached, the profit split (80%–100%) is **cashed out to the trader**, and the account is upgraded to a fresh higher starting balance. Profit does not need to be left in the account to "pay" for scaling.
  * Requesting regular 14-day payouts does **not** reset accumulated scaling progress.

---

## 4. Bootcamp Program

### Structure & Phases
* **Challenge Phases (Demo):** 3 consecutive challenge phases.
* **Entry Model:** Low entry fee upfront; remaining fee paid only upon completing Phase 3 to unlock the funded account. Fees are non-refundable.
* **Leverage:** 1:30 across Forex, 1:25 Metals/Indices, 1:1.5 Commodities, 1:0.6 Crypto.

### Drawdown Architecture
* **Evaluation Stages:** **5% Maximum Loss — strictly STATIC** based on initial balance. **Zero daily pause** in evaluation.
* **Funded Stage:** **4% Maximum Loss — STATIC** based on level balance.
* **Daily Pause (Funded Stage Only):** **3% Daily Pause**, resetting every midnight server time based on higher of midnight balance or equity.

---

## 5. Drawdown Mechanics: Daily vs. Maximum Loss

| Parameter | Type | Reset / Benchmark | Applies To |
| :--- | :--- | :--- | :--- |
| **Daily Loss / Daily Pause** | Dynamic | Highest value of Balance or Equity at 00:00 Server Time (EET / GMT+3) | High Stakes, Summer Plan, Bootcamp (Funded only) |
| **Maximum Total Loss (CFD)** | Static | Fixed from initial starting balance | All CFD Programs (High Stakes, Bootcamp, Summer Plan) |
| **Maximum Total Loss (Futures)** | EOD Trailing | Calculated from highest recorded end-of-day equity mark | Futures Programs |

* **Daily Drawdown Scaling:** Because the Daily Loss is calculated from midnight balance/equity, if an account balance increases, the dollar allowance for the daily loss increases proportionally on the next trading day.
* **Unwithdrawn Profits as Buffer:** Any profit left in the account expands the safety distance to the static maximum loss line.

---

## 6. Commissions, Spreads & Fees

### CFD Trading Commissions
* **Forex:** Fixed **$4.00 per standard round lot**.
* **Indices (NAS100, US30, GER40, etc.):** **$0.00 commission** (commission-free).
* **Crypto (BTCUSD, ETHUSD) & Metals (XAUUSD):** **Percentage-Based Commission** on notional trade value:
  $$\text{Commission} = \text{Lot Size} \times \text{Contract Size} \times \text{Current Market Price} \times \text{Fee } \%$$
  * As the asset price fluctuates, the dollar fee per lot adjusts automatically.
  * Crypto fees are higher (approx. 0.06%) compared to Metals (approx. 0.002%–0.003%).

### Payout Fees
* **Cash Withdrawals (Rise, Crypto, Bank Wire):** 3.5% processing fee.
* **Hub Credits:** 0% fee (100% credited to dashboard for future account purchases).

### Overnight Swaps & Rollover
* **Forex:** Charged daily at midnight; **Triple Swap on Wednesday**.
* **Indices:** Daily closure from **23:50 to 01:05 EET** (1h 15m closed); **Triple Swap on Friday**.
* **Index Swap Formula (MT5 Points):**
  $$\text{Swap USD} = \text{Swap Points} \times \text{Lots} \times \text{Point Multiplier (0.01)} \times \text{Nights}$$

---

## 7. Platform & Operational Guidelines

* **MT5 Platforms:** The5ers-branded MT5 is pre-configured with proprietary server connection strings. Generic MT5 from MetaQuotes functions identically once the broker server is located.
* **Account Reactivation Login Issues:** If an account is reactivated in the Hub but fails to connect in MT5, the trader should use **"Reset Password"** in the Hub to force synchronization.
* **Sumsub Mobile KYC Glitch:** If the KYC iframe fails to display input fields on mobile devices, advise the trader to log into the Hub via a **desktop/laptop browser**.
* **Inactivity Rule:** Accounts with **30 consecutive calendar days** without a new trade opened will expire and be terminated.

---

## 8. Prohibited Trading Practices (Terms & Conditions Summary)

1. **Arbitrage & Price Exploitation:** Latency arbitrage, price feed glitches, and platform delays.
2. **High-Frequency & Tick Scalping:** Holding durations lasting only milliseconds or a few seconds to exploit price feeds.
3. **Cross-Firm & Cross-Account Hedging:** Simultaneous buy and sell positions across different accounts or external prop firms. (Hedging on the *same* account is permitted).
4. **News Bracketing:** Placing pending buy/sell stop orders immediately around high-impact news releases.
5. **Account Sharing & Management:** Third-party "pass your challenge" services, account selling, or shared EA pools where source code is unowned.
6. **Gambling / Excessive Overleveraging:** One-sided all-in margin bets before major events without defined stop-loss risk management.
