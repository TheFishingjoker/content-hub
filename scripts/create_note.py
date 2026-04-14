#!/usr/bin/env python3
"""Create a tagged note in the Quartz content folder."""

import argparse
from datetime import datetime
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "content"


def slugify(text: str) -> str:
    return (
        text.lower()
        .strip()
        .replace(" ", "-")
        .replace("/", "-")
        .replace("\\", "-")
    )[:80]


def create_note(
    title: str,
    url: str,
    platform: str,
    tags: list[str],
    summary: str,
    notes: str = "",
    inbox: bool = True,
) -> Path:
    tags_yaml = "\n".join(f"  - {t}" for t in tags)
    target_dir = CONTENT_DIR / ("inbox" if inbox else "archive")

    content = f"""---
title: "{title}"
source: "{url}"
platform: {platform}
saved: {datetime.now().strftime("%Y-%m-%d")}
tags:
{tags_yaml}
---

{summary}

{f"## Notes\n\n{notes}" if notes else ""}
"""

    filename = f"{datetime.now().strftime('%Y%m%d')}-{slugify(title)}.md"
    filepath = target_dir / filename

    filepath.write_text(content)
    return filepath


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a vault note")
    parser.add_argument("--title", required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--platform", required=True)
    parser.add_argument("--tags", required=True, help="Comma-separated tags")
    parser.add_argument("--summary", required=True)
    parser.add_argument("--notes", default="")
    parser.add_argument("--archive", action="store_true", help="Skip inbox")

    args = parser.parse_args()
    tags = [t.strip() for t in args.tags.split(",")]

    path = create_note(
        title=args.title,
        url=args.url,
        platform=args.platform,
        tags=tags,
        summary=args.summary,
        notes=args.notes,
        inbox=not args.archive,
    )
    print(f"Created: {path}")
