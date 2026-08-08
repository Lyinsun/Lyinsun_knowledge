#!/usr/bin/env python3
"""Read-only validation for the portable engineering knowledge-base template."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


CANONICAL_DIRECTORIES = (
    "architecture",
    "services",
    "modules",
    "concepts",
    "interfaces",
    "workflows",
    "operations",
    "decisions",
)
SOURCE_DIRECTORY = "sources"
REQUIRED_FIELDS = ("id", "title", "status", "owner", "last_reviewed", "sources")
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


@dataclass(frozen=True)
class Finding:
    level: str
    path: Path
    message: str


def read_frontmatter(path: Path) -> set[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return set()
    fields: set[str] = set()
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):", line)
        if match:
            fields.add(match.group(1))
    return set()


def is_content_note(root: Path, path: Path) -> bool:
    relative = path.relative_to(root)
    return relative.parts[0] in CANONICAL_DIRECTORIES and path.name != "README.md"


def canonical_notes(root: Path) -> dict[Path, str]:
    notes: dict[Path, str] = {}
    for directory in CANONICAL_DIRECTORIES:
        for path in (root / directory).glob("*.md"):
            if path.name != "README.md":
                notes[path.resolve()] = path.read_text(encoding="utf-8")
    return notes


def source_records(root: Path) -> dict[Path, str]:
    records: dict[Path, str] = {}
    for path in (root / SOURCE_DIRECTORY).glob("*.md"):
        if path.name != "README.md":
            records[path.resolve()] = path.read_text(encoding="utf-8")
    return records


def link_destinations(path: Path, content: str) -> set[Path]:
    destinations: set[Path] = set()
    for target in MARKDOWN_LINK.findall(content):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        destination = target.split("#", 1)[0]
        if destination:
            destinations.add((path.parent / destination).resolve())
    return destinations


def check_structure(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for directory in CANONICAL_DIRECTORIES:
        if not (root / directory).is_dir():
            findings.append(Finding("ERROR", root / directory, "缺少规范内容目录"))
    if not (root / "index" / "topic-map.md").is_file():
        findings.append(Finding("ERROR", root / "index/topic-map.md", "缺少主题地图"))
    if not (root / "kb.config.yaml").is_file():
        findings.append(Finding("ERROR", root / "kb.config.yaml", "缺少知识库配置"))
    return findings


def check_notes(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in root.rglob("*.md"):
        relative = path.relative_to(root)
        if (
            ".git" in relative.parts
            or relative.parts[:2] == (".agents", "skills")
            or relative.parts[0] == "_templates"
        ):
            continue
        content = path.read_text(encoding="utf-8")
        if is_content_note(root, path):
            fields = read_frontmatter(path)
            for required in REQUIRED_FIELDS:
                if required not in fields:
                    findings.append(Finding("ERROR", path, f"缺少必填元数据: {required}"))
        for pattern in SECRET_PATTERNS:
            if pattern.search(content):
                findings.append(Finding("ERROR", path, "发现疑似凭据或私钥模式；请立即人工复核"))
                break
        for resolved in link_destinations(path, content):
            if not resolved.exists():
                findings.append(Finding("WARN", path, f"无法解析相对链接: {resolved}"))
    return findings


def check_bidirectional_links(root: Path) -> list[Finding]:
    notes = canonical_notes(root)

    findings: list[Finding] = []
    for path, content in notes.items():
        for destination in link_destinations(path, content):
            if destination not in notes:
                continue
            if path not in link_destinations(destination, notes[destination]):
                findings.append(
                    Finding(
                        "WARN",
                        path,
                        f"缺少反向链接: {destination.relative_to(root)} 未链接回本笔记",
                    )
                )
    return findings


def check_source_relationships(root: Path) -> list[Finding]:
    notes = canonical_notes(root)
    records = source_records(root)
    findings: list[Finding] = []

    for note, content in notes.items():
        for record in link_destinations(note, content) & records.keys():
            if note not in link_destinations(record, records[record]):
                findings.append(
                    Finding(
                        "WARN",
                        note,
                        f"来源记录缺少派生笔记链接: {record.relative_to(root)}",
                    )
                )

    for record, content in records.items():
        for note in link_destinations(record, content) & notes.keys():
            if record not in link_destinations(note, notes[note]):
                findings.append(
                    Finding(
                        "WARN",
                        record,
                        f"派生笔记缺少来源链接: {note.relative_to(root)}",
                    )
                )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="知识库根目录")
    parser.add_argument("--strict", action="store_true", help="将所有发现作为非零状态返回")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    findings = [
        *check_structure(root),
        *check_notes(root),
        *check_bidirectional_links(root),
        *check_source_relationships(root),
    ]
    if not findings:
        print("知识库检查通过：未发现结构、元数据、链接或常见敏感模式问题。")
        return 0
    for finding in findings:
        print(f"{finding.level}: {finding.path.relative_to(root)} — {finding.message}")
    return 1 if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
