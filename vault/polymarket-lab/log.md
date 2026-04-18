---
tags: [polymarket, daily-log]
---

# Polymarket Lab — Daily Log

Newest entries go on top.

---

## [2026-04-18] Daily Scan — Apr 19 Markets (5 cities, 5 trades)

**Markets found:** Madrid, Seoul, London, Paris, Tokyo (all targeting Apr 19 resolution)

**Trades made (all forecast_arbitrage, buying tomorrow):**
1. **Madrid — BUY NO NOT 28°C @ 61% × $10** (EV: $0.204) — Forecast 27.1°C, market overpricing 28°C at 39%. Model says only 18.6% chance.
2. **Seoul — BUY YES 24°C or higher @ 48% × $9** (EV: $0.439) — Huge edge. Forecast 26.1°C, model says 91.4% for ≥24°C, market only 47.5%.
3. **London — BUY NO NOT 15°C @ 57% × $8** (EV: $0.217) — Forecast 15.0°C, spread ±1.9°C. Market pricing 42.5% for exactly 15°C but forecast is right at boundary. Model says 79.2% NOT 15°C.
4. **Paris — BUY NO NOT 17°C @ 63% × $7** (EV: $0.180) — Forecast 17.8°C, market pricing 37% for 17°C. Model says 81.0% NOT 17°C.
5. **Tokyo — BUY NO NOT 24°C @ 60% × $7** (EV: $0.234) — Forecast 22.8°C, market pricing 40.5% for 24°C. Model says 82.9% NOT 24°C.

**Total open positions:** 20 | **Total EV:** $10.82 | **Resolved:** 0

**Observations:**
- Seoul has the biggest edge (+43.9%) — forecast strongly disagrees with market pricing the tail.
- Markets consistently overprice the exact forecast temperature bin (London 15°C at 42.5%, Paris 17°C at 37%, Tokyo 24°C at 40.5%). The "NOT exact" bet is consistently profitable because the forecast distribution is spread across ±2°C.
- Madrid pattern continues: market clusters around 27-29°C, model distribution more spread. BUY NO NOT 28°C is the best Madrid trade.

---

## [2026-04-17] Polymarket data sources research
- MarketLens API: tick-level L2 data but crypto series ONLY (no weather/content/politics markets)
- Free Polymarket APIs: sparse price history, no historical orderbook depth
- On-chain scraping is viable fallback for non-crypto markets
- Skill created: polymarket-data-sources (research category)
- PolyLayer (TheFishingjoker/PolyLayer) — full weatherbot on Coolify, experiments 012-014 active
- User considering extracting backtesting into standalone generic suite
