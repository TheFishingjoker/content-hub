---
title: "Polymarket Research Lab"
type: index
tags:
  - polymarket
  - trading
  - experiments
---

# Polymarket Research Lab

Paper trading experiments on Polymarket prediction markets.

## Active Strategies

| Strategy | Status | Trades | Hit Rate | P&L |
| --- | --- | --- | --- | --- |
| [Forecast Arbitrage](experiments/forecast-arbitrage.md) | Active | — | — | — |
| Extreme Prices | Planned | — | — | — |

## How It Works

1. **Scan** — Discover markets via Polymarket API
2. **Research** — Pull external signals (weather forecasts, historical data)
3. **Model** — Build probability distribution, compare to market prices
4. **Trade** — Paper trade when model finds edge > 3% with positive EV
5. **Resolve** — Check actual outcomes, calculate P&L
6. **Learn** — Track calibration curve (model % vs actual hit rate)

## KPI

**EV per trade** — cumulative expected value vs realized P&L.
If the model is well-calibrated, these should converge over time.

## Data

- Paper trade ledger: `/opt/data/polymarket-lab/data/ledger.jsonl`
- Market data: Polymarket public APIs (free, no key)
- Weather signals: Open-Meteo API (free, no key)

## Research Log

See [[polymarket-lab/log|Daily Log]] for run-by-run findings.
