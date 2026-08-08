---
name: knowledge-query
description: Search a Git-based Markdown engineering knowledge base and return evidence-backed answers with verified facts, inferences, and gaps. Use when asked to find, explain, compare, or verify architecture, services, modules, concepts, interfaces, workflows, operations, or decisions.
---

# Knowledge Query

1. Read `kb.config.yaml`, `AGENTS.md`, `index/topic-map.md`, and the relevant directory README.
2. Start from the topic map, then use `rg` to locate topic names, stable IDs, source IDs, and related files.
3. Read only candidate notes and their cited source records. Treat a source-backed, `active` note as stronger evidence than a draft, an inference, or an uncited statement.
4. Answer in three parts: verified facts, reasonable inferences, and open verification gaps. List files actually used.
5. Do not modify notes, indexes, or source records unless the user explicitly asks for an update.
6. Never reveal or reconstruct restricted source material, personal data, credentials, internal identifiers, or absolute paths. Report only a risk category when sensitive material is encountered.
