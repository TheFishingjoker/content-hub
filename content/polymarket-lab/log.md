---
title: "Polymarket Lab — Daily Log"
type: log
tags:
  - polymarket
  - log
---

# Research Log

## 2026-04-16 — First Run

**Markets scanned:** Madrid temperature Apr 17
**Trades logged:** 1
**Signals found:** 7 (3 BUY YES, 4 BUY NO)

### Key Finding

The crowd is massively overpricing 27°C — 50.5% market vs 18.1% model. This is the classic "favorite pile-on" where forecast followers all converge on 26-27°C without accounting for forecast spread.

The tails (23-25°C) are severely underpriced. Model says 12-18% for 24-25°C, market says <4%.

**Paper trade:** BUY NO 27°C @ 49.5%, EV +$0.32

### Model Notes

Using forecast-based std (1.9°C for 1 day out) instead of historical std (4.3°C). Historical std is too wide — it captures year-to-year climate variation, not forecast uncertainty. The market correctly ignores historical outliers (15°C in some years) and prices based on the forecast.

---
