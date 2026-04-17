---
tags: [polymarket, strategies]
---

# Strategy Findings

Track what works and what doesn't across strategy families.

## forecast_arbitrage
- Status: Active
- Key insight: Use forecast-based std (~0.4°C/day), not historical std
- Madrid Apr 17 test: BUY NO 27°C @ 49.5%, model says 18.1% — pending result

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

