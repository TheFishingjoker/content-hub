---
title: "Polymarket Paper Trader"
type: entity
category: tool
source: "https://github.com/agent-next/polymarket-paper-trader"
first_seen: 2026-04-17
tags: [polymarket, ai-agents, paper-trading, mcp, finance]
related: [polymarket-terminal]
---

# Polymarket Paper Trader

AI agent paper trading simulator for Polymarket. 26 MCP tools for autonomous trading. Realistic simulation: orderbook execution, exact fee model, slippage, limit orders. CLI + MCP server. Python, SQLite, PyPI.

**Key facts:**
- 252 stars, MIT, Python 3.10+
- 26 MCP tools for AI agent trading
- Level-by-level orderbook execution simulation
- Exact Polymarket fee model: bps/10000 × min(price, 1-price) × shares
- GTC/GTD limit orders, multi-outcome markets
- Multi-account A/B testing, public leaderboard
- 3 example strategies: momentum, mean reversion, limit grid
- CLI: pm-trader (init, browse, buy/sell, portfolio, backtest)
- MCP server: pm-trader-mcp (stdio transport)

**Where saved:**
- GitHub: direct link (2026-04-17)
- Content Hub: content/Finance/polymarket-paper-trader.md
