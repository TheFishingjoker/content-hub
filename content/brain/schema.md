---
title: "Brain — Schema"
type: schema
---

# Schema

How the brain is structured and maintained.

## Directory Layout

```
content/brain/
├── index.md        # Categorized overview of all entities
├── log.md          # Append-only activity log
├── schema.md       # This file — conventions and rules
└── entities/       # One page per entity
    └── *.md
```

## Entity Page Rules

### Frontmatter (required fields)
- title: Human-readable name (e.g. "Twenty — Open Source CRM")
- type: entity
- category: software | resource | article | video | tool | person | company
- source: Canonical URL (GitHub repo, official site)
- first_seen: YYYY-MM-DD
- tags: Fixed vocabulary, 2-4 per entity
- related: Wikilinks to related entity slugs

### Body structure
1. # Title (repeat frontmatter title)
2. One-paragraph summary of what it is
3. **Key facts:** bullet list (stars, license, tech stack, features)
4. **Where saved:** platform, context, date, link to content hub note

## Tag Vocabulary

Fixed set. Lowercase, hyphenated. New tags require justification.

ai, ai-agents, open-source, devtools, design, business, finance, productivity, knowledge-management, api, crm, music, video, recipe, developer-tools, multi-agent

## Log Format

```
## [YYYY-MM-DD] action | description
- source: platform (@handle or "direct")
- entity: slug
- tags: tag1, tag2
```

Actions: ingest, update, lint, query, setup

## Index Format

Tables grouped by category. Columns: Entity | What | Source | Saved.
Tag section at bottom mapping tags to entity wikilinks.

## Maintenance Rules

- On ingest: create entity page, append to log, update index
- On query with synthesis: consider filing result as a new page
- On lint (future): check for orphans, stale entries, missing links
- Never delete entries — mark superseded if outdated
