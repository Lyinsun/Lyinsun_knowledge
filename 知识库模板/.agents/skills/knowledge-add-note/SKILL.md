---
name: knowledge-add-note
description: Create or update one source-backed Markdown engineering note in this knowledge base. Use when asked to document an architecture, service, module, concept, interface, workflow, operation, or engineering decision.
---

# Knowledge Add Note

1. Read `AGENTS.md`, `kb.config.yaml`, `index/topic-map.md`, and the target directory README.
2. Search for an existing note with the same scope. Update the canonical note instead of creating a near-duplicate.
3. Create or reference a redacted record in `sources/` before asserting externally derived facts.
4. Copy the applicable file in `_templates/`; assign a stable ID, owner role, status, review date, source IDs, and relative links.
5. Add each cross-note relationship at both ends: the originating note links to the target, and the target's `相关内容` links back. Whenever a canonical note cites a source record, link to the record in `来源` and add the canonical note to the record's `派生笔记` in the same update.
6. Separate verified facts from inferences and pending items. Do not invent citations.
7. Update `index/topic-map.md` with the new or changed canonical entry.
8. Run `python3 .agents/skills/knowledge-lint/scripts/check_knowledge_base.py --root .` as an advisory checklist and `git diff --check`. Use `--strict` only when the user explicitly requests a gate.
9. Refuse to write credentials, PII, internal identifiers, raw private sources, absolute local paths, or unredacted logs. Use the placeholders in `docs/PRIVACY.md`.
