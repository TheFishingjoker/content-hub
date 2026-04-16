---
title: "Experiment: Forecast Arbitrage"
type: experiment
status: active
started: 2026-04-16
tags:
  - polymarket
  - experiment
  - weather
---

# Forecast Arbitrage

**Hypothesis:** Weather forecast models with known uncertainty distributions are better at pricing temperature probabilities than Polymarket crowds.

**Mechanism:** The crowd sees "forecast says 26°C" → piles into the favorite bins → undertails everything else. A normal distribution model around the forecast with appropriate std captures the tails better.

## Model Parameters

| Parameter | Value | Rationale |
| --- | --- | --- |
| Forecast source | Open-Meteo API | Free, no key, reliable for Europe |
| Distribution | Normal (Gaussian) | Standard for temperature uncertainty |
| Base std | 1.5°C | 1-day forecast typical error |
| Std scaling | +0.4°C per day out | Forecast error grows with horizon |
| Max std | 5.0°C | Cap for 7+ day forecasts |
| Edge threshold | 3% | Minimum model-market difference |
| EV threshold | 2% | Minimum positive expected value |

## What We're Testing

- **Calibration:** Outcomes the model prices at X% should win ~X% of the time
- **Edge:** Does the crowd systematically underprice tails and overprice favorites?
- **Forecast quality:** Is Open-Meteo accurate enough to beat the market?

## Invalidation Criteria

- Open-Meteo forecasts are systematically off for specific cities
- Normal distribution doesn't fit temperature outcomes (skew, bimodal)
- Crowd has access to better forecast data than Open-Meteo
- Std model (1.5 + 0.4/day) doesn't match actual forecast error

## Results

| Market | Date | Trade | Entry | Outcome | P&L |
| --- | --- | --- | --- | --- | --- |
| [Madrid Apr 17](../trades/madrid-apr17.md) | 2026-04-16 | BUY NO 27°C | 49.5% | Pending | — |

*Results table updated after each resolution.*
