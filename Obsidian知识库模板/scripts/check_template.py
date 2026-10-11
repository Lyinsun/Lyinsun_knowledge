#!/usr/bin/env python3
"""Read-only structural and privacy checks for this template."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED = (
    "00-Inbox",
    "01-Projects",
    "02-Areas",
    "03-Resources",
    "04-Archives",
    "05-Knowledge/Concepts",
    "05-Knowledge/How-Tos",
    "05-Knowledge/Decisions",
    "05-Knowledge/Insights",
    "06-QA-Log",
    "99-Templates",
    "Index",
    ".agents/skills",
)
REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "Index/Home.md",
    "Index/MOC-Knowledge.md",
    "Index/MOC-QA.md",
    "99-Templates/知识卡片模板.md",
    "99-Templates/问答记录模板.md",
    "01-Projects/示例-知识库整理.md",
    "05-Knowledge/How-Tos/示例-从收件箱到知识卡.md",
    "06-QA-Log/QA-示例-整理一次输入.md",
)
FORBIDDEN = ("/Users/", "/data00/home/", "git@", "ou_")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []

    for relative in REQUIRED:
        if not (root / relative).is_dir():
            errors.append(f"missing directory: {relative}")
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing file: {relative}")

    for path in root.rglob("*.md"):
        relative = path.relative_to(root)
        if any(part in {".git", ".obsidian", ".agents"} for part in relative.parts):
            continue
        text = path.read_text(encoding="utf-8")
        for marker in FORBIDDEN:
            if marker in text:
                errors.append(f"possible private identifier {marker!r}: {path.relative_to(root)}")
        if path.name not in {"README.md", "AGENTS.md"} and not text.startswith("---\n"):
            errors.append(f"missing frontmatter: {relative}")

    if errors:
        print("FAILED")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("PASS: template structure, examples, frontmatter, and basic privacy scan")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
