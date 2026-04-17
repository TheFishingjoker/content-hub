---
tags: [moc, polymarket]
---

# Polymarket Tools — Map of Content

Trading terminals, bots, paper traders, and research for Polymarket prediction markets.

## Active Research
- Polymarket Lab (VPS) — /opt/data/polymarket-lab/ — weather temperature market strategies
- PolyLayer (Coolify) — backtesting platform with experiments 012-14 (night floor NO strategies)

## Open-Source Tools
- [[polymarket-terminal]] — Copy trader, market-making MM, orderbook sniper (Node.js, 230 stars)
- [[polymarket-paper-trader]] — AI agent paper trading simulator, 26 MCP tools (Python, 252 stars)

## Data Sources
- Polymarket Gamma API — market metadata
- Polymarket CLOB API — prices, orderbooks
- Polymarket Data API — trades (free)
- MarketLens — tick-level L2 data (crypto only, free tier: 10 req/min)

## Key Insight
Temperature markets are independent binary contracts per °C bin. Use forecast-based std (~0.4°C/day), not historical std. Always buy tomorrow's market.
