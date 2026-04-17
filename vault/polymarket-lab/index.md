---
tags: [polymarket, prediction-markets]
---

# Polymarket Lab

Paper trading research system. Daily automated scans run at 9AM CET.

## Structure

- [[log]] — Daily research log (prepend newest entries)
- [[strategies]] — Strategy findings, what works, what doesn't
- [[cities]] — City-specific notes and quirks
- [[trades/]] — Per-market trade notes

## Key Decisions

- Always buy tomorrow's market (on 17th → target 18th)
- Skip closed/expired markets
- Filter by resolution date, not just availability

## Quick Links

- VPS lab: /opt/data/polymarket-lab/
- Cron job: 1437bef8aea5 (9AM CET daily)
