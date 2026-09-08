# The5ers Master Knowledge Base & Operational Reference (Chat Primary Knowledge)

> **Source of truth:** `knowledge_base/the5ers_master_kb.md` (hand-maintained).  
> **Compiled into:** `knowledge_base/faq_data.md` via `python backend/compiler.py`, always ahead of the FAQ archive.  
> **Status:** Verified active knowledge base for support chat inquiries. Where the
> official FAQ archive disagrees with this document, **this document wins**.

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

---

# The5ers Official FAQ Archive (Reference Material)

> The verified operational rules above take precedence over anything in this section if the two disagree.

---

# The5%ers — FAQs (CFD / Forex)

**Source:** https://the5ers.com/faqs/  
**Captured:** 2026-09-08  
**Articles:** 212

## Contents

- **Bootcamp** (6 articles)
- **Consistency Rule** (7 articles)
- **FAQ** (26 articles)
- **FAQs** (23 articles)
- **Futures FAQs** (3 articles)
- **General** (16 articles)
- **High Stakes** (12 articles)
- **Hyper Growth** (8 articles)
- **New Program: ProGrowth** (5 articles)
- **Payments** (2 articles)
- **Payouts** (6 articles)
- **Pro** (3 articles)
- **Refunds** (1 articles)
- **Scaling Plan** (1 articles)
- **Starter** (2 articles)
- **Summer Plan** (17 articles)
- **Summer Plan (Swing)** (4 articles)
- **Uncategorized** (70 articles)

---

## Bootcamp

### How Do I Get my Funded Bootcamp Account After Completing All 3 Evaluations?

<https://the5ers.com/frequently_questions/how-do-i-get-my-funded-bootcamp-account-after-completing-all-3-evaluations/>  
_Last updated: 2026-07-28_

You can obtain a funded Bootcamp account by visiting the ‘New Account’ section, selecting the Bootcamp funded account, and paying the remaining fee.

### How Does the Bootcamp Program Payment structure Work?

<https://the5ers.com/frequently_questions/how-much-does-the-bootcamp-cost-in-total-and-how-much-is-it-to-start/>  
_Last updated: 2026-07-22_

With our Bootcamp program, you don’t have to pay everything upfront. You pay a small entry fee to start, and you only pay the remaining balance once you pass and reach the funded stage:

| **Account Size** | **Initial Entry Fee** | **Remaining Fee (Upon Success)** | **Total Cost** |
| --- | --- | --- | --- |
| **$20K Account** | $22 | $50 | **$72** |
| **$100K Account** | $95 | $205 | **$300** |
| **$250K Account** | $225 | $350 | **$575** |

### How does the Bootcamp Program work?

<https://the5ers.com/frequently_questions/how-does-the-bootcamp-program-work/>  
_Last updated: 2026-09-06_

The Bootcamp Program is designed to test the consistency and discipline of skilled traders.

[<https://wp.the5ers.com/wp-content/uploads/2026/04/How-does-the-bootcamp-program-work.mp4>](https://wp.the5ers.com/wp-content/uploads/2026/04/How-does-the-bootcamp-program-work.mp4?_=1)

Traders who want to apply for a trading seat with us will need to complete **3 challenge phases on a demo account.**

The challenges aim to look for consistency and profitability.

Once the 3 challenge phases have been completed, the trader will start trading on a funded account and be applicable for a profit split.

**Specifications**

* Leverage for all accounts – 1:30. Margin requirements apply.
* News trading is allowed. Except for bracketing strategies.
* During the pro stages, each level will be accessible up to 48 hours after completing the previous level.
* Holding open trades overnight and over the weekend is allowed. Holding Indices over the weekend carries very high swaps.
* Accounts without activity for more than 30 consecutive days will be closed.
* The bootcamp program does not have a time limit to pass the evaluation stage
* Maximum number of active accounts per trader: 4 ( 1 $250K account + 1 $100K accounts, 2 $20K accounts). Each account must have a different trading method.
* The 3% daily pause applies only to funded accounts. Traders can continue trading the very next day from 00:00 MT5 Server Time .
* First payout can be requested 14 days after receiving a funded account, and every 2 weeks after that.
* The 14-day payout cycle will reset every time you scale.
* The Bootcamp fee is non-refundable
* [Click here for the program’s terms & conditions](https://the5ers.com/terms-and-conditions/)

### How does the Bootcamp scaling plan work?

<https://the5ers.com/frequently_questions/how-does-the-bootcamp-scaling-plan-work/>  
_Last updated: 2026-06-14_

For every 5% profit generated on a **funded account**, the account balance and profit split will grow according to the table below.

![](https://wp.the5ers.com/wp-content/uploads/2026/06/bootcamp-scaling.jpeg)

The profit split starts at 50% and scales to 100%.

### How many Bootcamp accounts can I have?

<https://the5ers.com/frequently_questions/how-many-bootcamp-accounts-can-i-have/>  
_Last updated: 2026-07-22_

To ensure risk management standards are met, traders are permitted a maximum of **4 active Bootcamp accounts** overall, broken down by account type:

* **$250K Account:** Maximum of 1 account
* **$100K Account:** Maximum of 1 account
* **$20K Account:** Maximum of 2 accounts

**Notes:**

The total combined number of active accounts across all sizes cannot exceed 4.

Each account must have a different trading method.

### What is the Leverage in the Bootcamp Program?

<https://the5ers.com/frequently_questions/what-is-the-leverage-in-the-bootcamp-program/>  
_Last updated: 2026-07-22_

In the Bootcamp program, the leverage is set to 1:30.

Each asset group has a different margin requirement affecting the leverage as follows:

* Forex pairs- 1:30
* Metals- 1:25
* Indices- 1:25
* Commodities- 1: 1.5
* Crypto- 1:0.60

## Consistency Rule

### Can I Pass the Evaluation In One Day?

<https://the5ers.com/frequently_questions/one-day-pass-consistency-rule-evaluation/>  
_Last updated: 2026-07-20_

You are allowed to pass the evaluation in one trading day; however, you must still comply with the 40% consistency rule, which exists to make sure your success comes from steady, repeatable trading – not one lucky trade.

Learn more about the consistency rule [here](https://the5ers.com/?post_type=frequently_questions&p=1953117&preview=true)

### Does the Consistency Rule Limit How Much Profit I Can Make in One Day?

<https://the5ers.com/frequently_questions/does-the-consistency-rule-limit-how-much-profit-i-can-make-in-one-day/>  
_Last updated: 2026-07-20_

No. The Consistency Rule does not limit how much profit you can make in a single day. You can make any amount of profit in one day. However, if one trading day becomes too large compared to your total profits, you may need to continue trading until your overall profit increases enough for that day to fall within the allowed consistency percentage.

Your account is not failed just because your best trading day is above the consistency percentage. It only means you are not eligible for a payout or scale-up yet.

### How is the Consistency Rule Calculated?

<https://the5ers.com/frequently_questions/how-is-the-consistency-rule-calculated/>  
_Last updated: 2026-08-10_

The Consistency Rule ensures trading performance is spread out over time rather than relying on a single trade. It is calculated using your total profits, not your account size:

**Consistency Percentage Formula:** (Best Trading Day Profit ÷ Total Profits) × 100 = Consistency Percentage

To qualify for a payout or scale-up, your best trading day must account for **40% or less** of your total profit.

**How to Calculate Your Required Total Profit:** Best Trading Day Profit ÷ 0.40 = Required Total Profit

**Example (40% Consistency Rule):**

* **Best Trading Day:** $1,500
* **Calculation:** $1,500 ÷ 0.40 = $3,750
* **Requirement:** Your total account profit must be at least **$3,750**.

If your total profit is currently $2,000, your best day ($1,500) represents 75% of your gains. You are not penalized—you simply need to continue trading to build your total profit until your best day accounts for 40% or less of the total.

### Is the Consistency Rule Calculated Based on Net Profit?

<https://the5ers.com/frequently_questions/is-the-consistency-rule-calculated-based-on-net-profit/>  
_Last updated: 2026-07-20_

No. The Consistency Rule is calculated based on accumulated profitable trades, not net daily profit.

This means that for the consistency calculation, only profitable trades are added. Losing trades are not deducted from the consistency P&L.

Example: Winning and losing trades on the same day

Let’s say a trader has the following trades in one day:

Trade 1: +$1,000

Trade 2: +$500

Trade 3: -$300

Trade 4: +$200

For normal net P&L, the calculation would be:

$1,000 + $500 – $300 + $200 = $1,400

However, for the consistency calculation, only profitable trades are counted:

$1,000 + $500 + $200 = $1,700

So, the consistency P&L for that day will be $1,700, not $1,400.

This is because losing trades are not deducted when calculating the daily consistency P&L.

### What Happens if My Best Trading Day Is Above the Allowed Percentage?

<https://the5ers.com/frequently_questions/what-happens-if-my-best-trading-day-is-above-the-allowed-percentage-2/>  
_Last updated: 2026-08-10_

Your account does **not** fail or get breached.

It simply means you are not eligible for a payout or scale-up yet. You just need to continue trading and accumulate total profits until your best trading day represents 40% or less of your overall profits.

**Example (40% Consistency Rule):**

* **Best trading day:** $2,000
* **Current total profit:** $2,900
* **Current calculation:** ($2,000 ÷ $2,900) × 100 = **68.96%**

Since 68.96% is higher than 40%, the trader is not eligible yet.

**Calculating the Required Profit:**

* **Formula:** Best Trading Day ÷ 0.40 = Required Total Profit
* **Calculation:** $2,000 ÷ 0.40 = **$5,000**

The trader needs to reach at least $5,000 in total profits for their $2,000 best day to meet the 40% threshold.

**What happens after making more profit?**

Using the same example:

* **Best trading day:** $2,000
* **Current total profit:** $2,900
* **Additional profit made:** $2,100 across subsequent trades
* **New total profit:** $2,900 + $2,100 = **$5,000**

**New calculation:** ($2,000 ÷ $5,000) × 100 = **40%**

Now the best trading day represents exactly 40% of total profits, making the account fully eligible.

### What Is the Consistency Rule?

<https://the5ers.com/frequently_questions/what-is-the-consistency-rule/>  
_Last updated: 2026-07-20_

The5ers Futures has a 40% consistency rule, which means a single trade can’t account for more than 40% of your total profits.

**For example:**
In a 50K account, the evaluation profit target is $3,000.
if one trade generates $1,600 (53% of profit target), you need to keep trading and grow your total profit until that one big trade shrinks down to 40% or less of the total.

**Here’s how to calculate the new target:**
(biggest profit) ÷ 0.40 = your new target

In our case:
$1,600 ÷ 0.40 = $4,000

Once total profits reach $4,000, the $1,600 trade equals 40% and becomes compliant.

This rule applies on funded accounts as well.

### Why Does My Consistency P&L Look Higher Than My Actual Daily Net Profit?

<https://the5ers.com/frequently_questions/why-does-my-consistency-pl-look-higher-than-my-actual-daily-net-profit/>  
_Last updated: 2026-07-20_

Your consistency P&L may look higher than your normal daily net profit because the consistency rule is based on accumulated profitable trades only.

Example:

* Winning trades: $2,000
* Losing trades: -$800
* Normal net profit:
* $2,000 – $800 = $1,200
* Consistency P&L: $2,000

In this case, your actual net profit is $1,200, but your consistency P&L will show $2,000, because the losing trades are not deducted from the consistency calculation.

## FAQ

### Can I Copy My Own Trades?

<https://the5ers.com/frequently_questions/can-i-copy-my-own-trades/>  
_Last updated: 2026-07-30_

Yes, you can copy your own trades across all of your accounts without a violation.

**If you have multiple Bootcamp accounts, they will need to be traded with different strategies**

### Can I Trade During News?

<https://the5ers.com/frequently_questions/can-i-trade-during-news/>  
_Last updated: 2026-08-10_

### For Instant Funding (Hyper-Growth) and Bootcamp

News trading is allowed except for bracket strategies around news.

Bracketing is when you are adding both BUY STOP & SELL STOP at the same time in the news. Meaning if one side is hit then you entered in and when the other is hit then you are also entering the market.

### For High Stakes

Holding open trades over the news is allowed on all of our programs, but we do have some limitations on orders being executed during the news. Executing orders 2 minutes before until 2 minutes after high-impact news is prohibited. We refer to [Forex Factory](https://www.forexfactory.com/calendar) and we follow the server time.

Any profits made at this time will be deducted from the account and won’t go towards your target. Losses will be absorbed by you.

*Example: US CPI is getting announced at 15:30 server time*You can’t have a new order being executed between 15:28 – 15:32

Why? Because given the speed and slippage of the movements during high-impact news, these kinds of trades do not make money in the real market, although you may see a profit on your side.

**Note:** For high-impact news restrictions, the rule applies to the exact moment an order is **triggered and executed**, not when the pending order was placed. Any pending order that triggers inside a restricted news window will be treated as a news trading violation.

### Can I Trade on Mobile?

<https://the5ers.com/frequently_questions/do-we-offer-a-trading-platform-for-mobile-devices/>  
_Last updated: 2026-07-22_

Yes, the available mobile/web trading access depends on the trader’s region and the program.

**For non-US clients:**
You can trade using **MetaTrader 5** and **cTrader**, which is available as a mobile app for iOS and Android. This allows you to manage trades, monitor the markets, and check your account while on the go.

**Google Play: (Android)**
[MT5](https://play.google.com/store/apps/details?id=net.metaquotes.metatrader5&hl=en)
[cTrader](https://play.google.com/store/apps/details?id=com.spotware.ct&pcampaignid=web_share)

**Apple Store: (iOS)**
[MT5](https://apps.apple.com/us/app/metatrader-5/id413251709)
[cTrader](https://apps.apple.com/lk/app/ctrader-cfd-trading-charts/id767428811)

**For US-based clients:**
TradingView is currently available through the web trading platform only for all our traders. You can access it here:
<https://terminal.the5ers.com/>

### Can I Trade Using Multiple IP Addresses or Devices?

<https://the5ers.com/frequently_questions/can-i-use-multiple-ip-addresses-for-the-same-account/>  
_Last updated: 2026-07-22_

Yes, you can use multiple devices and IP addresses to access your account, provided they originate from the same primary location. However, to keep your account secure and compliant, **you must not execute trades from two different IP addresses at the same time**.

*Please note: Our compliance team may reach out to request clarification regarding your IP address usage.*

### Can I use an EA (Expert Advisor)?

<https://the5ers.com/frequently_questions/can-i-use-an-ea-expert-advisor-can-i-set-a-stealth-mode-stop-loss/>  
_Last updated: 2026-07-22_

You can use any EA you have in your trading account, as long as it does not:

* Copy trades of other person’s signals
* Do tick scalping
* Perform latency arbitrage trading
* Perform reverse arbitrage trading
* Perform hedge arbitrage trading
* Perform High-frequency trading
* Use emulators

Any accounts using these types of EAs will be canceled, banned, and will not refunded.

The stop-loss order has to be visible in the trading platform, so you cannot use a ‘stealth mode’ stop-loss.

**Additionally, the trader must own the source code of the EA.**

For a full list of our proprietary EAs please head to <https://the5ers.com/downloads/>

![](https://wp.the5ers.com/wp-content/uploads/2026/06/indicators-dl.png)

### Do I Have to Close my Positions Overnight?

<https://the5ers.com/frequently_questions/do-i-have-to-close-my-positions-overnight/>  
_Last updated: 2026-07-30_

No, we allow holding positions overnight and over the weekend as well. However, it is the trader’s responsibility to mind the implications of rollover swap conditions, volatility, liquidity, and spread conditions.

We designed our program to offer the most flexible trading fund in the forex industry and try to allow for diverse trading styles and personalities.

Please note: The swap fees on Crude Oil are -$20, and x10 on the weekend. Keep this in mind when trading Crude Oil, especially towards the end of the week.

### Do I Have to Close My Trades Over the Weekend?

<https://the5ers.com/frequently_questions/do-i-have-to-close-my-trades-over-the-weekend/>  
_Last updated: 2026-07-22_

We allow holding positions overnight and over the weekend as well. However, it is the trader’s responsibility to mind the implications of rollover swap conditions, volatility, liquidity, and spread conditions.

**Please note:**The swap fees on Crude Oil are -$20, and x10 on the weekend. Keep this in mind when trading Crude Oil, especially towards the end of the week.

Asset specifications can be found [here](https://the5ers.com/asset-specifications/).

We designed our program to offer the most flexible trading fund in the forex industry and try to allow for diverse trading styles and personalities.

**Please note:** Swap fees on Crude Oil are **$20**, and **10x on the weekend**. Keep this in mind when trading Crude Oil, especially towards the end of the week.

### Do You Charge Any Recurring Monthly Fees?

<https://the5ers.com/frequently_questions/are-there-any-hidden-fees-or-recurring-fees/>  
_Last updated: 2026-07-22_

We can assure you that at The5ers there are no hidden or recurring fees.

The only time you will be charged at a later date is once you pass the Bootcamp challenge. In the Bootcamp program, traders are only required to pay the full amount once they pass the challenge and become fully funded.

> ### Bootcamp costs:
>
> | **Account Size** | **Initial Entry Fee** | **Remaining Fee (Upon Success)** | **Total Cost** |
> | --- | --- | --- | --- |
> | **$20K Account** | $22 | $50 | **$72** |
> | **$100K Account** | $95 | $205 | **$300** |
> | **$250K Account** | $225 | $350 | **$575** |

### Does the Consistency Rule Apply to Account Balance or Account Size?

<https://the5ers.com/frequently_questions/does-the-consistency-rule-apply-to-account-balance-or-account-size/>  
_Last updated: 2026-08-17_

No. The consistency percentage is not calculated based on your account size or account balance. It is calculated based on your profits.

For example, if you have a $100K account, the 50% rule does not mean you are capped at making 50% of the account size ($50,000) in a single day.
It means your best trading day cannot represent more than 50% of the total profits you are trying to withdraw or use for scale-up eligibility.

**Quick example**

If your account has a 50% Consistency Rule:

* **Best trading day**: $5,000
* **Required total profit**: $10,000
  (Because: $5,000 ÷ 50% = $10,000)
  If your total profit is below $10,000, you need to continue trading until your total profit reaches the required amount.

### Does The5ers Have a Discord Group?

<https://the5ers.com/frequently_questions/do-the5ers-have-a-discord-group/>  
_Last updated: 2026-07-22_

Yes, The5ers have an exclusive Discord community for traders only. You can find the link on the top left corner of your [HUB dashboard](https://hub.the5ers.com/en/overview).

![](https://wp.the5ers.com/wp-content/uploads/2026/06/discord-on-hub.png)

### Does The5ers Have an Affiliate Program?

<https://the5ers.com/frequently_questions/does-the5ers-have-an-affiliate-program/>  
_Last updated: 2026-07-22_

Yes, The5ers does have an affiliate program allowing you to get paid for providing value to your audience.

Affiliates will receive a discount link which will offer their audience a discount for first-time purchases and will grant them commission.

Affiliates also will be the first to know about special discounts and will receive promotional content to boost their earnings.

[<https://wp.the5ers.com/wp-content/uploads/2026/02/Does-the5ers-have-an-affiliate-program.mp4>](https://wp.the5ers.com/wp-content/uploads/2026/02/Does-the5ers-have-an-affiliate-program.mp4?_=1)

You can find your link in your HUB:

![](https://wp.the5ers.com/wp-content/uploads/2026/06/aff-1024x307.png)

Your unique affiliate link is located in the ‘Affiliate Dashboard’ section of your hub.

Anyone is eligible to join The5ers’ affiliate program and begin earning for promoting The5ers. This is not limited to The5ers traders. There are no qualifications needed to join the affiliate program.

*If you have any other ideas on how to boost your conversions, reach out: [collaboration@the5ers.com](mailto:collaboration@the5ers.com)*

### Does The5ers offer Swap Free accounts (Islamic accounts)?

<https://the5ers.com/frequently_questions/does-the5ers-offer-swap-free-accounts-islamic-accounts/>  
_Last updated: 2026-06-14_

The5ers do offer Swap Free accounts on theFunded stage, reach out via our support chat or email [help@the5ers.com](mailto:help@the5ers.com) to let us know, and we’ll set that up for you.

### How Do I Switch Between Multiple Accounts on cTrader?

<https://the5ers.com/frequently_questions/how-to-switch-between-multiple-accounts-on-ctrader/>  
_Last updated: 2026-07-22_

Traders with multiple trading accounts linked to the same cTrader ID or email can easily switch between their accounts within the cTrader platform. To do this, you need to:

1. Log in to the cTrader platform using your cTrader ID or email.
2. Navigate to the account menu at the top right of the platform.
3. Select the desired account from the dropdown list of linked accounts.
4. The platform will switch to the selected trading account, allowing you to trade or manage it as needed.
   ![](https://wp.the5ers.com/wp-content/uploads/2026/06/switch-account.png)This process makes it convenient to manage multiple accounts without needing to log out and log back in each time, unlike MT5.

### How Many Accounts Can I Have?

<https://the5ers.com/frequently_questions/how-many-the5ers-accounts-can-i-have/>  
_Last updated: 2026-07-22_

You can have the following number of accounts of each program at the same time.

You can combine these and have up to the maximum number of accounts in all the programs. (i.e. You can have 3 High-Stakes accounts, 4 Hyper Growth accounts, and 3 Bootcamp accounts, as long as you don’t go over the limitations).

**High Stakes**

CLASSIC

You can have up to **4 active accounts** at the same time:

* **One** $2.5K account
* **One** $5K account
* **One** account of **either** $10K **or** $25K
* **One** account of **either** $50K **or** $100K

NEW

* **Three** of  $2.5K accounts
* **Three** of $5K   accounts
* **Three** of  $10K accounts
* **One**  of  $25K account
* **One** account of **either** $50K **or** $100K

**Hyper Growth**

You can have 4 Hyper Growth accounts at the same time (one $20K + one $10K + two $5K).

**Bootcamp**

You can have 4 Bootcamp accounts at the same time (one $250K + one $100K + two $20K). Each account must have a different trading method.

**ProGrowth**

Traders can hold a max of 3 accounts, one of each size ($5K, $10K, and  $20K).

### How to Log In to cTrader account After Purchase?

<https://the5ers.com/frequently_questions/how-to-log-in-to-ctrader-account-after-purchase/>  
_Last updated: 2026-08-10_

After installing the cTrader platform, the login page will appear, giving you access to all your purchased accounts.

**Step 1: Create a cTrader ID**
To log in, you must first create a cTrader ID. Important: Use the5ers email associated with your purchase to create your cTrader ID and set a secure password. Alternatively, you may log in using your Google account.

**Step 2: Logging In**

* Enter your registered email or cTrader ID (you will receive your cTrader ID via email after your purchase from the5ers and selecting cTrader as an option).
* Enter the password you set during registration.
* Alternatively, click **Sign in with Google** to log in using your Google account.

**Step 3: Access Your Accounts**
Once logged in, you can access all your purchased accounts and begin trading immediately.

**Note**: Make sure to always use the 5ers email associated with your purchase for account creation to avoid login issues.

**Note:** You can easily retrieve your MT5 and TradingView account credentials directly from your dashboard. Just navigate to your active accounts list and click the **key icon** next to your account details to view your login information.

### Is there a minimum trading day or minimum position requirement?

<https://the5ers.com/frequently_questions/is-there-a-minimum-trading-day-or-minimum-position-requirement/>  
_Last updated: 2026-08-10_

There are no minimum trades or trading days requirements for completing Level 1.
Complete Level 1 immediately when reaching the profit target. No need to wait anymore to grow your account faster.

In the High Stakes program, traders need to have a minimum of 3 profitable days to pass the evaluation and to scale.

### Is there a time limit?

<https://the5ers.com/frequently_questions/is-there-a-time-limit/>  
_Last updated: 2026-06-14_

We have no time limits for our programs. Traders may take all the time they need in order to pass the challenge. However, we want to know that traders are active. Therefore, inactive accounts for more than 30 days calendar days will expire.

### Market Trading Hours

<https://the5ers.com/frequently_questions/market-trading-hours/>  
_Last updated: 2026-06-10_

Please note: All hours are in EET*

**Forex**

Monday- Friday: 00:05-23:55

Saturday & Sunday: Closed

**Metals**

Monday- Friday: 01:05-23:50

Saturday & Sunday: Closed

**Indices**

Monday- Friday: 01:05-23:50

Saturday & Sunday: Closed

**Crypto**

Monday- Friday: 00:05-23:55

Saturday- Sunday: 00:10-23:50

**Commodities**

Monday- Friday: 01:05-23:50

Saturday & Sunday: Closed

**Please Note:**

**Indices and Commodities** – Carrying overnight positions is allowed. Carrying over the weekend is allowed but involves high swap costs.

**Swaps** – See details on MT5

*

GMT +2 during Winter Time
GMT +3 during Summer Time

### What Are The Spreads and Commissions?

<https://the5ers.com/frequently_questions/what-are-the-spreads-and-commissions/>  
_Last updated: 2026-07-22_

Every trading asset has different trading hours, and margin requirements. Make sure to know them. To review updated specifications: Go to MT5, right-click on a symbol on the market watch window –> specification.

During periods of standard market fluctuations, major currency pairs like EUR/USD, GBP/USD, USD/JPY sell from 0.2 pips to 0.9 pips. Overnight swap fees are collected and/or paid nightly.

Note that the commissions are different per asset.

* Forex = Commission is $4 per lot round trip. ($2 for opening and $2 for closing)
* Indices = No commissions.
* Crypto, Metals and Oil = Percentage-based commissions.
  + Percentage-based commission = (Commission rate/100 ) × Trade entry price × Contract size × Lot size × 2

You can view our spreads [here](https://the5ers.com/charts/).

More information available under [asset specification](https://the5ers.com/asset-specifications/)

### What is a ‘Stop Loss Order’ and How is it Calculated?

<https://the5ers.com/frequently_questions/what-is-stop-loss-order-and-how-is-it-calculated/>  
_Last updated: 2026-08-23_

A stop-loss order (SL) is a risk management tool that automatically closes a trade when the price reaches a certain level in order to limit potential losses.

![](https://wp.the5ers.com/wp-content/uploads/2026/06/stoploss.png)

**Note:** There is no mandatory Stop Loss requirement for any of The5ers programs, including Bootcamp. You can trade without setting a Stop Loss.
However, we strongly recommend using a Stop Loss on every trade as part of proper risk management and to help protect your account from excessive losses.

### What is Drawdown and How is it Calculated?

<https://the5ers.com/frequently_questions/what-is-drawdown-and-how-is-it-calculated/>  
_Last updated: 2026-07-22_

The equity stop-out level (aka drawdown) is the lowest value of the account allowed. Once the account equity value is below this level, the fund will close all running trades, and disable trading and access. No matter how much the trader profits in the account, the maximum loss (drawdown) allowance increases. The trader can always choose to keep profits in the account in order to increase the maximum drawdown amount. Any payouts requested will reduce the account balance, hence reducing the maximum drawdown.

**Example for Hyper-Growth:** If the initial balance is $10,000 and the maximum drawdown of 6% is $600 then the account will be closed below the equity level of $9,400, Let’s say your account goes up to $10,300, the maximum drawdown is now $900.

**Example for High Stakes:** If the initial balance is $5,000 and the maximum drawdown of 10% is $500 then the account will be closed below the equity level of $4,500. Let’s say your account goes up to $5,300, the maximum drawdown is now $800.

**Example for Bootcamp:** If the initial balance is $10,000 and the maximum drawdown 5% is $500, the account will be closed below the equity level of $9,500. Let’s say your account goes up to $10,300, the maximum drawdown is now $800.

### What is the KYC Verification? Who Has to do One? and What Documents are Needed?

<https://the5ers.com/frequently_questions/what-is-the-kyc-verification-who-has-to-do-one-and-what-documents-are-needed/>  
_Last updated: 2026-07-22_

The KYC (Know Your Customer) verification is a process we use to verify the identities of our traders.

This is a fast and easy process that all traders must go through the process after successfully completing a challenge.

You will need to provide us with the following documentation:

– Name
– Address
– Date of birth
– Passport or National ID
– Proof of address
– Any other documentation required by local tax authorities

Please check [this article](https://sumsub.com/supported-documents/) to review supported documents.

Please note, the process is done by a third-party provider, and we have no control over the outcome of it.

Once you have passed KYC your newly funded account will be activated and ready for you to start trading.

### When Does an Account Expire Due to Inactivity?

<https://the5ers.com/frequently_questions/what-is-the-inactivity-rule-account-feature/>  
_Last updated: 2026-08-10_

Your account will expire if **30 consecutive calendar days** pass without a brand-new trade being opened. Please note that keeping an existing position open or simply logging in does **not** count as activity and will not reset the 30-day timer. You must execute a new order to keep your account active.

### Which Broker do we Trade With?

<https://the5ers.com/frequently_questions/which-broker-do-we-trade-with/>  
_Last updated: 2026-07-22_

The5ers trades directly through commercial liquidity providers. We do not trade with common retail broker brands.

We operate differently and our trading conditions have different requirements. Confidentiality is very important to us and we take as many precautions as possible to keep our supplier’s identity confidential.

Funded traders’ accounts are connected to our pool accounts.
The pool accounts are connected to our LPs and managed by the risk department.

### Which Trading Platform Do You Use For CFDs?

<https://the5ers.com/frequently_questions/which-trading-platform-do-you-use/>  
_Last updated: 2026-08-13_

The available trading platform depends on the trader’s region.

Non-US clients can use **MetaTrader 5,** **cTrader, and TradingView.**
US-based clients can use **TradingView**.

### MetaTrader 5

There are multiple ways to download MetaTrader 5 to your computer. Once you register for an evaluation, you will be prompted to download the platform from your HUB. We will also send you an email with the download links.

![](https://wp.the5ers.com/wp-content/uploads/2026/06/creds.png)

![](https://wp.the5ers.com/wp-content/uploads/2026/06/dnl.png)

You can access it here: https://mt5.the5ers.com/terminal

### cTrader

After registering for a new account, you will receive an email like the one below. To open cTrader, simply click the “Launch cTrader” icon.

![](https://cdn.livechat-files.com/api/file/kb/file/14119155/54e2d1c086-88a9ca98071bc373457c.png)

**Note:** Using cTrader incurs an additional $10 fee on top of the program price.

**Note:** Platform choices are final once purchased and cannot be switched between. Please double-check your selection before placing your order.

**Note:** cTrader is no longer an option for new accounts for US clients.

For mobile users, both platforms are free and available for download from Google Play and the Apple Store. For more details, please see the link below:
<https://the5ers.com/faqs/do-we-offer-a-trading-platform-for-mobile-devices/>

You can access it here: <https://terminal.the5ers.com/>

### Who Should I Contact for Technical and Trading Support?

<https://the5ers.com/frequently_questions/who-should-i-contact-for-technical-and-trading-support/>  
_Last updated: 2026-09-07_

We attend to all of your needs no matter when they occur.

We believe that every trader is entitled to full support and assistance, whether it is technology inquiries, minor or major concerns, or trading-related queries.

To accelerate the treatment process, please make sure to include as much relevant information as possible, such as a full description of the case, your name, program, and program level, account number, ticket numbers, screenshots, and terminal log files.

Send all information via Email: [help@the5ers.com](mailto:help@the5ers.com) or Head to our website and click the live chat button at the bottom right

![](https://wp.the5ers.com/wp-content/uploads/2026/06/f6badf8af3-cc4b8e1e642f9ce71661.png)
For urgent matters, please include the phrase [URGENT] in the email subject line.

**Office Hours:**
Sunday – Thursday: 07:00 – 15:00 GMT

Friday: 07:00 – 12:00 GMT

## FAQs

### Are There Time Limits or Active Trading Requirements for Evaluation?

<https://the5ers.com/frequently_questions/time-limit-for-evaluation-futures/>  
_Last updated: 2026-08-10_

There is no time limit to complete the evaluation. However, you must place at least one trade every 14 calendar days to keep the account active.

Accounts with no trading activity for a 14-day period will be terminated due to inactivity.

### Can I Copytrade Between my Futures Accounts?

<https://the5ers.com/frequently_questions/can-i-copytrade-between-my-futures-accounts/>  
_Last updated: 2026-07-15_

Copy trading is only permitted on 25K and 50K accounts with a total size of up to $75,000.

One important restriction: you can only copytrade your own accounts and your own trades. You can’t copy trades from another trader, or let anyone else copy trades from you.

### Can I Hold Positions Overnight?

<https://the5ers.com/frequently_questions/overnight-holding-2/>  
_Last updated: 2026-07-15_

**Swing**: You can hold 1 mini contract or 10 micro contracts overnight. Bigger positions must close at least 10 minutes before market close.

**Day Trade**: Overnight holding is not allowed. You must manually close all positions and cancel pending orders at least 10 minutes before the close (by 4:50 PM CET).

**Both programs**: No weekend holding allowed. All positions must be closed at least 10 minutes before the Friday close.

Missing these requirements can result in account termination.

### Can I Trade During the News?

<https://the5ers.com/frequently_questions/can-i-trade-during-the-news/>  
_Last updated: 2026-07-15_

Yes. The5ers Futures allows trading during news events. There are no restrictions on trading around economic releases, as long as you follow all risk and account rules.

### Do Evaluation Profits Carry Over When Funded?

<https://the5ers.com/frequently_questions/if-i-make-profits-in-the-evaluation-phase-do-those-carry-over-when-i-get-funded/>  
_Last updated: 2026-07-15_

Profits earned during the evaluation phase do not carry over. Funded accounts start with the program’s defined starting balance and parameters.

### Does My Drawdown Limit Change After a Withdrawal?

<https://the5ers.com/frequently_questions/drawdown-after-withdrawing-a-payout/>  
_Last updated: 2026-07-20_

Every time you withdraw a payout, your drawdown limit resets to 4% below your new balance (after the withdrawal).
Example: Your account grows to $55,000, making the drawdown limit $52,800.
You withdraw $1,500, leaving a balance of $53,500. Your new drawdown limit is 4% below that ($51,360).

So each payout gives you a fresh 4% buffer based on where your balance stands after the withdrawal.

### How Many The5ers Futures Accounts Can I Have?

<https://the5ers.com/frequently_questions/how-many-the5ers-futures-accounts-can-i-have/>  
_Last updated: 2026-08-17_

150k accounts (both swing & daytrade) are limited to 1 account only

100k accounts (both swing & daytrade) are limited to 2 accounts only

### Is high-frequency trading, algorithmic trading, or hedging allowed?

<https://the5ers.com/frequently_questions/is-high-frequency-algorithmic-trading-and-hedging-allowed/>  
_Last updated: 2026-08-27_

No. These practices are strictly forbidden. Any trader found using them will be banned from our programs.

### Is There a Monthly Subscription During the Evaluation?

<https://the5ers.com/frequently_questions/is-there-a-monthly-subscription-during-the-evaluation/>  
_Last updated: 2026-08-10_

**No. The5ers Futures does not charge any monthly subscription fees.** You pay a **one-time upfront fee** when purchasing an evaluation, and there are no recurring monthly payments on either program.

### Micro Single Stock Futures

<https://the5ers.com/frequently_questions/micro-single-stock-futures/>  
_Last updated: 2026-08-20_

### **What are Micro Single Stock Futures?**

Micro Single Stock Futures are standardized, cash-settled futures contracts traded on CME Globex. Sized at 10 shares of the underlying stock (or 1/10th of a standard Single Stock Futures contract), they offer capital-efficient exposure to individual U.S. equities with nearly 24-hour access.

### **Which Micro Single Stock Futures are available to trade?**

| Ticker | Contract Name | Underlying Company |
| --- | --- | --- |
| **XAAPL** | Micro Apple Futures | Apple Inc. |
| **XAMD0** | Micro AMD Futures | Advanced Micro Devices, Inc. |
| **XAMZN** | Micro Amazon Futures | Amazon.com, Inc. |
| **XAVGO** | Micro Broadcom Futures | Broadcom Inc. |
| **XBA00** | Micro Boeing Futures | The Boeing Company |
| **XBAC0** | Micro Bank of America Futures | Bank of America Corporation |
| **XCSCO** | Micro Cisco Futures | Cisco Systems, Inc. |
| **XGOOG** | Micro Alphabet Futures | Alphabet Inc. |
| **XINTC** | Micro Intel Futures | Intel Corporation |
| **XJPM0** | Micro JPMorgan Futures | JPMorgan Chase & Co. |
| **XMETA** | Micro Meta Futures | Meta Platforms, Inc. |
| **XMSFT** | Micro Microsoft Futures | Microsoft Corporation |
| **XMU00** | Micro Micron Futures | Micron Technology, Inc. |
| **XNEM0** | Micro Newmont Futures | Newmont Corporation |
| **XNFLX** | Micro Netflix Futures | Netflix, Inc. |
| **XNVDA** | Micro NVIDIA Futures | NVIDIA Corporation |
| **XPFE0** | Micro Pfizer Futures | Pfizer Inc. |
| **XPLTR** | Micro Palantir Futures | Palantir Technologies Inc. |
| **XSPCX** | Micro SpaceX Futures | Space Exploration Technologies Corp. |
| **XTSLA** | Micro Tesla Futures | Tesla, Inc. |
| **XWMT0** | Micro Walmart Futures | Walmart Inc. |
| **XXOM0** | Micro ExxonMobil Futures | Exxon Mobil Corporation |

### What Are Each of the Futures Trading Commissions & Contracts? (2026)

<https://the5ers.com/frequently_questions/futures-trading-commissions-contracts-2026/>  
_Last updated: 2026-07-20_

#### 1. Equity Indices

|  |  |  |  |
| --- | --- | --- | --- |
| Symbol | Asset Name | 2026 Contracts | Round Turn Commission |
| ES | E-mini S&P 500 | ESH26, ESM26, ESU26, ESZ26 | $5.00 |
| NQ | E-mini Nasdaq 100 | NQH26, NQM26, NQU26, NQZ26 | $5.00 |
| YM | E-mini Dow Jones | YMH26, YMM26, YMU26, YMZ26 | $5.00 |
| RTY | E-mini Russell 2000 | RTYH26, RTYM26, RTYU26, RTYZ26 | $5.00 |
| EMD | E-mini S&P MidCap 400 | EMDH26, EMDM26, EMDU26, EMDZ26 | $5.00 |
| NKD | Nikkei 225 | NKDH26, NKDM26, NKDU26, NKDZ26 | $5.00 |
| MES | Micro S&P 500 | MESH26, MESM26, MESU26, MESZ26 | $2.50 |
| MNQ | Micro Nasdaq 100 | MNQH26, MNQM26, MNQU26, MNQZ26 | $2.50 |
| MYM | Micro Dow Jones | MYMH26, MYMM26, MYMU26, MYMZ26 | $2.50 |
| M2K | Micro Russell 2000 | M2KH26, M2KM26, M2KU26, M2KZ26 | $2.50 |

#### 2. Currencies (FX)

|  |  |  |  |
| --- | --- | --- | --- |
| Symbol | Asset Name | 2026 Contracts | Round Turn Commission |
| 6A / 6B | AUD / GBP | All Months (F-Z) | $5.00 |
| 6C / 6E | CAD / EUR | All Months (F-Z) | $5.00 |
| 6J / 6S | JPY / CHF | All Months (F-Z) | $5.00 |
| M6A | Micro AUD | All Months (F-Z) | $2.50 |
| M6E | Micro EUR | All Months (F-Z) | $2.50 |

#### 3. Metals

|  |  |  |  |
| --- | --- | --- | --- |
| Symbol | Asset Name | 2026 Contracts | Round Turn Commission |
| GC | Gold | G, J, M, Q, V, Z | $5.00 |
| SI | Silver | H, K, N, U, Z | $5.00 |
| HG | Copper | All Months (F-Z) | $5.00 |
| PL | Platinum | F, J, N, V | $5.00 |
| PA | Palladium | H, M, U, Z | $5.00 |
| MGC | Micro Gold | G, J, M, Q, V, Z | $2.50 |

#### 4. Energy

|  |  |  |  |
| --- | --- | --- | --- |
| Symbol | Asset Name | 2026 Contracts | Round Turn Commission |
| CL | Crude Oil | All Months (F-Z) | $5.00 |
| NG | Natural Gas | All Months (F-Z) | $5.00 |
| HO | Heating Oil | All Months (F-Z) | $5.00 |
| RB | RBOB Gasoline | All Months (F-Z) | $5.00 |
| QM | E-mini Crude Oil | All Months (F-Z) | $5.00 |

#### 5. Agriculture

|  |  |  |  |
| --- | --- | --- | --- |
| Symbol | Asset Name | 2026 Contracts | Round Turn Commission |
| ZC | Corn | H, K, N, U, Z | $5.00 |
| ZS | Soybeans | F, H, K, N, Q, U, X | $5.00 |
| ZW | Wheat | H, K, N, U, Z | $5.00 |
| ZM | Soymeal | F, H, K, N, Q, U, V, Z | $5.00 |

#### 6. Crypto Futures

|  |  |  |  |
| --- | --- | --- | --- |
| Symbol | Asset Name | 2026 Contracts | Round Turn Commission |
| BTC | Bitcoin | H, M, U, Z | $5.00 |
| ETH | Ethereum | H, M, U, Z | $5.00 |

### Quick Summary for Traders:

* Standard Contracts: Most standard futures carry a $5.00 commission per side.
* Micro Contracts: All Micro symbols (starting with ‘M’) carry a reduced $2.50 commission per side.
* E-mini Metals/Energy: Note that E-mini versions of Crude (QM) and Gold (QG) are still priced at $5.00.

### What are the Available Trading Instruments?

<https://the5ers.com/frequently_questions/trading-instruments/>  
_Last updated: 2026-08-31_

The following is a list of futures products available for trading within The5ers futures programs:

### Equity Index Futures:

| Instrument | Ticker BA (Continuous) | Ticker BA (with Expiration) | Market | Asset Type | Market Data | Tick Size | Tick Value | Contract Multiplier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ES: E-Mini S&P 500 | ESFUT | ESH6 | E-Mini S&P 500 | E-mini Indices | CME | 0.25 | $12.50 | 50 |
| NKD: Nikkei 225 | NKDFUT | NKDH6 | Nikkei 225 | Indices | CME | 5 | $25 | 5 |
| NQ: E-Mini Nasdaq 100 | NQFUT | NQH6 | E-mini Nasdaq 100 | E-mini Indices | CME | 0.25 | $5 | 20 |
| EMD: E-mini S&P Midcap 400 | EMDFUT | EMDH6 | E-mini S&P Midcap 400 | Indices | CME | 0.1 | $10 | 100 |
| RTY: E-mini Russell 2000 | RTYFUT | RTYH6 | E-mini Russell 2000 | E-mini Indices | CME | 0.1 | $5 | 50 |
| MES: Micro E-mini S&P 500 | MESFUT | MESH6 | Micro E-mini S&P 500 | Micro Indices | CME | 0.25 | $1.25 | 5 |
| MNQ: Micro E-mini NASDAQ 100 | MNQFUT | MNQH6 | Micro E-mini NASDAQ 100 | Micro Indices | CME | 0.25 | $5.00 | 2 |
| M2K: Micro E-mini Russell 2000 | M2KFUT | M2KH6 | Micro E-mini Russell 2000 | Micro Indices | CME | 0.1 | $0.50 | 5 |
| MYM: Micro E-mini Dow | MYMFUT | MYMH6 | Micro E-mini Dow | Micro Indices | CME | 1 | $0.50 | 0.5 |
| YM: E-mini Dow | YMFUT | YMH6 | E-mini Dow | E-mini Indices | CME | 1 | $5.00 | 5 |

### Currency Futures:

| Instrument | Ticker BA (Continuous) | Ticker BA (with Expiration) | Market | Asset Type | Market Data | Tick Size | Tick Value | Contract Multiplier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6A: Australian Dollar | 6AFUT | 6AH6 | Australian Dollar | Currencies | CME | 0.00005 | $5 | 100000 |
| 6B: British Pound | 6BFUT | 6BH6 | British Pound | Currencies | CME | 0.0001 | $6.25 | 62500 |
| 6C: Canadian Dollar | 6CFUT | 6CH6 | Canadian Dollar | Currencies | CME | 0.00005 | $5 | 100000 |
| 6E: Euro FX | 6EFUT | 6EH6 | Euro FX | Currencies | CME | 0.00005 | $6.25 | 125000 |
| 6J: Japanese Yen | 6JFUT | 6JH6 | Japanese Yen | Currencies | CME | 0.0000005 | $6.25 | 12500000 |
| 6S: Swiss Franc | 6SFUT | 6SH6 | Swiss Franc | Currencies | CME | 0.00005 | $6.25 | 125000 |
| M6A: Micro Australian Dollar | M6AFUT | M6AH6 | Micro Australian Dollar | Micro Indices | CME | 0.0001 | $1.00 | 10000 |
| M6E: Micro Euro | M6EFUT | M6EH6 | Micro Euro | Micro Indices | CME | 0.0001 | $1.25 | 12500 |

### Commodity Futures:

| Instrument | Ticker BA (Continuous) | Ticker BA (with Expiration) | Market | Asset Type | Market Data | Tick Size | Tick Value | Contract Multiplier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GC: Gold | GCFUT | GCZ5 | Gold | Precious Metal | COMEX | 0.1 | $10.00 | 100 |
| MGC: Micro Gold | MGCFUT | MGCZ5 | Micro Gold | Precious Metal | COMEX | 0.1 | $1.00 | 10 |
| SI: Silver | SILFUT | SIZ5 | Silver | Precious Metal | COMEX | 0.005 | $25.00 | 1000 |
| HG: Copper | HGFUT | HGZ5 | Copper | Base Metal | COMEX | 0.0005 | $12.50 | 25000 |
| PL: Platinum | PLFUT | PLF6 | Platinum | Precious Metal | COMEX | 0.1 | $5.00 | 50 |
| PA: Palladium | PAFUT | PAZ5 | Palladium | Precious Metal | COMEX | 0.1 | $10.00 | 100 |

### Agricultural Futures:

| Instrument | Ticker BA (Continuous) | Ticker BA (with Expiration) | Market | Asset Type | Market Data | Tick Size | Tick Value | Contract Multiplier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ZC: Corn | ZCFUT | ZCZ5 | Corn | Agricultural | CBOT | 0.25 | $12.50 | 50 |
| ZS: Soybeans | ZSFUT | ZSX5 | Soybeans | Agricultural | CBOT | 0.25 | $12.50 | 50 |
| ZW: Wheat | ZWFUT | ZWZ5 | Wheat | Agricultural | CBOT | 0.25 | $12.50 | 50 |
| ZM: Soybean Meal | ZMFUT | ZMZ5 | Soybean Meal | Agricultural | CBOT | 0.10 | $10.00 | 1 |

### Energy Futures:

| Instrument | Ticker BA (Continuous) | Ticker BA (with Expiration) | Market | Asset Type | Market Data | Tick Size | Tick Value | Contract Multiplier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CL: WTI Crude Oil | CLFUT | CLX5 | WTI Crude Oil | Energy (Oil) | NYMEX | 0.01 | $10.00 | 1000 |
| NG: Henry Hub Natural Gas | NGFUT | NGX25 | Henry Hub Natural Gas | Energy (Gas) | NYMEX | 0.001 | $10.00 | 10000 |
| HO: Heating Oil | HOFUT | HOZ5 | Heating Oil | Energy (Oil product) | NYMEX | 0.0001 | $4.20 | 42000 |
| RB: RBOB Gasoline | RBFUT | RBFV5 | RBOB Gasoline | Energy (Oil product) | NYMEX | 0.0001 | $4.20 | 42000 |
| QM: E-mini Crude Oil | QMFUT | QMH6 | E-mini Crude Oil | Energy (Oil) | NYMEX | 0.025 | $12.50 | 500 |
| QG: E-mini Natural Gas | QGFUT | QGH6 | E-mini Natural Gas | Energy (Gas) | NYMEX | 0.005 | $12.50 | 2500 |
| QO: E-mini Gold | QOFUT | QOJ6 | E-mini Gold | Precious Metal | COMEX | 0.25 | $12.50 | 50 |

### Nano Futures:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Contract Name | Ticker | Contract Multiplier | Tick Size | Tick Value |
| E-nano S&P 500 | NES | $0.50 × Index | 0.25 index points | $0.125 ($0.25 tick point scale dependent on broker tick rounding, typically $0.125 or $0.25) |
| E-nano Nasdaq-100 | NNQ | $0.20 × Index | 0.25 index points | $0.05 |
| E-nano Russell 2000 | N2K | $0.50 × Index | 0.10 index points | $0.05 |
| E-nano Dow Jones | NDOW | $0.05 × Index | 1.0 index point | $0.05 |

### What are the Contract Size Limits?

<https://the5ers.com/frequently_questions/volume-number-of-contracts/>  
_Last updated: 2026-07-21_

Number of contracts per trade:

* $25K evaluation and funded stage: 2 minis and 20 micros
* $50K evaluation and funded stage: 4 minis and 40 micros
* $1000K evaluation and funded stage: 8 minis and 80 micros
* $150K evaluation and funded stage: 12 minis and 120 micros

### What are the Futures Market Hours?

<https://the5ers.com/frequently_questions/futures-market-hours/>  
_Last updated: 2026-07-15_

The Futures markets run nearly 24 hours a day, Sunday through Friday.

**Market opens**: 5:00 PM CT Sunday.
**Market closes**: 4:00 PM CT Friday.
**Daily maintenance break**: from 4:00 to 5:00 PM CT.

**Day Trade accounts** are required to close all their positions by 4:50 PM CT.
Trades can be reopened after the daily maintenance break.

**Swing accounts** are allowed to hold positions through the maintenance break, but have to reduce their size to a maximum of 1 mini or 10 micro contracts all their positions by 4:50 PM CT.
Bigger positions can be reopened after he daily maintenance break.

**Both programs must close all positions before the weekend**

### What Are the General Rules for the Futures Program?

<https://the5ers.com/frequently_questions/what-are-the-general-rules-for-the-futures-program/>  
_Last updated: 2026-08-30_

* **Evaluation:** $25,000 account with a **6% profit target**.
* **Funded stage:** $25,000 account with a **4% profit target**.
* **Maximum daily loss (EOD): 4%** in both evaluation and funded stages.
* **Daily drawdown:** **2.5%** for both 100k and 150k programs
* **Consistency:** One trade cannot represent more than **40% of total profits**. If it does, continue trading until its share falls to 40% or less.
* **Contract limits:**Up to **2 Mini contracts or 20 Micro contracts**.
* **News trading: A**llowed.
* **Overnight positions:** Allowed on **Swing accounts**.
* **Prohibited practices:** Arbitrage and high-frequency trades lasting only a few seconds or less.
* **Fees:** A one-time **$59 evaluation fee**; no monthly fees, and the evaluation fee is refunded after the third payout.
* **Scaling:** Accounts can scale up to**$500,000**.
* **Multiple accounts:** Up to **five Futures accounts** can be traded simultaneously.
* **Platform:** Black Arrow

### What Do I Need to Know About Futures?

<https://the5ers.com/frequently_questions/about-futures/>  
_Last updated: 2026-07-21_

### Understanding Futures Asset Commissions: A Comprehensive Guide

Futures trading has become increasingly popular among investors looking to diversify their portfolios and hedge against market volatility. However, one crucial aspect that traders must consider is the commissions associated with trading futures assets. This article aims to provide a comprehensive overview of futures asset commissions, their types, and how they can impact trading strategies.

### **Quick Summary for Traders:**

* Standard Contracts: Most standard futures carry a $5.00 commission per side.
* Micro Contracts: All Micro symbols (starting with ‘M’) carry a reduced $2.50 commission per side.
* E-mini Metals/Energy: Note that E-mini versions of Crude (QM) and Gold (QG) are still priced at $5.00.

### What Are Futures Assets?

Futures assets are contracts that obligate the buyer to purchase, and the seller to sell, a specific asset at a predetermined price on a specified future date. These assets can include commodities like oil, gold, and agricultural products, as well as financial instruments such as stock indices and currencies.

### What is My Maximum Drawdown/Loss Limit?

<https://the5ers.com/frequently_questions/what-is-my-maximum-drawdown-loss/>  
_Last updated: 2026-07-15_

Both the Day Trade and Swing programs have a maximum drawdown of 4%, which is calculated from your highest midnight balance or equity.
Not the account’s initial balance.

**Example:**
You start with $50,000 and end Day 1 up $200, for a midnight balance of $50,200. Your drawdown limit is now $48,200 (4% below that balance).
On Day 2, you have a small $100 loss, bringing your balance to $50,100. Your limit stays exactly where it was  ($48,200) since that’s still based on your highest point.

### What Is the Cancellation and Refund Policy?

<https://the5ers.com/frequently_questions/cancellation-and-refund-policy/>  
_Last updated: 2026-08-10_

**Evaluation Programs:** Refund available only if no trades have been placed within 14 days of purchase.
**Black Arrow Pro:** Non-refundable, regardless of trading activity.
**Refund Processing:** Refunds are processed via your original payment method within 5 to 7 business days.

For a specific refund request, please reach out to help@the5ers.com

### What is The Daily Drawdown Limit on the $100K and $150K Accounts?

<https://the5ers.com/frequently_questions/what-is-the-daily-drawdown-limit-on-the-100k-and-150k-accounts/>  
_Last updated: 2026-08-21_

Both the $100K and $150K accounts (across Daytrade and Swing options) feature a **2.5% daily drawdown limit**. This helps ensure consistent risk management across our larger account sizes.
When the Daily Drawdown is reached, the account will be permanently terminated.

### What Is the Profit Split in The5ers Futures?

<https://the5ers.com/frequently_questions/what-is-the-profit-split-in-the5ers-futures/>  
_Last updated: 2026-07-15_

The profit split is **80/20 in your favor** across all accounts.

### What Programs Does The5ers Futures Offer?

<https://the5ers.com/frequently_questions/the5ers-futures-evaluation-programs-explained/>  
_Last updated: 2026-07-15_

We offer two evaluation paths designed for different trading styles:

* **Day Trade:** Trade during official market hours, closing all positions 10 minutes before the market close (4:50 PM CET). No overnight risk, no surprises.
* **Swing:** Hold positions overnight and ride out multi-day moves within set contract limits.

Read more about the programs’ objectives [here](https://www.the5ers.com/futures/#programs).

### What trading platform can I use with The5ers Futures?

<https://the5ers.com/frequently_questions/what-trading-platform-can-i-use-with-the5ers-futures/>  
_Last updated: 2026-06-10_

BlackArrow is currently the only trading platform supported for The5ers Futures.
BlackArrow offers seamless access across multiple devices and operating systems, including **Windows, macOS, iOS, Android, and web browsers**.
The platform supports mobile trading, with dedicated applications available on both **iOS (App Store)** and **Android (Google Play)**, allowing you to trade conveniently from anywhere.

### Who Can Join The5ers Futures ?

<https://the5ers.com/frequently_questions/who-can-join-the5ers-futures/>  
_Last updated: 2026-07-15_

Anyone over 18 years of age, with any level of trading experience, is welcome to join The5ers Futures as a trader. The5ers Futures values its expansive range of traders from all over the world, of different nationalities, cultures, and skill levels.

Due to reasons beyond our control, there is a list of countries that we can not accept. Those are: Afghanistan, Belarus, Bosnia and Herzegovina, Burundi, Central African Republic, Cuba, Congo Republic, Crimea, Democratic Republic of Congo, Donetsk, Eritrea, Guinea, Guinea-Bissau, Iraq, Iran, Israel, Kherson, Laos, Lebanon, Liberia, Libya, Luhansk, Myanmar, North Korea, Palestinian Territory, Papua New Guinea, Russia, South Sudan, Sudan, Somalia, Syria, Vanuatu, Venezuela, Yemen, Zaporizhzhia.

## Futures FAQs

### Must the Name on My Credit Card Match My Trading Account?

<https://the5ers.com/frequently_questions/payment-compliance-2/>  
_Last updated: 2026-07-21_

To ensure security and regulatory compliance, **all payments must be made using a payment method registered in your own name**. There are strictly no exceptions. While the cardholder’s name must match your trading account, the email address linked to your payment method does not need to match.

### What happens if I use someone else’s card?

Using a third-party card will result in **account disabling and payment processing delays**. If an incorrect card is used by mistake, we cannot simply update your details—we are required to refund the payment to the original card, and the account will remain disabled.

### What should I do if I don’t have a card in my name?

We recommend applying for a card through your bank or using another approved payment option registered to you. If you have questions about compliant payment methods, please contact our support team.

### What Happens if my Best Trading Day is Above the Allowed Percentage?

<https://the5ers.com/frequently_questions/what-happens-if-my-best-trading-day-is-above-the-allowed-percentage/>  
_Last updated: 2026-07-20_

Your account does not fail.

It simply means you are not eligible for a payout or scale-up yet. You need to continue trading and increase your total profits until your best trading day becomes equal to or lower than the allowed consistency percentage.

Example based on the 50% rule:

* Best trading day: $2,000
* Current total profit: $2,900
* Calculation: $2,000 ÷ $2,900 × 100 = 68.96%

Since 68.96% is higher than 50%, the trader does not meet the rule yet.

Required total profit: $2,000 ÷ 50% = $4,000

So, the trader needs to increase total profits to at least $4,000 for the best trading day to represent 50% or less.

**What happens after I make more profit?**

Using the same example:

* Best trading day: $2,000
* Current total profit: $2,900
* The trader then makes another $1,100 in accumulated profitable trades.
* New total profit: $2,900 + $1,100 = $4,000
* New calculation: $2,000 ÷ $4,000 × 100 = 50%

Now the trader meets the 50% Consistency Rule.

### Which trading platform do you use for Futures?

<https://the5ers.com/frequently_questions/which-trading-platform-do-you-use-for-futures/>  
_Last updated: 2026-07-08_

The available platform is Black Arrow

![](https://wp.the5ers.com/wp-content/uploads/2026/07/BA-300x197.png)

After registering for a new account, you will receive an email like the one below. To open Black Arrow, simply click the “SET/RESET PASSWORD” icon.

![](https://wp.the5ers.com/wp-content/uploads/2026/07/BA-1-300x159.png)

## General

### Are The5ers Regulated?

<https://the5ers.com/frequently_questions/are-the5ers-regulated/>  
_Last updated: 2026-07-28_

The5ers is a private equity fund holding ownership of a forex trading account connected to regulated liquidity providers. However, there is no regulation clause to what we do, because we are not a financial institute and do not provide any financial services. We trade using our fund’s capital, with the support of our competent funded traders.

### Can I Have More Than One Email Address Registered with The5ers?

<https://the5ers.com/frequently_questions/can-i-have-more-than-one-email-address-registered-with-the5ers/>  
_Last updated: 2026-08-23_

It is **not** allowed to register to The5ers with two different email addresses.

Traders must keep all accounts on the same email address.

Additionally, we do not permit switching email addresses.

### Can I Merge Accounts?

<https://the5ers.com/frequently_questions/can-i-merge-accounts/>  
_Last updated: 2026-08-10_

No, we are unable to merge accounts or transfer balances between them. Every account you hold remains a separate, standalone account throughout your trading journey with us. This is applicable for all The5ers accounts.

### Do I get access to extra resources?

<https://the5ers.com/frequently_questions/do-i-get-access-to-extra-resources/>  
_Last updated: 2026-08-10_

Yes! As a 5ers’ trader, you will get access to our community [trade-talk page](https://hub.the5ers.com/en/trade-talk), the trading room, exclusive webinars, our traders-only Discord, and special events.

On our Website, you can find the Trading Resources, available for everyone to take advantage of.

Head to the website, click ‘Leadn to Trade’ and see the full list under ‘Tools’:

![](https://wp.the5ers.com/wp-content/uploads/2026/06/tools.png)

For Traders that are already trading with The5ers, we have the VOD section that has guest webinars and workshops available on demand.

Head to the Client Portal (HUB) > Click on Academy > VOD > Relax and enjoy all the trading content you could imagine

![](https://wp.the5ers.com/wp-content/uploads/2026/06/Screenshot-2026-06-10-095813.png)

While we do not offer free demo accounts, you can explore our live spreads using a real account. [Click here](https://the5ers.com/charts/) for more information.

### Do I Have to Trade Under my Legal Name?

<https://the5ers.com/frequently_questions/do-i-have-to-trade-under-my-legal-name/>  
_Last updated: 2026-07-28_

Yes. Your account must be under the same name as on your ID and payment information. We do not allow traders to create accounts under fake or alternate names. This is important as your KYC will not be approved otherwise and will cause issues when becoming funded.

### Payment Compliance

<https://the5ers.com/frequently_questions/payment-compliance/>  
_Last updated: 2026-07-02_

**Q1: Can I use a credit card that is not in my name to make payments?**

**A1**: No, you must use a credit card that is registered in your name for all payments. Using a credit card under a different name disabling your account

**Q2: What happens if I use a credit card that is not in my name?**

**A2**: Payments made with a credit card under a different name will cause disabling the account. This is to ensure compliance with our security and fraud prevention policies.

**Q3: Why is it necessary to use a credit card in my name?**

**A3**: Using a credit card in your name helps us verify your identity and ensures the security of transactions. It also helps prevent fraud and ensures compliance with regulatory requirements.

**Q4: Can I update my payment information if I accidentally used a credit card under a different name?**

**A4**: No, we are required to refund the original payment method if it is not in your name and the account will remain disabled.

**Q5: What should I do if I do not have a credit card in my name?**

**A5**: If you do not have a credit card in your name, we recommend applying for one through your bank or using alternative payment methods that comply with our requirements. Please contact our support team for further assistance.

**Q6: How long will the delay be if I use a credit card under a different name?**

**A6**: The length of the delay can vary depending on the verification process. To avoid any delays, always use a credit card that matches the name on your account.

**Q7: Are there any exceptions to this policy?**

**A7**: No, there are no exceptions to this policy. All payments must be made using a credit card that is registered in the account holder’s name.

If you have any further questions or need assistance, please contact our support team. We are here to help ensure your transactions are secure and compliant.

**Q8: Does the email address registered with my credit card have to match the email on my trading account?**

**A8**: No, the email address registered with your credit card does not have to match the email on your trading account.

### Prohibited Trading Practices

<https://the5ers.com/frequently_questions/prohibited-trading-practices/>  
_Last updated: 2026-07-28_

At The5ers, we seek **genuine individual traders** who can bring their own system and strategy applied to **multiple market conditions.** Those traders will be highly rewarded, and we will be able to assist them along their trading journey. **The program is designed to cater to speculative trading strategies.**

However, some trading practices that tend to abuse our system and programs are completely forbidden and are a strict violation of our Terms and Conditions.

This works both for our evaluation phases and funded accounts.

### Prohibited trading practices that will breach our Terms and Conditions:

**Use exploitation of price discrepancies or glitches** within different markets of similar or identical assets, also known as Arbitrage Trading

*Situation:* A trader notices that the same asset is priced differently on two different exchanges. They exploit this price difference by buying/ selling the asset on the on the exchange where it’s price is different making a profit from the price discrepancy.

**High-frequency trading,** in which the majority of trade durations span is measured within a few seconds or less.

*Situation:* A trader uses sophisticated algorithms to execute thousands of trades within milliseconds, taking advantage of small price movements in the market. They aim to profit from these rapid trades, leveraging technology to gain an edge.

**Bulk trading,** is when multiple trades are open simultaneously.

*Situation:* A trader opens manually  or uses automatic trading tools that open multiple trades at the same time, clearly showing a trader is not behind the strategy activity.

**Bracketing strategy** by opening pending orders around high-impact news. It consists of opening buy and sell stops close to the price before the news.

*Situation:* Ahead of a major economic announcement, a trader places both buy and sell pending orders just above and below the current market price. When the news is released, triggering volatility, one of the pending orders is executed, allowing the trader to profit from the price swing.

**Intentionally or unintentionally employ trading strategies that take advantage of errors within the system**, such as inaccuracies in price display or delays in updating

*Situation:* Due to a technical glitch, the trading platform displays incorrect price quotes for a particular asset. A trader quickly identifies this discrepancy and places trades based on the inaccurate prices, intending to profit before the error is corrected.

**Trade coordination or copy trading with other traders** **or accounts**

*Situation:* A group of traders collaborates to execute coordinated trades across multiple accounts. They share signals and strategies with each other, effectively copying each other’s trades to amplify their collective profits.

**One-sided bets,** which refer to a trading strategy where the user consistently takes positions in one single direction.

*Situation:* A trader consistently enters long positions on a particular currency pair, believing it will continue to rise indefinitely, regardless of market conditions or contrary indicators.

**Expert Advisors that scalp during the****rollover**night to take advantage of the price feed

*Situation:* A trader uses an Expert Advisor programmed to exploit price discrepancies during the rollover period when liquidity is lower. The EA executes rapid trades to capitalize on small price differences between bid and ask prices.

**EA from a third party, where other traders have the same trades open** (copy trading)

*Situation:* A trader purchases an EA from a third-party provider without realizing that many other traders are already using the same EA with identical trading strategies, leading to saturation in the market and diminished effectiveness.

**Using an EA from a provider where the trader does not own the sourc****e code.**

*Situation:* A trader subscribes to an EA service where they receive pre-built trading algorithms without access to the underlying source code. They deploy these EAs without understanding how they operate or being able to customize them to their needs.

**Tick Scalping**

*Situation:* A trader engages in rapid-fire trading, entering and exiting positions within seconds based on minor fluctuations in price that occur with each tick of the market.

**Hedge Arbitrage Trading**

*Situation:* A trader simultaneously buys and sells the same currency pair on different accounts exploiting temporary pricing inefficiencies

**Reverse Arbitrage Trading**

**Account Sharing or Reselling accounts with other individuals or entities**

*Situation:* A trader sells access to their funded trading account to another individual or entity, allowing them to trade on their behalf or use the account for their own purposes in exchange for a fee or profit share.

Account Management Services **“Pass your Challenge”** is also prohibited

*Situation:* A services to manage other individuals’ challenge accounts, promising to pass the evaluation phase and gain funding on their behalf in exchange for a percentage of the profits generated.

**Cross-operator coordinated trading, performed alone or in concert with other persons across accounts held with different providers, or proprietary trading firms, for manipulative purposes, for example by simultaneously entering into opposite positions across those accounts.**

Situation: A trader holds funded accounts with The5ers and another proprietary trading firm simultaneously. They place a buy position on one account and a sell position on the other on the same instrument, hedging their exposure across firms and ensuring a profit regardless of market direction.

**Using trading strategies that artificially distribute profit across multiple days without proportionally distributing market risk, such as holding opposing positions on the same or highly correlated instruments, or partially closing and managing the same trade idea across multiple trading days, in order to artificially inflate the number of profitable days recorded on the account.**

Situation: A trader opens a large long position and simultaneously hedges it with a smaller short on a correlated instrument. They close the profitable leg on one day and the losing leg on another, manufacturing two separate profitable days on the account while the underlying market risk was taken in a single move.

**Using automated robots or Expert Advisors that cause the trading account to generate an excessive number of server requests per day through individual trades or pending orders being opened, modified, or closed, causing overload of the trading server.**

Situation: A trader deploys a high-frequency Expert Advisor that continuously opens, modifies, and cancels pending orders across multiple instruments throughout the trading session, generating thousands of server-side requests per day and placing disproportionate load on the platform infrastructure.

**Opening position sizes or a number of positions that are substantially larger or smaller than your typical trading activity, whether compared across your own accounts or between your evaluation and funded account stages; or repeatedly concentrating risk in a single instrument or group of correlated instruments in a way that builds cumulative overexposure beyond what market-standard risk management would permit**

Situation: A trader uses small, consistent lot sizes throughout the evaluation period and then, on the final day before hitting the profit target, opens a single position ten times larger than any previous trade in order to close out the required profit in one move.

**Overleveraging or overexposure to a single instrument or correlated instruments in a manner inconsistent with market-standard risk management practices that a reasonable person would apply when trading with their own capital.**

Situation: A trader allocates their entire available margin to a single currency pair ahead of a high-impact news event, taking a position size that would be financially catastrophic in a live account but carries limited personal consequence in a simulated environment, in order to maximise the chance of hitting the profit target in a single trade.

**Generating disproportionate concentrated exposure through a highly speculative position resulting in rapid profits within a limited trading history, where the overall activity does not demonstrate sustainable, risk-managed trading across varying market conditions and is inconsistent with realistic proprietary trading practices or the responsible capital management standards expected of funded traders.**

Situation: A trader with a short account history places a single high-leverage position on a volatile instrument during an abnormal market event, generating a large profit in a very short period. The trade represents the majority of the account’s total profit and bears no resemblance to the measured, consistent trading activity the evaluation process is designed to assess. While no individual rule threshold was technically breached, the overall pattern of activity does not reflect how a responsible trader would manage real proprietary capital, and creates unjustified financial and operational risk exposure to the Company.

**Engaging in speculative position-taking that resembles gambling rather than legitimate proprietary trading, characterised by one or more of the following: opening positions of disproportionate size relative to account balance or prior trading activity; placing trades without a demonstrable analytical or risk management basis; concentrating exposure in a single instrument or event outcome; or relying on leverage as the primary driver of profit rather than market analysis or trading skill.**

Situation: A trader opens an outsized leveraged position immediately before a major scheduled event with no stop loss, no prior trading history on the account, and no evidence of a defined strategy, generating a large profit purely as a result of favourable price movement rather than any demonstrable trading edge. The activity is inconsistent with how a responsible trader would deploy proprietary capital and does not reflect the sustainable trading behaviour the evaluation process is designed to identify.

If your account has been found abusing the system and violating the trading rules, we will terminate the entire relationship between you and the company and/or suspend, block and/or restrict your access to the services for specific functions immediately.

**Any refund or profit will not be processed, and you will be permanently banned** from The5ers Fund.

### Weekly Trading Contest

<https://the5ers.com/frequently_questions/weekly-trading-contest/>  
_Last updated: 2026-08-10_

Each week brings a new contest, a fresh leaderboard, and a chance to be one of 100 traders walking away with prizes.

**Prizes**

* 1st place: 60K High Stakes
* 2nd place: 20K High Stakes
* 3rd place: 10K High Stakes
* 4th place: 5K High Stakes
* 5th place: 5K High Stakes
* 6th place: 5K High Stakes
* 7th place: 5K High Stakes
* 8th place: 5K High Stakes
* 9th place: 5K High Stakes
* 10th place: 5K High Stakes
* 90 secondary winners: 11-20th Places: 20K Bootcamp | 21-80th Places: $5 HUB CREDITS | 81-100th Places: $5 TTP HUB CREDITS

**Rules**

* Only one position can be open at any given moment.
* Daily Loss: 5%
* Maximum Loss: 10%
* Leverage: 1:30
* EA’s are NOT allowed
* Account Balance: $10,000
* News trading is allowed
* Prizes will be awarded the day after the contest ends.

**Registration**

* Traders can only register for one contest at a time
* Contests run from 10am on Wednesday until 10 am on Tuesday every week (server time)
* Once one contest ends, the following week’s contest can be registered to
* The contest is limited to the first 20,000 traders who register
* The contest account credentials will be available on your dashboard on the day the contest begins
* The contest is only available on MT5
* Participation is free

### What Are Hub Credits?

<https://the5ers.com/frequently_questions/what-is-hub-credits/>  
_Last updated: 2026-08-10_

Hub Credits are bonus rewards deposited right into your trader dashboard to help you save on new program purchases! Any trader in an eligible region can use them toward purchasing new challenges.

Here are a few quick rules to keep in mind:

* **Non-Cashable:** Credits can only be used toward program purchases and **cannot be cashed out or withdrawn**.
* **Expiration:** Credits are valid for **3 months** from the date they are granted.
* **Combining Discounts:** Hub Credits cannot be combined with promotional codes or discount coupons.
* **Partial Payments:** If your credit balance doesn’t cover the full program price, you can pay the remaining balance with your preferred payment method. The remaining amount to be paid must be at least **$12**.
* **Partial use of Hub Credits is not supported**. Traders can only use Hub Credits if, after applying them, the remaining balance is at least $12.

### What are The5ers Certificates?

<https://the5ers.com/frequently_questions/what-are-the5ers-certificates/>  
_Last updated: 2026-08-11_

The5ers certificates are official, personalized digital documents awarded to traders to recognize key milestones in their trading journey, such as passing an evaluation phase, reaching a new scaling level, or receiving a profit payout.

### **How do I earn a certificate?**

Certificates are generated automatically when you achieve specific milestones on the platform, including:

* **Passing an Evaluation:** Completing Phase 1, Phase 2, or a 1-Step challenge.
* **Receiving a Payout:** Reaching your first or subsequent funded account profit splits.

### **Where can I find and download my certificate?**

You can access, view, and download all your earned certificates directly from your **Trader Dashboard** under the **Certificates** or **Achievements** tab.

### **Can I share my certificate on social media?**

Yes! Your dashboard includes direct links to download high-resolution PDFs or share your verified certificates straight to platforms like LinkedIn, X (Twitter), and Instagram.

### **Does my certificate display my real name?**

Yes, certificates are issued using the legal name registered on your verified The5ers profile.

### **Is there any fee to receive a certificate?**

No. All digital certificates are issued free of charge as part of your achievements with The5ers.

### What Does it Mean if my Account is ‘waiting for risk’?

<https://the5ers.com/frequently_questions/what-does-it-mean-if-my-account-is-waiting-for-risk/>  
_Last updated: 2026-08-10_

If your account status shows **‘****waiting for risk,’** it simply means your account is undergoing our standard review process for a milestone—such as a payout request or an account scaling evaluation.

There is nothing to worry about. This is a routine check to ensure everything is in order, and the review process can take **up to 72 hours**. If our Risk Team needs any additional details or clarification, they will reach out to you directly via email. Otherwise, no action is needed on your part, and your request will proceed as soon as it is approved**.**

### What Instruments Can I trade with The5ers?

<https://the5ers.com/frequently_questions/what-instruments-can-i-trade-with-the5ers/>  
_Last updated: 2026-07-28_

The5ers traders can trade Forex, Commodities, Indexes, Cryptocurrencies, and Energy Commodities

Below you can see a full list of assets taken from MT5:

![](https://wp.the5ers.com/wp-content/uploads/2025/08/instruments.png)

The full list can be found here with a full breakdown of the asset’s specifications <https://the5ers.com/asset-specifications/>

### What is constancy Rule?

<https://the5ers.com/frequently_questions/what-is-constancy-rule/>  
_Last updated: 2026-07-09_

**Consistency Rule Explained**

The Consistency Rule is designed to encourage stable and consistent trading performance. It means that your best trading day cannot account for more than the allowed consistency percentage of your total profits when you request a payout or scale-up.

Depending on your account type or region, the consistency percentage may be different. Some accounts may have a 30% Consistency Rule, while others may have a 50% Consistency Rule or another percentage.
The examples below are mainly based on the 50% Consistency Rule, but the same calculation method applies to other consistency percentages as well.

**Does the Consistency Rule limit how much profit I can make in one day?**

No. The Consistency Rule does not limit how much profit you can make in a single day. You can make any amount of profit in one day. However, if one trading day becomes too large compared to your total profits, you may need to continue trading until your overall profit increases enough for that day to fall within the allowed consistency percentage.
Your account is not failed just because your best trading day is above the consistency percentage. It only means you are not eligible for a payout or scale-up yet.

**How is the Consistency Rule calculated?**

The basic formula is:

**Best trading day ÷ Total profits × 100 = Consistency percentage**

To meet the rule, your best trading day must be equal to or lower than the allowed percentage.
For example, if your account has a 50% Consistency Rule, your best trading day must not be more than 50% of your total profits.

**Example based on the 50% Consistency Rule**

* Best trading day: $1,500
* Consistency limit: 50%
* Required total profit:
* $1,500 ÷ 50% = $3,000

This means that if your best trading day is $1,500, your total profit must be at least $3,000 for that day to represent 50% or less of your total profits.
If your total profit is only $1,500 and all of it came from one day, you are not eligible yet. You would need to continue trading and increase your total profits.

**Example based on the 30% Consistency Rule**

* Best trading day: $1,500
* Consistency limit: 30%
* Required total profit:
* $1,500 ÷ 30% = $5,000

This means that if your best trading day is $1,500, your total profit must be at least $5,000 for that day to represent 30% or less of your total profits.

**Is the Consistency Rule calculated based on net profit?**

No. The Consistency Rule is calculated based on accumulated profitable trades, not net daily profit.
This means that for the consistency calculation, only profitable trades are added. Losing trades are not deducted from the consistency P&L.

Example: Winning and losing trades on the same day
Let’s say a trader has the following trades in one day:
Trade 1: +$1,000
Trade 2: +$500
Trade 3: -$300
Trade 4: +$200
For normal net P&L, the calculation would be:
$1,000 + $500 – $300 + $200 = $1,400
However, for the consistency calculation, only profitable trades are counted:

$1,000 + $500 + $200 = $1,700

So, the consistency P&L for that day will be $1,700, not $1,400.
This is because losing trades are not deducted when calculating the daily consistency P&L.

**Why does my consistency P&L look higher than my actual daily net profit?**

Your consistency P&L may look higher than your normal daily net profit because the consistency rule is based on accumulated profitable trades only.

Example:

* Winning trades: $2,000
* Losing trades: -$800
* Normal net profit:
* $2,000 – $800 = $1,200
* Consistency P&L: $2,000

In this case, your actual net profit is $1,200, but your consistency P&L will show $2,000, because the losing trades are not deducted from the consistency calculation.

**What happens if my best trading day is above the allowed percentage?**

Your account does not fail.
It simply means you are not eligible for a payout or scale-up yet. You need to continue trading and increase your total profits until your best trading day becomes equal to or lower than the allowed consistency percentage.

Example based on the 50% rule:

* Best trading day: $2,000
* Current total profit: $2,900
* Calculation: $2,000 ÷ $2,900 × 100 = 68.96%

Since 68.96% is higher than 50%, the trader does not meet the rule yet.
Required total profit: $2,000 ÷ 50% = $4,000
So, the trader needs to increase total profits to at least $4,000 for the best trading day to represent 50% or less.

**What happens after I make more profit?**

Using the same example:

* Best trading day: $2,000
* Current total profit: $2,900
* The trader then makes another $1,100 in accumulated profitable trades.
* New total profit: $2,900 + $1,100 = $4,000
* New calculation: $2,000 ÷ $4,000 × 100 = 50%

Now the trader meets the 50% Consistency Rule.

**Does the Consistency Rule apply to account balance or account size?**

No. The consistency percentage is not calculated based on your account size or account balance. It is calculated based on your profits.

For example, if you have a $100K account, the 50% rule does not mean you can only make 50% of the account size in one day.
It means your best trading day cannot represent more than 50% of the total profits you are trying to withdraw or use for scale-up eligibility.

**Example**
If your account has a 50% Consistency Rule:

* Best trading day: $5,000
* Required total profit: $10,000
* Because: $5,000 ÷ 50% = $10,000

If your total profit is below $10,000, you need to continue trading until your total profit reaches the required amount.

### Where is The5ers registered?

<https://the5ers.com/frequently_questions/where-is-the5ers-registered/>  
_Last updated: 2026-06-10_

The5ers.com is a website legally owned by FIVE PERCENT ONLINE LTD, incorporated in the State of Israel
Company Number 515864007 and FIVE PERCENT ONLINE LTD, incorporated in the UK Company number 12553363

### Who can join The5ers?

<https://the5ers.com/frequently_questions/who-can-join-the5ers/>  
_Last updated: 2026-06-23_

Anyone over 18 years of age, with any level of trading experience, is welcome to join The5ers as a trader. The5ers values its expansive range of traders from all over the world, of different nationalities, cultures, and skill levels.

Due to reasons beyond our control, there is a list of countries that we can not accept. Those are: Afghanistan, Belarus, Bosnia and Herzegovina, Burundi, Central African Republic, Cuba, Congo Republic, Crimea, Democratic Republic of Congo, Donetsk, Eritrea, Guinea, Guinea-Bissau, Iraq, Iran, Israel, Kherson, Laos, Lebanon, Liberia, Libya, Luhansk, Myanmar, North Korea, Palestinian Territory, Papua New Guinea, Russia, South Sudan, Sudan, Somalia, Syria, Vanuatu, Venezuela, Yemen, Zaporizhzhia.

### Who legally owns the trading accounts that traders use?

<https://the5ers.com/frequently_questions/who-legally-owns-the-trading-accounts-that-traders-use/>  
_Last updated: 2026-06-10_

Every trading account and its capital value are legally owned by [The 5%ers’ Funded Trading Program](https://the5ers.com/).

## High Stakes

### How do you define a profitable day in the High Stakes program?

<https://the5ers.com/frequently_questions/how-do-you-define-a-profitable-day-in-the-high-stakes-program/>  
_Last updated: 2026-07-05_

A profitable day is a day on which the closed positions made a positive profit* of at least 0.5% of the initial balance.
**The positive profit is calculated as follows: Minimum(Midnight Balance, Midnight Equity) – Previous Day Balance*
Eg; Account size of $100K for you to gain a profitable day you will need to close the day with a min of $500 net in profit.

$100,000*0.005= $500

[<https://wp.the5ers.com/wp-content/uploads/2026/06/minimum_profitable_days.mp4_v1-1080p.mp4>](https://wp.the5ers.com/wp-content/uploads/2026/06/minimum_profitable_days.mp4_v1-1080p.mp4?_=8)

### How does growth work in the High Stakes Program?

<https://the5ers.com/frequently_questions/how-does-growth-work-in-the-high-stakes-program/>  
_Last updated: 2026-06-10_

Once you are a funded trader, you will be entitled to extra funding depending on your performance.

At every funding stage, you have a milestone target of 10%. Once the 10% milestone is hit you will need to close your trades and we will advance your account to the next level.

You can see below the full list of progression you can have on High-stakes

![](https://wp.the5ers.com/wp-content/uploads/2026/06/621d238cb2-8a0a2a8c10a8fd43e322.jpeg)

### How does scaling & monthly fixed payout work?

<https://the5ers.com/frequently_questions/how-does-scaling-monthly-fixed-payout-work/>  
_Last updated: 2026-06-10_

Monthly fix payout are available for our High Stakes traders.

Once your account balance hits $350,000 you will be eligible for a monthly fixed payout of $4000.

We will credit your trading account with your monthly paycheck. This can be withdrawn on your next payout cycle. Once your account balance hits $500,000 you will be eligible for a monthly fixed payout of $10,000.

Scaling Plan:

[<https://wp.the5ers.com/wp-content/uploads/2025/08/high_stakes_forex_funding_program___scaling_plan_v1-1080p.mp4>](https://wp.the5ers.com/wp-content/uploads/2025/08/high_stakes_forex_funding_program___scaling_plan_v1-1080p.mp4?_=9)

### How many High Stakes accounts can I have?

<https://the5ers.com/frequently_questions/how-many-high-stakes-accounts-can-i-have/>  
_Last updated: 2026-06-10_

**High Stakes**

* **You can have the following number of accounts of each program at the same time.**
* **You can combine these and have up to the maximum number of accounts in all the programs. (i.e. You can have 3 High-Stakes accounts, 4 Hyper Growth accounts, and 3 Bootcamp accounts, as long as you don’t go over the limitations).**
* **Classic and New program account limits are counted independently.** You can hold accounts from both programs at the same time, as long as each program’s individual limits are respected.

**Cross-program rules:**

* **You cannot** hold the same size account across both programs ONLY for the $50K and $100K tiers, you may only hold one of these across Classic and New combined
* $2.5K, $5K, $10K, and $25K accounts **can** be duplicated across programs

**Examples of valid combinations:**

* **1× $5K Classic + 3× $5K New**
* 1× $10K Classic + 3× $10K New
* 1× $25K Classic + 1× $25K New
* 1× $100K Classic (no $50K or $100K New allowed alongside this)

**CLASSIC**
**You can have up to 4 active accounts** at the same time:

* **One** $2.5K account
* **One** $5K account
* **One** account of **either** $10K **or** $25K
* **One** account of **either** $50K **or** $100K

**NEW**

* **Three** of $2.5K accounts
* **Three** of $5K accounts
* **Three** of $10K accounts
* **One** $25K account
* **One** account of **either** $50K **or** $100K

### Is News Trading Allowed in the High Stakes Program?

<https://the5ers.com/frequently_questions/is-news-trading-allowed-in-the-high-stakes-program2024/>  
_Last updated: 2026-08-10_

Holding open trades over high-impact news is allowed.

However, it is not allowed to execute any order (market buy, market sell, buy stop, sell stop, buy limit, sell limit) 2 minutes prior, after or within to high-impact news in the related currency or index. We refer to Forex Factory and we follow the server time.

Any trade opened within the 2-minute period before or after a high-impact (red folder) news event will be classified as a soft breach.

**Any profits made at this time will be deducted from the account and won’t go towards your target. Losses will be absorbed by you.**

This rule applies exclusively to opening new positions (including market orders and entry pending orders). It does not eliminate the risk of existing trades hitting pre-set Stop Loss or Take Profit orders during news events.

### Payout Policy and Hub Credit in the High Stakes Program

<https://the5ers.com/frequently_questions/payout-policy-and-hub-credit-in-the-high-stakes-program/>  
_Last updated: 2026-08-11_

Throughout the 2 phase evaluation, a payout request cannot be fulfilled. Payout payments can only be processed once the trader is fully funded and has generated a minimum of $150 in profit.

Once you’re a funded trader, you’ll get the new funded account which you will be able to request a profit payout bi-weekly through your dashboard.

You will have the possibility to withdraw your profits through Rise, Bank Transfer or crypto payments.

You can choose to keep the profit in the account which would increase the maximum drawdown amount

**** The refundable fee is added to the equity of your funded account. You will be eligible to receive 70% of this fee back with your first payout, provided you have generated a minimum profit of $150 and your account has been active for at least 14 days.***

What is HUB Credit/how do I get it?

We reward your progress! At each major step—passing Phase 1 and Phase 2—we will credit your Hub with a portion of **your initial program fee**.

You can use hub credit towards the cost of a new challenge in your trading dashboard. It can be redeemed at the checkout when purchasing a new challenge. Note that hub credits are non-withdrawable.

Here’s what you unlock along your journey:

* Pass Step 1: Get 10% Hub Credit
* Pass Step 2: Get 20% Hub Credit
* Funded Stage: Get a 70% refund

Example for a 100K account which costs $545:

* After passing Step 1 → trader receives 10% in Hub Credits ($54.5)
* After passing Step 2 → trader receives 20% in Hub Credits ($109)
* At the funded stage → The 70% ($381.5) will be added to the account equity and can be withdrawn with the first payout (after 14 days).

**Please note:** The 70% refund applies only to payments made with external funds, not Hub Credit. If you paid for the account partially with Hub Credit, the 70% will be calculated based only on the portion paid with your original payment method.

**Please note:** Traders can request cryptocurrency withdrawals up to a maximum limit of $1,500 per transaction.

**Please note:** The minimum for a withdrawal is $150. This applies to the payout amount after the profit split.

This update is designed to reward traders earlier in their journey rather than only at the end.

### What are the general rules for the High Stakes Program?

<https://the5ers.com/frequently_questions/what-are-the-general-rules-for-the-high-stakes-program/>  
_Last updated: 2026-08-10_

High Stakes is a 2-step evaluation challenge where you have unlimited time to complete the evaluation and get funded

[<https://wp.the5ers.com/wp-content/uploads/2025/08/high_stakes_forex_funding_program___overview_v1-1080p.mp4>](https://wp.the5ers.com/wp-content/uploads/2025/08/high_stakes_forex_funding_program___overview_v1-1080p.mp4?_=2)

**New High Stakes:**
We require traders to have at least 3 profitable trading days and to reach a target of **10% for Phase 1 and 5% for Phase 2.**
**Classic High Stakes:**
We require traders to have at least 3 profitable trading days and to reach a target of **8% for Phase 1 and 5% for Phase 2.**

Trading accounts without activity will automatically expire if left inactive. The inactivity limit is **30 consecutive days** for evaluation accounts (starting from your registration day) and **60 consecutive days** for funded accounts.

The **max loss on the account is 10% from your initial balance** (absolute drawdown) and 5% daily drawdown that is taken from the closing equity or balance of your previous day. This is taken at 00:00 UTC+3.

Once passed you will be given a new funded account with the ability to withdraw funds from your dashboard every 14 days. You will have the possibility to withdraw your profits via Crypto or RISE through your hub.

**Note:** Holding open trades over the news is allowed on all of our programs, but we do have some limitations on orders being executed during the news. Executing orders 2 minutes before until 2 minutes after high-impact news is prohibited. We refer to [Forex Factory](https://www.forexfactory.com/calendar) and we follow the server time.

Any profits made at this time will be deducted from the account and won’t go towards your target. Losses will be absorbed by you.

### What are the Key Benefits of the High Stakes Program?

<https://the5ers.com/frequently_questions/what-are-the-key-benefits-of-the-high-stakes-program/>  
_Last updated: 2026-08-23_

The High Stakes program offers traders lots of great benefits, including, but not limited to:

* Highest split in the industry – up to 100%
* Monthly salary available
* Largest drawdown
* Highest leverage of all programs
* Better entry price in the industry
* Reward from 1st stage

[<https://wp.the5ers.com/wp-content/uploads/2025/08/high_stakes_forex_funding_program___overview_v1-1080p.mp4>](https://wp.the5ers.com/wp-content/uploads/2025/08/high_stakes_forex_funding_program___overview_v1-1080p.mp4?_=3)

### What is the drawdown rule for High Stakes?

<https://the5ers.com/frequently_questions/what-is-the-drawdown-rule-for-high-stakes/>  
_Last updated: 2026-08-10_

The max loss on the account is 10% from your initial balance (absolute drawdown) and 5% daily drawdown that is taken from the closing equity or balance of your previous day (the highest between them). This is taken at 00:00 server time.

E.g. If you have a $100K account and your equity is $110,000 at 23:59 server time, then after rollover, your daily max loss will be $5,500. Meaning if your equity goes below $104,500 your account will close.

***Rolling over a trade from the previous day.** D*aily loss will be taken from the highest number between your balance and equity. if your balance is $105,000 but your floating trade is in a $1K loss (equity $104,000) then the snapshot will be taken from the $105K Level (Balance)

Reaching any of these limits will lead to the termination of the account.

[<https://wp.the5ers.com/wp-content/uploads/2026/06/high_stakes_forex_funding_program_drawdown_explained_v1-1080p.mp4>](https://wp.the5ers.com/wp-content/uploads/2026/06/high_stakes_forex_funding_program_drawdown_explained_v1-1080p.mp4?_=11)

### What is the High Stakes program?

<https://the5ers.com/frequently_questions/what-is-the-high-stakes-program/>  
_Last updated: 2026-06-10_

The high-risk-high-reward 2-step program. Traders will need to show their skills over 2 evaluations in order to get funded.

### What is the leverage in the High Stakes program?

<https://the5ers.com/frequently_questions/what-is-the-leverage-in-the-high-stakes-program/>  
_Last updated: 2026-06-10_

In the High Stakes program, the leverage is set to 1:100.

Each asset group has a different margin requirement affecting the leverage as follows:

**Forex pairs**– 1:100

**Indices and Metals**– 1:25

**Commodities**– 1:5

**Crypto**– 1:2

**PLEASE NOTE:** Due to potential extreme market volatility, the following temporary adjustment applies to 50K and 100K High Stakes funded accounts:

* Leverage has been reduced to 1:5 on Oil only.

Please note that swaps and spreads may also be subject to adjustment in line with market volatility and liquidity conditions. These measures will remain in effect until further notice.

These updates are aligned with current market volatility and are susceptible to changes. We recommend you review these changes carefully and adjust any open positions or pending orders accordingly.

### What is the maximum loss and the maximum daily loss in the High Stakes program?

<https://the5ers.com/frequently_questions/what-is-the-maximum-loss-and-the-maximum-daily-loss-in-the-high-stakes-program/>  
_Last updated: 2026-06-10_

The maximum loss is 10% of the initial balance.

Daily loss is 5% of the starting equity of the day OR the starting balance of the day (the highest between them) at MT5 Server Time. (GMT +2 winter time or GMT+3 summer Time)

Reaching any of these limits will lead to the termination of the account.

[<https://wp.the5ers.com/wp-content/uploads/2026/06/high_stakes_forex_funding_program_drawdown_explained_v1-1080p.mp4>](https://wp.the5ers.com/wp-content/uploads/2026/06/high_stakes_forex_funding_program_drawdown_explained_v1-1080p.mp4?_=10)

## Hyper Growth

### How Does the Daily Pause Work?

<https://the5ers.com/frequently_questions/how-does-the-daily-pause-work/>  
_Last updated: 2026-07-30_

The Daily Pause applies for the Hyper Growth stage in all stages and the Bootcamp funded stage.

The daily pause is a loss protection that helps traders avoid significant losses.

When an account hits the daily pause level, all open trades get closed, and the account remains disabled until the next trading day.

The daily pause is taken from midnight 00:00 GMT+3 from the balance or equity of your account, the highest between them.

E.g. If your balance is $10,500 at midnight, your daily pause level will be 3% of $10,500. This means if your equity falls below $10,185 you will be paused for that trading day, and your account will only reopen after 00:00 GMT+3

[<https://wp.the5ers.com/wp-content/uploads/2026/06/How-does-the-daily-pause-work.mp4>](https://wp.the5ers.com/wp-content/uploads/2026/06/How-does-the-daily-pause-work.mp4?_=7)

### How does the Hyper Growth Program work?

<https://the5ers.com/frequently_questions/how-does-the-hyper-growth-program-work/>  
_Last updated: 2026-08-10_

Hyper Growth is the program with the highest success rate in the Industry. There are no TIME LIMITS with an amazing growth opportunity … it’s the fastest way to start managing millions

[<https://wp.the5ers.com/wp-content/uploads/2025/08/How-does-the-hyper-growth-program-work-1.mp4>](https://wp.the5ers.com/wp-content/uploads/2025/08/How-does-the-hyper-growth-program-work-1.mp4?_=6)

#### SPECIFICATIONS

* Double your funded account on every target
* The profit target, maximum loss and daily pause remain the same for the funded stages.
* The daily pause does not terminate an account. It only disables the account for the current day. Traders can continue trading the very next day at 00:00 MT5 Server Time.
* Accounts that hit the stopout level will be terminated. The stopout level is 6% below the inital account size.
* When completing each level, traders will receive bonuses to their HUB on top of their profit split.
* Holding open trades over the weekend is allowed.
* Growth up to $4M
* Leverage 1:30
* News trading is allowed. (except for bracket strategies around news or others mentioned on our T&C)
* Assets available: FX, Metals, Indices.
* Platform: Mt5 Hedge in desk, web and mobile version.
* No minimum trades or days requirements for completing level 1
* Holding indices over the weekend is allowed but carries a high swap.
* Complete Level 1 immediately when reaching the profit target
* Maximum capital per trader on evaluation account sizes: $40,000. (eg. you can have 4 X $10K, or 2 X $20K accounts all adding to the max starting capital of $40K)
* First payout 14 days after receiving a funded account, and every 2 weeks after that.
* The 14-day payout cycle will reset every time you have a new account scaled.
* The Hyper Growth fee is non-refundable
* Traders have all the time they need in order to pass the challenge. However, we want to know that traders are active. Therefore, inactive accounts for more than 30 consecutive days will get expired.

### How does the Hyper Growth scaling plan work?

<https://the5ers.com/frequently_questions/how-does-the-hyper-growth-scaling-plan-work/>  
_Last updated: 2026-07-31_

For every 10% profit generated on a **funded account**, the account balance will **double**. The profit split starts at 50% and scales to 100%.
Check out the tables below for more details.

* **Evaluation Phase:** For accounts in the $5K to $20K range, a 50%/50% profit split applies during the evaluation process.
* **Funded Phase:** Once the Evaluation phase is successfully passed, the account becomes **Funded**, and the payout ratio automatically increases to **75%/25% (includes 10K and 20 K funded).**

![](https://wp.the5ers.com/wp-content/uploads/2026/06/hyper-growth-scaling.jpeg)
At every stage traders receive bonuses, starting from $15, and scaling up to $1600!
These bonuses will be paid as hub credit which traders can use for future purchases of The5ers programs.

### How Many Hyper Growth Accounts I Can Have?

<https://the5ers.com/frequently_questions/how-many-hyper-growth-accounts-i-can-have/>  
_Last updated: 2026-07-30_

You can have a max of 4 accounts.

1 * $10K, 1*  *$20K, and 2** $5K accounts (all adding to the max starting capital of $40K).

### Is Copy Trading allowed in the Hyper Growth program?

<https://the5ers.com/frequently_questions/is-copy-trading-allowed-in-the-hyper-growth-program/>  
_Last updated: 2026-07-30_

Yes, copy trading between your own accounts is allowed. However, once your total managed capital reaches **$500K** across all programs and accounts, copy trading across accounts is no longer permitted.

### What Are the Bonuses in the Hyper Growth Program?

<https://the5ers.com/frequently_questions/what-are-the-bonuses-in-the-hyper-growth-program/>  
_Last updated: 2026-07-30_

Bonuses are an extra reward for your performance, and will be given once you pass to a new funding level (this is on top of your profit split). You will receive the bonuses as hub credit and you will be able to use them for future internal purchases for other funding programs.

You can learn more in the video below:

[<https://wp.the5ers.com/wp-content/uploads/2025/08/What-are-the-bonuses-in-the-HG-program.mp4>](https://wp.the5ers.com/wp-content/uploads/2025/08/What-are-the-bonuses-in-the-HG-program.mp4?_=4)

### What are the key benefits of the Hyper Growth program?

<https://the5ers.com/frequently_questions/what-are-the-key-benefits-of-the-hyper-growth-program/>  
_Last updated: 2026-07-05_

There are many benefits of the Hyper Growth program, including:

* Double your account every 10% while withdrawing profits
* Grow your account up to $4M and keep 100% of the profits
* Profit split + bonus on each milestone
* Withdraw profits from the first objective

[<https://wp.the5ers.com/wp-content/uploads/2025/08/What-are-the-key-benefits-of-the-HG-program.mp4>](https://wp.the5ers.com/wp-content/uploads/2025/08/What-are-the-key-benefits-of-the-HG-program.mp4?_=5)

### What is the Leverage in the Hyper Growth Program?

<https://the5ers.com/frequently_questions/what-is-the-leverage-in-the-hyper-growth-program/>  
_Last updated: 2026-07-30_

In the Hyper Growth program, the leverage is set to 1:30.

Each asset group has a different margin requirement affecting the leverage as follows:

Forex pairs- 1:30

Indices and Metals- 1:25

Commodities- 1: 1.5

Crypto- 1:0.60

## New Program: ProGrowth

### How do you Define a Profitable Day in the ProGrowth Program?

<https://the5ers.com/frequently_questions/how-do-you-define-a-profitable-day-in-the-progrowth-program/>  
_Last updated: 2026-07-30_

A profitable day is a day on which the closed positions made a positive profit* of at least 0.5% of the initial balance.
**The positive profit is calculated as follows: Minimum(Midnight Balance, Midnight Equity) – Previous Day Balance*

> Eg; Account size of $5K for you to gain a profitable day you will need to close the day with a min of $25 net in profit.
>
> $5,000 * 0.005 = $25

### How Many ProGrowth Accounts Can I Have?

<https://the5ers.com/frequently_questions/how-many-progrowth-accounts-can-i-have/>  
_Last updated: 2026-06-10_

Traders can hold a max of 4 accounts, one of each size ($5K, $10K, $20K and $50K).

### What is the Drawdown Rule for ProGrowth?

<https://the5ers.com/frequently_questions/what-is-the-drawdown-rule-for-progrowth/>  
_Last updated: 2026-07-30_

The maximum loss for ProGrowth is 6% of the initial balance.

Daily loss of ProGrowth is 3% of the starting equity of the day OR the starting balance of the day (the highest between them) at MT5 Server Time. (GMT +2 winter time or GMT+3 summer Time)

Reaching any of these limits will lead to the termination of the account.

### What is the Leverage in the ProGrowth Program?

<https://the5ers.com/frequently_questions/what-is-the-leverage-in-the-progrowth-program/>  
_Last updated: 2026-07-30_

In the ProGrowth program, the leverage is set to 1:30.

Each asset group has a different margin requirement affecting the leverage as follows:

Forex pairs- 1:30

Indices and Metals- 1:25

Commodities- 1: 1.5

Crypto- 1:0.60

### What is the Scaling Plan for the Progrowth Program?

<https://the5ers.com/frequently_questions/what-is-the-scaling-plan-for-the-progrowth-program/>  
_Last updated: 2026-08-10_

Your account will scale up upon meeting each 10% target.

You can check out the full scaling table [here](https://the5ers.com/hyper-growth/).

*Pro Growth uses a 1-step evaluation process rather than providing instant funding without an assessment.

## Payments

### Which Payment Methods Can I Use?

<https://the5ers.com/frequently_questions/which-payment-methods-can-i-use/>  
_Last updated: 2026-07-14_

We support a variety of secure payment methods for your convenience:

* **Credit and Debit Cards** (Visa, Mastercard)
* **PayPal**
* **Checkout** (Visa, Mastercard, Apple Pay, Google Pay)
* **Confirmo** (Cryptocurrency payments)

> Note; ** Traders that pay via Confimo (Cryptocurrency) will need to take into account extra fees for network transactions, if the payment is underpaid due to fees the order will not complete and the account will not open.
>
> Traders can pay via Confirmo in the following currencies:
>
> USDT via TRON or Arbitrum network
> USDC via Ethereum or Arbitrum network
> TRX via TRON network
> If the payment is sent in the wrong cryptocurrency or use wrong network, funds can be lost.

### Which Payment Methods Can I Use?

<https://the5ers.com/frequently_questions/what-payment-methods-are-available/>  
_Last updated: 2026-07-15_

We support a variety of secure payment methods for your convenience:

* Credit and Debit Cards (Visa, Mastercard)
* PayPal
* Checkout (Visa, Mastercard, Apple Pay, Google Pay)
* Confirmo (Cryptocurrency payments)

**Note:** Traders that pay via Confimo (Cryptocurrency) will need to take into account extra fees for network transactions, if the payment is underpaid due to fees the order will not complete and the account will not open.

Traders can pay via Confirmo in the following currencies:

USDT via TRON or Arbitrum network
USDC via Ethereum or Arbitrum network
TRX via TRON network
If the payment is sent in the wrong cryptocurrency or use wrong network, funds can be lost.

## Payouts

### Crypto Withdrawals

<https://the5ers.com/frequently_questions/crypto-withdrawals/>  
_Last updated: 2026-06-10_

Withdrawal requests smaller than $1500 may be processed via direct crypto payment. Larger amounts will be paid via Rise.
In order to process payment via Crypto, you will need a crypto wallet address, the coin, and the network you would like to use.

We offer the following options:

* USDT on the Tron network
* USDC on the Ethereum network
* ETH
* LTC

### What are the Payout Caps?

<https://the5ers.com/frequently_questions/what-are-the-payout-caps/>  
_Last updated: 2026-08-18_

Each funded account has a maximum payout amount per withdrawal, depending on the account size.

**25K Account**
Payout caps remain consistent at $1,250 across all payouts.

**50K-$150K Accounts**

Each payout is capped at 3% of your current balance.

**Example:**

If you have a **$100,000 account** and request a withdrawal, your maximum allowed payout for that request would be **$3,000** (3% of $100,000).

### What Are the Requirements for a Payout?

<https://the5ers.com/frequently_questions/what-do-i-need-for-a-withdrawal/>  
_Last updated: 2026-07-30_

To request a payout, your funded futures account needs to meet all of the following:

* It’s a Funded Futures Account (evaluation accounts aren’t eligible)
* You’ve reached 4% profit or more, calculated from your initial account balance
* The account is at least 14 days old

Once all four conditions are met, you’re clear to submit your payout request.

### What Payout Methods are Available?

<https://the5ers.com/frequently_questions/what-payout-methods-are-available/>  
_Last updated: 2026-07-22_

The5ers can process payouts via Rise, Cryptocurrencies, Bank Transfers, or add as Hub Credits onto the dashboard. The added hub credits can be used toward purchasing programs and are non-withdrawable.

> **Commission Percentage on payouts:**
> Rise, Cryptocurrencies, and Bank Transfers – 3.5%
> HUB Credits – No commission percentage

Payouts can only be processed once the trader passes onto funded levels.
After that, you will have the possibility to withdraw your profits on a biweekly basis.

The payout cycle will reset every time you have a new account scaled.

> **Withdrawals won’t affect your scaling of the account**

You can request a payout from your hub using the ‘Withdrawal’ button.

### What Payout Methods Are Supported?

<https://the5ers.com/frequently_questions/what-payout-methods-are-supported/>  
_Last updated: 2026-07-15_

The5ers can process payouts via Rise, Cryptocurrencies, Bank Transfers, or add Hub Credits onto the dashboard.

*Hub credits can only be used toward purchasing programs and are non-withdrawable.

**Commission Percentage on payouts:**
Rise and Cryptocurrencies, and Bank Transfers – 3.5%
HUB Credits – No commission percentage

Payouts can only be processed once an account is at the funded stage.

After that, you will have the possibility to withdraw your profits on a biweekly (14-day period) basis.

*The payout cycle will reset every time you have a new account scaled.

**Withdrawals won’t affect your scaling of the account**

You can request a payout from your hub via the ‘Withdrawal’ button.

### Withdrawals: Everything You Need to Know

<https://the5ers.com/frequently_questions/withdrawals-everything-you-need-to-know/>  
_Last updated: 2026-08-24_

**When can I request a withdrawal?**

* You can request your first withdrawal 14 days after your funded account is activated.
* Subsequent withdrawal requests can be made every 2 weeks from your last approved withdrawal.
* Note: If your account is scaled, the 14-day timer resets from the scaling date.

**What is the minimum withdrawal amount?**

* You can request a withdrawal once you reach a profit of $150.

**How long does it take to process a withdrawal?**

* All approved withdrawal requests are typically processed in up to 3 business days.
* If additional information is required, our support team will contact you.

**Supported Withdrawal Methods**

We currently support the following four payout options:

1. **Rise**
   * Funds are transferred to your Rise Works account: [www.riseworks.io](https://www.riseworks.io)
   * Your Rise email must match your The5ers account email.
   * Commission: 3.5% per withdrawal
2. **Crypto**
   * Sent to the wallet address provided during your withdrawal request
   * Limit: $1,500 per withdrawal
   * Commission: 3.5% per withdrawal
   * Supported currencies:
     + USDT (TRC20 – Tron Network)
     + USDC (ERC20 – Ethereum Network)
     + ETH
     + LTC
3. **Bank Transfer**
   * Sent to your bank account using the details you provided on the withdrawal page
   * Limit & timing: Vary depending on your bank’s processing conditions
   * Commission: 3.5% per withdrawal + any fees charged by the receiving bank
4. **Hub Credits**
   * Your payout is converted to Hub Credits in your The5ers account
   * Hub Credits can be used to purchase new accounts only
   * No commission applied

**Notes:**

* All open trades must be closed before submitting a payout request
* Always double-check your withdrawal details before submitting
* We do not allow withdrawals to be split between two different methods
* Traders can also check their own withdrawal requests and current status here: https://hub.the5ers.com/en/purchases/withdrawals
* A payout marked as Pending Approval is currently being reviewed by our Risk Team. The review usually takes 24–48 business hours, excluding weekends and holidays.
* For help or further questions, please contact us at: help@the5ers.com

## Pro

### What are the Summer Contests and Prizes?

<https://the5ers.com/frequently_questions/what-are-the-summer-contests-and-prizes/>  
_Last updated: 2026-08-02_

Purchasing a Pro Booster (at least 4 Summer Plans) marks you eligible to participate in The5ers Summer Contests set to take place on August 24th at 10:00 AM GMT!

**You will receive a link to the contest a few days before it goes live.**

The rules for the Summer Contest are as follows:

* + 1- $20k account
  + 2. 3% max loss ($600)
  + 3. Max loss per trade = 3% ($600)
  + 4- Leverage 1:30

The Prizes for the Summer Contests are:

* + 1st Place: $2,000
  + 2nd Place: $1,000
  + 3rd Place: $500
  + 4th-10th Place: 5K Evaluation Account
  + 11th-20th Place: 5K Bootcamp Evaluation Account
  + 21st-80th Place: $5 HUB Credits

**Traders must be sure to purchase their Summer Plans BEFORE entering the Summer Contest. This is required to be eligible for the grand prize (and any subsequent awards).*

### What is the 5K Trade the Pool Account?

<https://the5ers.com/frequently_questions/what-is-the-5k-trade-the-pool-account/>  
_Last updated: 2026-07-30_

If you purchase 4 Summer Plans, you’re eligible to receive $59 in HUB Credits equal to a 5K evaluation account (Day Trade – Beginner) with Trade the Pool (trade 12,000+ stocks and ETFs). You must make sure you’re logged in to the [Trade The Pool Hub](https://tradethepool.com/).

### What is TraderSync and TrendSpider?

<https://the5ers.com/frequently_questions/what-is-tradersync-and-trendspider/>  
_Last updated: 2026-07-29_

TraderSync is a suite of analysis and research trading tools designed to ensure traders are fully informed before taking action. Track your analytics and even replay key market moments, all with TraderSync! Traders are eligible to receive a one-month free TraderSync membership with their Pro Booster.

TrendSpider is the future of technical and fundamental analysis that every serious trader needs to take their understanding of the markets to the next level! Traders are eligible to receive a free one-month TrendSpider membership with their Pro Booster.

Your free trial lasts 1 month—if you don’t want to roll into a paid subscription, make sure to cancel directly with TraderSync and TrendSpider (check your inbox for instructions).

## Refunds

### How Does the Evaluation Fee Refund Work?

<https://the5ers.com/frequently_questions/evaluation-fee-refund/>  
_Last updated: 2026-07-20_

**Q: How does the evaluation fee refund work?**

A: Once you successfully receive your third payout on any funded futures trading account, we will refund the full evaluation fee you originally paid. The refund is automatically added to your total equity at the time of your third payout. It is our way of rewarding traders who demonstrate consistent, long-term performance on our platform.
 **Q: Which accounts are eligible for a fee refund?**

A: Every funded futures account that successfully reaches its third payout qualifies for this program. This applies universally across both our Day Trade and Swing trading programs, regardless of the account size you choose to trade.
 **Q: How much of the evaluation fee will I get back?**

A: You will receive a 100% refund of exactly what you paid out-of-pocket for the initial account evaluation fee—no more and no less. For example, if you purchased a 50K Day Trade account for $100, that full $100 will be added back to your balance once your third payout is officially processed and confirmed.

## Scaling Plan

### What is the Scaling Plan?

<https://the5ers.com/frequently_questions/futures-scaling-plan-explanied/>  
_Last updated: 2026-08-31_

Once you’re funded, your account grows automatically every time you hit a 10% profit milestone.

Here’s the process:
You reach the 10% profit target and close all open positions.
Your account is temporarily disabled and sent to our Risk Department for review.
Once approved, you’re issued a new, scaled-up account.

Each time you scale, two things increase:
Your balance is increased by 5%
Your contract limits increase by +1 mini contract and +10 micro contracts.

### Here’s how your new account balance is built:

|  |  |
| --- | --- |
|  | **Amount** |
| Original balance | $50,000 |
| +5% buying power increase | $2,500 |
| +Your profit (80% of $5,000) | $4,000 |
| **New account balance** | **$52,500** |

**Note:** There is no ‘minimum profitable days’ rule in our Futures program.

## Starter

### What are the Exclusive Sessions?

<https://the5ers.com/frequently_questions/what-are-the-exclusive-sessions/>  
_Last updated: 2026-07-29_

Will Davies, The5ers Content Leader, with a decade of professional trading experience, will be leading bi-weekly trader-exclusive sessions that make up *The Consistent Trader Framework*!

* *AUG. 7, 1300 GMT+1: The Mindset Shift – Thinking Like a Professional Trader*

* *AUG. 21, 1300 GMT+1: Mastering Trading Psychology*

* *SEP. 4, 1300 GMT+1: Building Consistency*

* *SEP. 18, 1300 GMT+1: The Blueprint to Long-Term Success*

More information, and invitations to the sessions, will be sent to your registered email.

### What is The5ers’ Affiliate Program?

<https://the5ers.com/frequently_questions/what-is-the5ers-affiliate-program/>  
_Last updated: 2026-07-29_

If you purchase a Summer Plan account, you are eligible to be upgraded to The5ers Affiliates Program and receive upgraded Commission terms. Make sure to sign up to be an Affiliate in The5ers Hub.

* 10% Commission (no discount) -> 10% Commission and 5% discount for first-time users

## Summer Plan

### 1-Step Plan Rules & Specifications

<https://the5ers.com/frequently_questions/1-step-plan-rules-specifications/>  
_Last updated: 2026-07-15_

### **How do I pass the 1-Step evaluation?**

You need to hit a 10% profit target on your $100,000 evaluation account while respecting all risk parameters:

* Maximum Loss: 6% of your initial balance.
* Daily Loss Limit: 3% of the previous day’s closing balance.
* Consistency Requirement: 50% (no single trading day can account for more than 50% of your total profit).

### **What happens after I pass the 1-Step evaluation?**

You move directly to a $100,000 funded account. Plus, as a passing bonus, you will receive a 10% credit from your evaluation fee applied directly toward your Funded account.

### Do the rules change once I am funded on the 1-Step plan?

No. To keep things simple and structured, your profit target (10%) and risk rules (6% max loss, 3% daily loss, and 50% consistency) remain exactly the same on your funded account as they were during evaluation.

### **What are the payout limits for the 1-Step funded account?**

To request a payout, you must have a minimum PnL of $250 in profit. The maximum amount you can withdraw is capped at $2,000 per payout cycle.

### What is the refund policy?

Upon receiving your funded account, you will be credited with 10% of your fee back in Hub Credits.

Additionally, you will receive a 90% cash refund of your initial fee included directly in your third payout.

### 2-Step Plan Rules & Specifications

<https://the5ers.com/frequently_questions/2-step-plan-rules-specifications/>  
_Last updated: 2026-09-07_

### **What is the difference between the “New” and “Classic” 2-Step options?**

The 2-Step plan offers two entry tiers for the $100,000 account to fit your budget and strategy:

* New ($149): Phase 1 profit target is 10%; Phase 2 is 5%.
* Classic ($179): Phase 1 profit target is 8%; Phase 2 is 5%.

### **What are the risk parameters for the 2-Step Plan evaluation?**

Both the New and Classic versions share the same evaluation risk model:

* Maximum Loss: 10% of your initial balance.
* Daily Loss Limit: 3% of the previous day’s closing balance or equity balance, whichever is higher.
* *Note: There is no consistency rule during the evaluation phases for the 2-Step plan.*

### **Does the consistency rule apply to the 2-Step Plan?**

Yes, but only on the Funded account. Once you pass both Phase 1 and Phase 2 and receive your live $100,000 funded account, a 50% consistency requirement will apply to your trading.

### What are the rewards and payout limits for the 2-Step plan?

* Milestone Bonuses: Completing Step 1 and Step 2 each unlocks HUB credits that you can use for future internal purchases.
* Payout Limits: You need a minimum PnL of $250 in profit to request a withdrawal. The payout cap is $2000 per payout cycle.

### Does the $200K High Stakes Summer Plan Support Account Scaling?

<https://the5ers.com/frequently_questions/does-the-200k-high-stakes-summer-plan-support-account-scaling-2/>  
_Last updated: 2026-08-11_

No. The $200K Summer Plan is a specialized, limited-time program engineered to provide maximum capital allocation upfront at a heavily discounted entry price. Scaling is not available for this program, and the account balance remains fixed at $200,000.

### How do I Receive my Evaluation Fee Refund and Summer Boost Credits?

<https://the5ers.com/frequently_questions/how-do-i-receive-my-evaluation-fee-refund-and-summer-boost-credits-2/>  
_Last updated: 2026-08-11_

Your evaluation fee refund is distributed in three distinct stages throughout your progression:

* **Step 1 Completion:** You receive 10% of your evaluation fee back as HUB credits as soon as you pass Phase 1.
* **Step 2 Completion (Reaching Funded Stage):** You receive 20% of your evaluation fee back as HUB credits as soon as you pass Phase 2 and gain funded status.
* **3rd Payout Milestone:** The remaining 70% of your evaluation fee is paid out directly as withdrawable cash alongside your 3rd profit payout.

### How do Payouts, Profit Split, and Consistency Work on the $200K Funded Account?

<https://the5ers.com/frequently_questions/how-do-payouts-profit-split-and-consistency-work-on-the-200k-funded-account-2/>  
_Last updated: 2026-08-11_

Once you complete both evaluation steps and move to your $200,000 funded account:

* **Profit Share:** You receive an 80/20 profit split (80% to the trader).
* **Payout Cap & Minimum:** The minimum withdrawal is $250, with a payout cap of up to $3,000 per payout cycle.
* **Daily Consistency Rule:** A 50% daily consistency requirement applies, meaning no single trading day can account for more than 50% of your total generated profit at the time of a payout request.

### How Does the Daily Loss Limit Work?

<https://the5ers.com/frequently_questions/how-does-the-daily-loss-limit-work-2/>  
_Last updated: 2026-08-10_

For both the 1-Step and 2-Step summer plans, the daily loss limit is 3%. It is calculated at the end of each trading day based on 3% of your account’s EOD equity OR balance—whichever of the two is higher.

When the Daily Loss is reached, the account is permanently terminated.

### How does the Daily Loss Limit Work?

<https://the5ers.com/frequently_questions/how-does-the-daily-loss-limit-work/>  
_Last updated: 2026-08-10_

For both the 1-Step and 2-Step summer plans, the daily loss limit is 3%. It is calculated at 00:00 MT5 Server Time based on 3% of your day’s starting equity OR starting balance—whichever of the two is higher.

When the Daily Loss is breached, the account is permanently terminated.

### How is Consistency Calculated?

<https://the5ers.com/frequently_questions/how-is-the-consistency-calculated/>  
_Last updated: 2026-08-20_

The basic formula is:

**(Best trading day ÷ profits from profitable days) × 100 = Consistency percentage**

To meet the rule, your best trading day must be equal to or lower than the allowed percentage.

For example, if your account has a 50% Consistency Rule, your best trading day must not be more than 50% of your total profits.

**Example based on the 50% Consistency Rule**

* Best trading day: $1,500
* Consistency limit: 50%
* Required total profit:
* $1,500 ÷ 50% = $3,000

This means that if your best trading day is $1,500, your total profit must be at least $3,000 for that day to represent 50% or less of your total profits.

If your total profit is only $1,500 and all of it came from one day, you are not eligible yet. You would need to continue trading and increase your total profits.

### Is Copy Trading Allowed Between my Accounts?

<https://the5ers.com/frequently_questions/is-copy-trading-allowed-between-my-accounts-2/>  
_Last updated: 2026-08-11_

Yes. Copy trading between your own Summer Plan accounts is fully allowed. If you hold multiple accounts (such as both $200K plans and additional $100K accounts), you can replicate trades across them simultaneously using trade copiers or management software.

### Summer Booster Q&A

<https://the5ers.com/frequently_questions/summer-booster-qa/>  
_Last updated: 2026-07-29_

**General: What is TradePoints and how many points can I earn with my Boosters?**

* TradePoints is a rewards platform built by traders, for traders, where you can convert earned points for physical rewards such as special event admission, vacations, gift cards, and more!
* Every $ you spend towards a Starter Booster gets you 2 points.
* Every $ spent towards a Pro Booster gets you 10 points.

**Pro: What is TraderSync and TrendSpider?**

* TraderSync is a suite of analysis and research trading tools designed to ensure traders are fully informed before taking action. Track your analytics and even replay key market moments, all with TraderSync! Traders are eligible to receive a one-month free TraderSync membership with their Pro Booster.

* TrendSpider is the future of technical and fundamental analysis that every serious trader needs to take their understanding of the markets to the next level! Traders are eligible to receive a free one-month TrendSpider membership with their Pro Booster.

* Your free trial lasts 1 month—if you don’t want to roll into a paid subscription, make sure to cancel directly with TraderSync and TrendSpider (check your inbox for instructions).

**General: What are Hub Credits?**

* With HUB Credits, you can purchase new evaluation accounts within The5ers ecosystem.

**Pro: What is the 5K Trade the Pool account?**

* If you purchase 4 Summer Plans, you’re eligible to receive $59 in HUB Credits equal to a 5K evaluation account (Day Trade – Beginner) with Trade the Pool (trade 12,000+ stocks and ETFs). You must make sure you’re logged in to the Trade The Pool Hub.

**Pro: What are the Summer Contests and Prizes?**

* Purchasing a Pro Booster (at least 4 Summer Plans) marks you eligible to participate in The5ers Summer Contests set to take place on August 24th at 10:00 AM GMT!

### What are Hub Credits?

<https://the5ers.com/frequently_questions/what-are-hub-credits/>  
_Last updated: 2026-07-29_

With HUB Credits, you can purchase new evaluation accounts within The5ers ecosystem.

### What are Summer Boosters?

<https://the5ers.com/frequently_questions/what-are-summer-boosters/>  
_Last updated: 2026-07-29_

Boosters are free gifts from The5ers that you unlock after you purchase a Summer Plan. Purchasing 1 Summer Plan unlocks the Starter Booster, and even more gifts are unlocked with the Pro Booster (after 4+ Summer Plans are purchased).

### What are the Maximum Allocation and Account Limits for the Summer Plan?

<https://the5ers.com/frequently_questions/what-are-the-maximum-allocation-and-account-limits-for-the-summer-plan-2/>  
_Last updated: 2026-08-11_

To offer high trading capacity while managing risk, the following allocation rules apply:

* Maximum Buying Power Cap: The total aggregate buying power allowed across all Summer Plan accounts is $600,000 per trader.
* $200K Account Options: Each trader is permitted to purchase one $200K (10/5 Plan) and one $200K (8/5 Plan) account simultaneously.
* Combining Account Sizes: Since holding two $200K accounts equals $400K in total capital, you still have $200K in remaining allocation under the $600K cap. This means you can also hold additional $100K accounts (e.g., up to two $100K accounts) alongside your $200K accounts.

### What Are The New $200K High Stakes Summer Plan Options?

<https://the5ers.com/frequently_questions/what-are-the-new-200k-high-stakes-summer-plan-options-2/>  
_Last updated: 2026-08-11_

* **200K (10/5 Plan) – $249:** Pass Step 1 with a **10% target** and Step 2 with a **5% target**.
* **200K (8/5 Plan) – $279:** Pass Step 1 with a lower **8% target** and Step 2 with a **5% target**.

### What is the Summer Plan, and what are my Options?

<https://the5ers.com/frequently_questions/what-is-the-summer-plan-and-what-are-my-options/>  
_Last updated: 2026-08-10_

The Summer Plan is a limited-time opportunity to get funded with a $100,000 account starting from as low as $149. You can choose between two distinct paths to funding depending on your trading style:

* 1-Step Plan ($249): A single evaluation phase with a 10% profit target and a fast track straight to funding.
* 2-Step Plan (From $149): A traditional two-phase evaluation with two different pricing and target options (New or Classic).

**Note:** Buy up to 4 (2 x 10/5 and 2 x 8/5) accounts at the same time

**Note:** The Summer Plan has a payout cap of up to $2,000 per payout cycle

**Note:** News trading: Executing orders 2 minutes before until 2 minutes after high-impact news is prohibited.

**Note:** Traders may copy trades between 2 Summer Plan accounts under the condition that both accounts are owned by the same trader. Copying trades from third-party accounts is strictly prohibited

### What is TradePoints and How Many Points Can I Earn with my Boosters?

<https://the5ers.com/frequently_questions/what-is-tradepoints-and-how-many-points-can-i-earn-with-my-boosters/>  
_Last updated: 2026-07-29_

* TradePoints is a rewards platform built by traders, for traders, where you can convert earned points for physical rewards such as special event admission, vacations, gift cards, and more!
* Every $ you spend towards a Starter Booster gets you 2 points.
* Every $ spent towards a Pro Booster gets you 10 points.

### What Rewards are Included in the Starter and Pro Boosters?

<https://the5ers.com/frequently_questions/what-rewards-are-included-in-the-starter-and-pro-boosters/>  
_Last updated: 2026-07-29_

*The Starter Booster contains:*

* $10 one-time Hub Credits for Trade the Pool
* Access to The5ers’ Affiliate Program
* Exclusive access to The5ers’ Spotify playlist
* Exclusive access to a strategy series with Will Davies
* TradePoints Rewards

*The Pro Booster contains:*

* $15 one-time Hub Credits for your The5ers or Futures Account
* FREE $5K Trade the Pool Account
* Exclusive access to Summer Contests
* FREE one-month TraderSync trial
* FREE one-month TrendSpider trial

## Summer Plan (Swing)

### How Many Contracts Can I Hold Overnight?

<https://the5ers.com/frequently_questions/how-many-contracts-can-i-hold-overnight/>  
_Last updated: 2026-07-23_

To help manage risk, we allow overnight holdings based on your account size. You can hold position sizes up to the following maximum limits overnight:

**$100k:** 2 mini  **or** 20 micros
**$150k:** 3 mini **or** 30 micros

### Summer Boost Rewards (Swing Accounts Only)

<https://the5ers.com/frequently_questions/summer-boost-rewards/>  
_Last updated: 2026-07-23_

### **What is the Summer Boost Rewards ladder?**

The Summer Boost is an exclusive, limited-time promotional reward structure built specifically for Swing account traders during the campaign. As you hit key milestones from evaluation to multiple payouts, you unlock a cascading ladder of extra rewards.

### **How exactly do the reward tiers work?**

Rewards accumulate dynamically as you progress through the funded lifecycle of your account:

| Milestone | Reward |
| --- | --- |
| Funded Stage | $15 Hub Credits |
| 1st Payout | $20 Hub Credits |
| 2nd Payout | $25 Hub Credits |
| 3rd Payout | Full Account Refund + $30 Hub Credits |
| 4th Payout | $35 Hub Credits |

### **Can Day Trading accounts participate in the Summer Boost Rewards?**

No. The Summer Boost promotional reward ladder is running **exclusively** for Swing account traders during the campaign timeline.

### **What can I use my HUB Credits for?**

HUB Credits function as internal currency on our platform. You can accumulate them through your trading achievements and redeem them toward future account purchases or other internal platform features.

### What are the New Swing Account Sizes and Pricing?

<https://the5ers.com/frequently_questions/summer-plan-pricing/>  
_Last updated: 2026-07-23_

We are slashing existing Swing prices and permanently introducing $100K and $150K account sizes to our lineup. The new pricing structure is set up to sit just 10% above our standard Day Trading accounts:

| Account Size | **New Price** | Old Price |
| --- | --- | --- |
| 25K | **$69** | $120 |
| 50K | **$120** | $240 |
| 100K | **$189** | New account |
| 150K | **$219** | New account |

### **Will the new Swing account prices change back after summer?**

No. While launched alongside the summer campaign, the price drops for the 25K and 50K accounts—as well as the brand-new 100K and 150K sizes—are **permanent additions** to the program. They will remain active even after the summer campaign ends.

### What is the Futures Summer Plan?

<https://the5ers.com/frequently_questions/what-do-i-get-with-the-futures-summer-plan-2/>  
_Last updated: 2026-07-23_

The Futures Summer Plan is a campaign designed to give Swing traders an aggressive edge. It introduces permanent price drops on Swing accounts, brings brand-new account sizes to the platform, and features a limited-time promotional reward ladder for traders who hit key performance milestones during the summer.

## Uncategorized

### Can asset specifications change over time?

<https://the5ers.com/frequently_questions/can-asset-specifications-change-over-time/>  
_Last updated: 2026-06-09_

Yes. Trading hours, margin requirements, and other conditions can be updated due to market conditions, regulatory changes, or platform updates. Always refer to the latest specifications on your platform.

### Can I add custom indicators to my account?

<https://the5ers.com/frequently_questions/can-i-add-custom-indicators-to-my-account/>  
_Last updated: 2026-06-09_

Yes, you can add custom indicators to your charts on both MT5 and cTrader.
MT5: Custom indicators must be written in MQL5.
cTrader: Custom indicators must be written in cAlgo/C#. Ensure the indicator file is correctly installed in the respective platform’s indicators folder before applying it to your chart.

### Can I trade multiple evaluation accounts at once?

<https://the5ers.com/frequently_questions/can-i-trade-multiple-evaluation-accounts-at-once/>  
_Last updated: 2026-08-27_

150k accounts (Swing and Day Trade) are limited to 1 account only.
100k accounts (Swing and Day Trade) are limited to 2 accounts only.
25k and 50k accounts can be added freely, up to a 500k maximum allocation across all accounts combined.

### Can I use ads and keywords?

<https://the5ers.com/frequently_questions/can-i-use-ads-and-keywords/>  
_Last updated: 2026-06-09_

Before running any paid ads campaign, you must request written permission from The5ers. Running a paid ad campaign without permission will result in immediate termination of your affiliate account without payment. It is prohibited to use The5ers brand as keywords, and to promote The5ers in connection with websites or platforms containing defamatory, obscene, illegal, or otherwise inappropriate content. If you run a Google Ads campaign, you must include the following phrases in your “negative keywords” list: “the5ers”, “the 5ers”, “the5ers,” “5ers,” “5 percenters,” “the5%ers,” and “5%ers”.

### Can I use multiple discount codes on one purchase?

<https://the5ers.com/frequently_questions/can-i-use-multiple-discount-codes-on-one-purchase/>  
_Last updated: 2026-06-09_

No—only one promo code can be used per order. Choose the one that gives you the best value.

### Commission re-bate explanation:

<https://the5ers.com/frequently_questions/commission-re-bate-explanation/>  
_Last updated: 2026-06-09_

At The5ers Futures, we reward our traders by giving back **100% of their trading commissions**. All commissions paid during the trading day are **refunded automatically at the end of each day**, allowing you to trade more efficiently and keep your costs as low as possible.

### Do I pay monthly fees?

<https://the5ers.com/frequently_questions/monthly-fees/>  
_Last updated: 2026-08-27_

No. The5ers Futures does not charge monthly fees or activation fees after passing the evaluation.

### Do the rules change once I am funded on the 1-Step plan?

<https://the5ers.com/frequently_questions/do-the-rules-change-once-i-am-funded-on-the-1-step-plan/>  
_Last updated: 2026-07-15_

No. To keep things simple and structured, your profit target (10%) and risk rules (6% max loss, 3% daily loss, and 50% consistency) remain the same on your funded account as they were during evaluation.

BONUS: Get 10% in hub credits once funded

### Do The5ers offer coupon codes year-round?

<https://the5ers.com/frequently_questions/do-the5ers-offer-coupon-codes-year-round/>  
_Last updated: 2026-06-09_

Not always. Most of our promotions are seasonal, event-driven, or tied to a specific partner collaboration.

### Does the $200K High Stakes Summer Plan support account scaling?

<https://the5ers.com/frequently_questions/does-the-200k-high-stakes-summer-plan-support-account-scaling/>  
_Last updated: 2026-08-11_

**Scaling is not available** for this program, and the account balance remains fixed at $200,000.

**What are the payout caps:**

* $200K –  **$3,000 per payout cycle**

* **$100K – $2,000 per payout cycle**

### Does the consistency rule apply to the 2-Step Plan?

<https://the5ers.com/frequently_questions/does-the-consistency-rule-apply-to-the-2-step-plan/>  
_Last updated: 2026-07-15_

Yes, but only on the funded account. Once you pass both Phase 1 and Phase 2 and receive your live $100,000 funded account, a 50% consistency requirement will apply to your trading.

### Does this come with market data?

<https://the5ers.com/frequently_questions/market-data/>  
_Last updated: 2026-08-27_

No extra cost. All required market data is included in your program.

### How can I earn Hub Credits on my Swing account?

<https://the5ers.com/frequently_questions/how-can-i-earn-hub-credits-on-my-swing-account/>  
_Last updated: 2026-07-21_

Hub Credits are awarded automatically as traders reach key milestones: $15 at the Funded Stage, $20 at the 1st Payout, $25 at the 2nd Payout, a Full Account Refund plus $30 at the 3rd Payout, and $35 at the 4th Payout. This program is exclusive to Swing accounts and does not apply to Day Trading accounts.

### How can I get paid?

<https://the5ers.com/frequently_questions/how-can-i-get-paid/>  
_Last updated: 2026-06-09_

Once your rewards exceed $150 and you referred at least 3 new users, you can request to withdraw your commission.

### How can the News Sentiment help me make decisions?

<https://the5ers.com/frequently_questions/how-can-the-news-sentiment-help-me-make-decisions/>  
_Last updated: 2026-06-09_

By revealing the overall market mood, News Sentiment can help you anticipate potential reversals, confirm trends, or identify opportunities that may not be obvious from technical charts alone. It provides a broader context for your trading decisions.

### How do I change the chart timeframes?

<https://the5ers.com/frequently_questions/how-do-i-change-the-chart-timeframes/>  
_Last updated: 2026-06-09_

On MT5 and cTrader, you can change the chart timeframe using the toolbar on the platform:
MT5: Right-click on the chart -> “Timeframes” -> select the desired timeframe (e.g., M1, H1, D1).
cTrader: Click the timeframe dropdown at the top of the chart and select your preferred timeframe

### How do I earn commissions?

<https://the5ers.com/frequently_questions/how-do-i-earn-commissions/>  
_Last updated: 2026-06-09_

You will receive a unique link that will grant you a commission of 10% for all programs for first-time purchase (you can split 5% each with your followers upon request).

### How do I get my affiliate link?

<https://the5ers.com/frequently_questions/how-do-i-get-my-affiliate-link/>  
_Last updated: 2026-06-09_

After joining the program, go to the affiliate section in your dashboard and click on ‘Referral Link’. This will create a unique link that you can share.

### How do I pass the 1-Step evaluation?

<https://the5ers.com/frequently_questions/how-do-i-pass-the-1-step-evaluation/>  
_Last updated: 2026-07-24_

You need to hit a 10% profit target on your $100,000 evaluation account while respecting all risk parameters:

* Maximum Loss: 6% of your initial balance.
* Daily Loss Limit: calculated at the end of each trading day based on 3% of your account’s EOD equity OR balance—whichever of the two is higher.
* Consistency Requirement: 50% (no single trading day can account for more than 50% of your total profit).

### How do I receive my evaluation fee refund and Summer Boost credits?

<https://the5ers.com/frequently_questions/how-do-i-receive-my-evaluation-fee-refund-and-summer-boost-credits/>  
_Last updated: 2026-08-11_

Your evaluation fee refund is distributed in three distinct stages throughout your progression:

* **Step 1 Completion:** You receive **10% of your evaluation fee** back as HUB credits as soon as you pass Phase 1.
* **Step 2 Completion (Reaching Funded Stage):** You receive **20% of your evaluation fee** back as HUB credits as soon as you pass Phase 2 and gain funded status.
* **3rd Payout Milestone:** The remaining **70% of your evaluation fee** is paid out directly as **withdrawable cash** alongside your 3rd profit payout.

### How do I remove or reset indicators on my chart?

<https://the5ers.com/frequently_questions/how-do-i-remove-or-reset-indicators-on-my-chart/>  
_Last updated: 2026-06-09_

MT5: Right-click on the chart -> select Indicators List -> choose the indicator you want to remove -> click Delete. To reset all indicators, you can remove them one by one or apply a template without indicators.
cTrader: Click on the indicator’s “x” button in the chart panel, or open the Indicators window, select the indicator, and click Remove. This ensures your chart is cleared and ready for new indicators or templates.

### How do payouts, profit split, and consistency work on the $200K Funded Account?

<https://the5ers.com/frequently_questions/how-do-payouts-profit-split-and-consistency-work-on-the-200k-funded-account/>  
_Last updated: 2026-08-11_

Once you complete both evaluation steps and move to your $200,000 funded account:

* **Profit Share:** You receive an **80/20 profit split** (80% to the trader).
* **Payout Cap & Minimum:** The minimum withdrawal is **$250**, with a payout cap of up to **$3,000 per payout cycle**.
* **Daily Consistency Rule:** A **50% daily consistency requirement** applies, meaning no single trading day can account for more than 50% of your total generated profit at the time of a payout request.

### How is the economic calendar used?

<https://the5ers.com/frequently_questions/how-is-the-economic-calendar-used/>  
_Last updated: 2026-06-09_

By monitoring the calendar, traders can anticipate market movements and adjust their trading strategies accordingly. They analyze the expected impact of each event on currency pairs and may enter or exit positions based on their predictions. Additionally, traders use the calendar to manage risk by avoiding trading during high-impact events or adjusting their position sizes to account for potential volatility. Overall, the economic calendar helps traders make informed decisions and stay ahead of market movements in the forex market.

### How is the News Sentiment score calculated?

<https://the5ers.com/frequently_questions/how-is-the-news-sentiment-score-calculated/>  
_Last updated: 2026-06-09_

The sentiment score is derived from analyzing market news, economic reports, and trader reactions. Advanced algorithms evaluate the language and content of news to determine whether it is likely to have a positive (bullish), negative (bearish), or neutral impact on the market.

### How long can I take advantage of Summer Boost Rewards?

<https://the5ers.com/frequently_questions/how-long-can-i-take-advantage-of-summer-boost-rewards/>  
_Last updated: 2026-07-21_

It’s a limited-time offer available only through the end of summer. It applies exclusively to Swing accounts and does not extend to Day Trading accounts.

### How many competitions can I register for?

<https://the5ers.com/frequently_questions/what-are-the-top-5-winners/>  
_Last updated: 2026-06-09_

Traders can register to 1 contest simultaneously.

### How many times can I use this coupon?

<https://the5ers.com/frequently_questions/how-many-times-can-i-use-this-coupon/>  
_Last updated: 2026-06-09_

Each trader can take advantage of this coupon one time.

### How much is the profit split in The5ers?

<https://the5ers.com/frequently_questions/how-much-is-the-profit-split-in-the5ers/>  
_Last updated: 2026-06-14_

For the Bootcamp and Hyper-Growth programs, traders start with a 50% profit split, but they can quickly grow that to 75% already by the next stage in the scale-up plan.

*For the full breakdown of the scaling plans on Hyper Growth click here <https://the5ers.com/hyper-growth/> (choose HyperGrowth)*

*![](https://wp.the5ers.com/wp-content/uploads/2026/06/split.png)*

Traders can scale up the profit split to **100%**, meaning you’ll take home 100% of the profits you earn!

---

*For the full breakdown of the scaling plans on Bootcamp click here <https://the5ers.com/bootcamp/>*

![](https://wp.the5ers.com/wp-content/uploads/2026/06/splitb.png)

In order to scale in the Bootcamp program, traders need to reach the 5% target

---

In the High Stakes program, traders start with an 80% profit split and can also scale that up to **100%**.

In order to scale in the High Stakes program, traders need to reach the 10% target and have 3 profitable days.*

*For the full breakdown of the scaling plans click here <https://the5ers.com/high-stakes/> and scroll to the bottom of the page*

![](https://wp.the5ers.com/wp-content/uploads/2026/06/splitc.png)

---

ProGrowth program, traders start with a 75% profit split and can also scale up to 100%

In order to scale in the Pro Growth program, traders need to reach the 10% target

*For the full breakdown of the scaling plans on ProGrowth click here <https://the5ers.com/hyper-growth/> (choose ProGrowth)*

![](https://cdn.livechat-files.com/api/file/kb/file/14119155/fa5b8e17cb-31b6679cb162675b32a9.png)

*A profitable day is a day on which the closed positions made a positive profit of at least 0.5% of the initial balance.
The positive profit is calculated as follows: Minimum(Midnight Balance, Midnight Equity) – Previous Day Balance

### How often is the sentiment data updated?

<https://the5ers.com/frequently_questions/how-often-is-the-sentiment-data-updated/>  
_Last updated: 2026-06-09_

Sentiment data is updated in real-time or at frequent intervals as new news and market information become available, ensuring that you have the most current view of market psychology.

### How should I combine News Sentiment with my existing technical analysis?

<https://the5ers.com/frequently_questions/how-should-i-combine-news-sentiment-with-my-existing-technical-analysis/>  
_Last updated: 2026-06-09_

Use News Sentiment as a complementary tool. For example, if your technical analysis signals a potential trend reversal and News Sentiment shows a shift in market mood, this can strengthen your confidence in the trade. Conversely, if sentiment contradicts your technical signals, you might reconsider or adjust your strategy.

### How to read the calendar?

<https://the5ers.com/frequently_questions/how-to-read-the-calendar/>  
_Last updated: 2026-06-09_

Select the day you want to see the news for. Be specially aware of the high-impact news as they tend to bring volatility to related currencies. During these events, slippage is expected to happen so make sure to adjust risk accordingly.

### How to use the calendar while trading?

<https://the5ers.com/frequently_questions/how-to-use-the-calendar-while-trading/>  
_Last updated: 2026-06-09_

Trading with an economic calendar involves using the information provided to anticipate market movements and adjust your trading strategy accordingly.

### Is copy trading allowed between my accounts?

<https://the5ers.com/frequently_questions/is-copy-trading-allowed-between-my-accounts/>  
_Last updated: 2026-08-11_

**Yes.** Copy trading between your own Summer Plan accounts is fully allowed.

### Is there a limit to the number of indicators I can use on MT5 or cTrader?

<https://the5ers.com/frequently_questions/is-there-a-limit-to-the-number-of-indicators-i-can-use-on-mt5-or-ctrader/>  
_Last updated: 2026-06-09_

There is no fixed limit on the number of indicators you can add to MT5 or cTrader. However, adding too many indicators, especially complex or custom ones, may affect platform performance. For optimal performance, we recommend using only the indicators necessary for your analysis.

### My chart froze and is not updating- what should I do?

<https://the5ers.com/frequently_questions/my-chart-froze-and-is-not-updating-what-should-i-do/>  
_Last updated: 2026-06-09_

Chart freezing is usually caused by connection issues. To fix this:

1. Check that your internet connection is stable.
2. Make sure you are connected to the correct server:
   * Paid Evaluation / Funded Accounts: FivePercentOnline-Real
   * Contest Accounts: FivePercentOnline-Experience
3. Look at the signal bars in the bottom-right corner of your MT5 or cTrader platform. Red bars indicate a connection problem or that you’re not connected to the server.

Following these steps usually restores normal chart updates. If the issue continues, please reach out to our support team for further assistance.

### Scaling Plan Explained

<https://the5ers.com/frequently_questions/scaling-plan-explained/>  
_Last updated: 2026-08-10_

Say you’re trading a $50K account. Hit $5,000 in profit (that’s your 10% target) and you scale up: your balance jumps to $52,500 (a 5% boost), on top of whatever profit share you’ve earned from the 80/20 split. Your max contract size grows too, adding 1 mini and 10 micros for a new total of 5 minis and 50 micros.

**Note:** For more information on scaling plans, check each program page for specific details.

### Terms and conditions

<https://the5ers.com/frequently_questions/terms-and-conditions/>  
_Last updated: 2026-06-09_

Supplementing Agreements
These Terms supplement the Company’s Terms of Use (which can be found at [https://the5ers.com/terms-and-conditions](/terms-and-conditions/)) (the “Terms”) and Privacy Policy (a current copy which can be found at <https://the5ers.com/privacy-policy/>) in effect from time to time, each of which remain in full force and effect, and apply to the AFFILIATE and govern the AFFILIATE’s access to and the use of the Website, the Hub or Services. All capitalized terms not otherwise defined herein shall have the meanings set forth in the Terms. Please also refer to the information provided in the FAQ to dully understand the program.

### What are asset specifications?

<https://the5ers.com/frequently_questions/what-are-asset-specifications/>  
_Last updated: 2026-06-09_

Asset specifications provide key details about each trading instrument, including trading hours, margin requirements, contract size, and any special conditions. They help you understand the rules and requirements before placing a trade.

### What are my Responsibilities as an Affiliate

<https://the5ers.com/frequently_questions/what-are-my-responsibilities-as-an-affiliate/>  
_Last updated: 2026-06-09_

As an Affiliate, will promote The5ers’ by using authorized marketing materials and accurate testimonies of your experience as a user. All marketing activities must be ethical and legal. As an Affiliate you are required to comply with all applicable laws and regulations related to your marketing activities, and to refrain from any misleading marketing activities, fraudulent activities, or spamming practices.

### What are the new $200K High Stakes Summer Plan options?

<https://the5ers.com/frequently_questions/what-are-the-new-200k-high-stakes-summer-plan-options/>  
_Last updated: 2026-08-11_

The $200K High Stakes Summer Plan offers two discounted 2-step evaluation paths to secure a $200,000 funded account:

* **200K (10/5 Plan) – $249:** Pass Step 1 with a **10% target** and Step 2 with a **5% target**.
* **200K (8/5 Plan) – $279:** Pass Step 1 with a lower **8% target** and Step 2 with a **5% target**.

Both options feature unlimited trading days, 1:100 leverage, a 10% maximum overall loss limit, and a 3% daily loss limit.

### What are the payout limits for the 1-Step funded account?

<https://the5ers.com/frequently_questions/what-are-the-payout-limits-for-the-1-step-funded-account/>  
_Last updated: 2026-08-10_

To request a payout, you must have a minimum PnL of $150 in profit. The maximum amount you can withdraw is capped at $2,000 per payout cycle.

First withdrawal: Available 14 days after your funded account is activated.
Subsequent withdrawals: Every 2 weeks after your last approved withdrawal.
Scaling: If your account is scaled, the 14-day waiting period resets from the scaling date.

### What are the prizes?

<https://the5ers.com/frequently_questions/how-many-competitions-can-i-register-for/>  
_Last updated: 2026-06-09_

* 1st place: 60K High Stakes
* 2nd place: 20K High Stakes
* 3rd place: 10K High Stakes
* 4th place: 5K High Stakes
* 5th place: 5K High Stakes
* 6th place: 5K High Stakes
* 7th place: 5K High Stakes
* 8th place: 5K High Stakes
* 9th place: 5K High Stakes
* 10th place: 5K High Stakes
* 90 subsequent winners: 11-20th Places: 20K Bootcamp | 21-80th Places: $5 HUB CREDITS | 81-100th Places: $5 TTP HUB CREDITS

### What are the rewards and payout limits for the 2-Step plan?

<https://the5ers.com/frequently_questions/what-are-the-rewards-and-payout-limits-for-the-2-step-plan/>  
_Last updated: 2026-08-23_

* Milestone Bonuses: Completing Step 1 and Step 2 each unlocks HUB credits that you can use for future internal purchases.
* Payout Limits: You need a minimum PnL of $250 in profit to request a withdrawal.
* Payout Cap: $100K plan- Up to $2,000 per payout cycle. $200K plan- Up to $3000 per payout cycle.

### What are the risk parameters for the 2-Step Plan evaluation?ˇ

<https://the5ers.com/frequently_questions/what-are-the-risk-parameters-for-the-2-step-plan-evaluation%cb%87/>  
_Last updated: 2026-07-15_

Both the New and Classic versions share the same evaluation risk model:

* Maximum Loss: 10% of your initial balance.
* Daily Loss Limit: Calculated at the end of each trading day based on 3% of your account’s EOD equity OR balance—whichever of the two is higher.
* *Note: There is no consistency rule during the evaluation phases for the 2-Step plan.*

### What are the rules?

<https://the5ers.com/frequently_questions/what-are-the-rules/>  
_Last updated: 2026-06-09_

* Only one position can be open at any given moment
* Daily Loss: 5%
* Maximum Loss: 10%
* Leverage: 1:30
* EA’s are NOT allowed
* Account Balance: $10,000
* News trading is allowed
* Prizes will be awarded the day after the contest ends

### What are the weekend rules for my Swing account?

<https://the5ers.com/frequently_questions/what-are-the-weekend-rules-for-my-swing-account/>  
_Last updated: 2026-07-21_

Weekend holding is not permitted on Swing accounts. All positions must be closed by 4:50 PM ET before the weekend. Failure to comply will result in account termination.

### What do I get with the Futures Summer Plan?

<https://the5ers.com/frequently_questions/what-do-i-get-with-the-futures-summer-plan/>  
_Last updated: 2026-07-21_

It’s a limited-time offer for Swing accounts, running through the end of summer. It includes reduced pricing across account sizes, two new account tiers (100K and 150K), and the Summer Boost Rewards program, which rewards Hub Credits at key milestones.

### What do the sentiment labels mean — negative, neutral, or positive?

<https://the5ers.com/frequently_questions/what-do-the-sentiment-labels-mean-negative-neutral-or-positive/>  
_Last updated: 2026-06-09_

* **Negative**: Market mood is bearish; traders are generally expecting prices to fall.
* **Neutral**: Market sentiment is balanced; there is no strong bias toward buying or selling.
* **Positive**: Market mood is bullish; traders are generally expecting prices to rise.

### What happens after I pass the 1-Step evaluation?

<https://the5ers.com/frequently_questions/what-happens-after-i-pass-the-1-step-evaluation/>  
_Last updated: 2026-07-15_

You move directly to a $100,000 funded account. Plus, as a passing bonus, you will receive 10% of your evaluation fee as hub credit.

### What happens to my account after the summer plan ends?

<https://the5ers.com/frequently_questions/what-happens-to-my-account-after-the-summer-plan-ends/>  
_Last updated: 2026-07-21_

Nothing changes. Any account purchased during the Summer Plan keeps running exactly as normal after the promotion ends, with no impact on your rules, targets, or progress.

### What is a forex economic calendar?

<https://the5ers.com/frequently_questions/what-is-a-forex-economic-calendar/>  
_Last updated: 2026-06-09_

A forex economic calendar is a tool used by traders to track important economic events and indicators that may impact currency prices. It includes dates, times, and details of events like interest rate decisions, employment reports, and GDP releases, helping traders make informed trading decisions based on potential market impact.

### What is the difference between the One-Step and Two-Step Summer Plans?

<https://the5ers.com/frequently_questions/what-is-the-difference-between-the-one-step-and-two-step-summer-plans/>  
_Last updated: 2026-07-15_

The 2-Step plan offers two entry tiers for the $100,000 account to fit your budget and strategy:

* Summer 10/5 ($149): Phase 1 profit target is 10%; Phase 2 is 5%.
* Summer 8/5 ($179): Phase 1 profit target is 8%; Phase 2 is 5%.

**REFUND POLICY**

TWO-Step: Receive 10% hub credits upon passing Step One.

Receive 20% hub credits upon passing Step Two.

Withdraw 70% with your third payout

### What is the hyper growth program?

<https://the5ers.com/frequently_questions/what-is-the-hyper-growth-program/>  
_Last updated: 2026-06-09_

This is our 1-step program, where you can get paid from the very first objective.

See more details [here](https://the5ers.com/hyper-growth/).

### What is the maximum allocation for the Summer Plan?

<https://the5ers.com/frequently_questions/what-are-the-maximum-allocation-and-account-limits-for-the-summer-plan/>  
_Last updated: 2026-08-11_

* **Maximum Buying Power Cap:** The total aggregate buying power allowed across all Summer Plan accounts is **$600,000 per trader**.
* **$200K Account Options:** Each trader is permitted to purchase **one $200K (10/5 Plan)** and **one $200K (8/5 Plan)** account simultaneously.
* **Combining Account Sizes:** Since holding two $200K accounts equals $400K in total capital, you still have $200K in remaining allocation under the $600K cap. This means you can also hold additional $100K accounts (e.g., up to two $100K accounts) alongside your $200K accounts.

### What is the News Sentiment?

<https://the5ers.com/frequently_questions/what-is-the-news-sentiment/>  
_Last updated: 2026-06-09_

News Sentiment is an analysis of market psychology based on recent news and events. It shows the general mood of the market- whether traders are leaning bullish, bearish, or neutral- helping you understand how news may influence price movements.

### What Materials Can I use?

<https://the5ers.com/frequently_questions/what-materials-can-i-use/>  
_Last updated: 2026-06-09_

You can use promotional materials we share with our Affiliates and our users materials solely for promoting The5ers services in accordance with this Affiliate Program Terms. You may not alter, modify, or create derivative works from the materials we share or any other The5ers intellectual property without prior written consent from the Company. The5ers reserves the right to revoke this license at any time. This license terminates once you terminate your affiliation with us.

### What time frames are available for viewing?

<https://the5ers.com/frequently_questions/what-time-frames-are-available-for-viewing/>  
_Last updated: 2026-06-09_

You can view charts in the following time frames:
**Minutes**: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30
**Hours**: 1, 2, 3, 4, 6, 8, 12
**Longer periods**: Daily, Weekly, Monthly

### What types of charts are available?

<https://the5ers.com/frequently_questions/what-types-of-charts-are-available/>  
_Last updated: 2026-06-09_

Bar, Candlestick, and Line charts.

### When do the competitions start and end?

<https://the5ers.com/frequently_questions/when-do-the-competitions-start-and-end-3/>  
_Last updated: 2026-06-09_

A new contest starts each Wednesday at 10:00 am server time and ends the following Tuesday.

### When do the competitions start and end?

<https://the5ers.com/frequently_questions/when-do-the-competitions-start-and-end-2/>  
_Last updated: 2026-06-09_

**Lorem Ipsum** is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry’s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

### When do the competitions start and end?

<https://the5ers.com/frequently_questions/when-do-the-competitions-start-and-end/>  
_Last updated: 2026-06-09_

**Lorem Ipsum** is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry’s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

### Where can I access updated asset specifications?

<https://the5ers.com/frequently_questions/where-can-i-access-updated-asset-specifications/>  
_Last updated: 2026-06-09_

You can find the most up-to-date specifications directly on your trading platform. Right-click on your symbol, then select ‘Specification’. Always check this before trading, as conditions can change.

### Where can I find active promotions?

<https://the5ers.com/frequently_questions/where-can-i-find-active-promotions/>  
_Last updated: 2026-06-09_

Right here on this page

### Where can I share my affiliate link?

<https://the5ers.com/frequently_questions/where-can-i-share-my-affiliate-link/>  
_Last updated: 2026-06-09_

You can share your link on social media, where you can reach potential users.

### Which indicators are available by default on MT5 and cTrader?

<https://the5ers.com/frequently_questions/which-indicators-are-available-by-default-on-mt5-and-ctrader/>  
_Last updated: 2026-06-09_

MT5: MT5 comes with a wide range of built-in indicators, including Moving Averages, RSI, MACD, Bollinger Bands, Stochastic Oscillator, Average True Range (ATR), and many more. These can be accessed via Insert -> Indicators on the platform.

cTrader: cTrader also offers a variety of default indicators, such as Moving Averages, RSI, MACD, Bollinger Bands, Stochastic Oscillator, and others. You can access them by clicking the Indicators button on the top toolbar of the chart. These default indicators are fully integrated and optimized for performance on each platform

### Who Can I Contact For Help?

<https://the5ers.com/frequently_questions/who-can-i-contact-for-help/>  
_Last updated: 2026-08-05_

If you have any questions or need assistance, our support team is here to help. You can reach us through the contact form on our site or directly via email at help@the5ers.com.

### Who can sign up to The5ers’ affiliate program?

<https://the5ers.com/frequently_questions/who-can-sign-up-to-the5ers-affiliate-program/>  
_Last updated: 2026-06-09_

Any active user can sign up The5ers’ affiliate program once using a single referral link.

### Why do trading hours differ between assets?

<https://the5ers.com/frequently_questions/why-do-trading-hours-differ-between-assets/>  
_Last updated: 2026-06-09_

Each market operates in its own time zone and may have different opening and closing hours. Knowing the trading hours ensures you can plan your trades when the market is active and liquid.

### Why does my chart look different from other broker platforms on TradingView?

<https://the5ers.com/frequently_questions/why-does-my-chart-look-different-from-other-broker-platforms-on-tradingview/>  
_Last updated: 2026-06-09_

Our chart data comes directly from our liquidity providers, while TradingView uses feeds from their own partner brokers, which may rely on different liquidity sources. This can cause slight variations in candle formation, price levels, or spreads. For the most accurate trade execution, please use our feed on MT5 or cTrader.

### Why does my chart show a different time zone?

<https://the5ers.com/frequently_questions/why-does-my-chart-show-a-different-time-zone/>  
_Last updated: 2026-06-09_

Charts on MT5 and cTrader operate according to the server time, which is GMT+2 during standard time and GMT+3 during daylight saving time. This ensures consistency across all trading activity. For accurate trade execution and analysis, we recommend referencing the server time on MT5 or cTrader.
