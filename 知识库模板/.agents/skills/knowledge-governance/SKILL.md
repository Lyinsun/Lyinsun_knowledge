---
name: knowledge-governance
description: Apply content ownership, evidence, review, retention, and privacy rules to a Markdown engineering knowledge base. Use when asked to design governance, review material for inclusion, prepare content for sharing, or decide where a knowledge item belongs.
---

# Knowledge Governance

1. Read `AGENTS.md`, `kb.config.yaml`, `docs/CONTENT-MODEL.md`, and `docs/PRIVACY.md`.
2. Classify each item as a verified engineering fact, inference, decision, source record, or temporary question. Store it in the corresponding canonical directory.
3. Require an owner role, review date, status, and source IDs for every authoritative engineering note.
4. Keep raw restricted material outside the repository. Store only approved, minimum redacted summaries and visibility metadata in `sources/`.
5. Before sharing, verify that links are relative and that the material contains no people, real organizations, internal endpoints, credentials, production identifiers, or private raw data.
6. Use `knowledge-lint` as a baseline check, then explain any risks that require human review. Do not approve or publish external content without user authorization.
