---
tags: [polymarket, strategies]
---

# Strategy Findings

Track what works and what doesn't across strategy families.

## forecast_arbitrage
- Status: Active
- Key insight: Use forecast-based std (~0.4°C/day), not historical std
- Madrid Apr 17 test: BUY NO 27°C @ 49.5%, model says 18.1% — pending result
- **Apr 18 finding:** Markets consistently overprice the exact forecast temperature bin. "BUY NOT X°C" where X is near forecast mean is consistently profitable (+10-24% edge). The forecast distribution is spread ±2°C but market piles on one bin.
- Seoul Apr 19: massive +43.9% edge on BUY YES ≥24°C @ 48% (model 91.4%). Tail bucket market for "or higher" was mispriced.

## seasonal_prior
- Status: Active
- Notes: Historical distribution as baseline or blend

## extreme_prices
- Status: Active
- Notes: Bet against <5% / >95% bins — add min price floor (skip <2% / >98%)

## tail_hunter
- Status: Active
- Notes: Focus on underpriced tail bins

---

