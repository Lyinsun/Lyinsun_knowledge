---
name: knowledge-ingest
description: Convert approved source material into a source record and a small set of linked Markdown engineering notes. Use when asked to import, compile, organize, or refresh documentation from a document, repository, meeting record, or other source.
---

# Knowledge Ingest

1. Read `AGENTS.md`, `docs/PRIVACY.md`, `docs/CONTENT-MODEL.md`, and `index/topic-map.md`.
2. Classify the source visibility before copying any content. If it is restricted, preserve the original in an approved external location and retain only a minimum redacted record in `sources/`.
3. Produce a concise update plan: source record, proposed canonical notes, ownership, evidence level, and index changes. Ask for confirmation when the plan creates multiple new topics or changes existing authoritative conclusions.
4. Create the source record, then derive only source-backed notes. Keep facts, inferences, quotations, and unresolved gaps distinct.
5. Avoid copying full documents when a durable summary and a reference are enough. Do not include names, URLs, credentials, private logs, or organization-specific identifiers.
6. Link new notes with relative Markdown links, update `index/topic-map.md`, and run `knowledge-lint` plus `git diff --check`.
