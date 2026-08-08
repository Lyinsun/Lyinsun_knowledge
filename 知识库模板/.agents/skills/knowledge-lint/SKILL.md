---
name: knowledge-lint
description: Perform an advisory, read-only health check of this Markdown engineering knowledge base for metadata, relative links, source relationships, index presence, and common sensitive-content patterns. Use when asked to inspect, audit, lint, or diagnose knowledge-base structure, quality, or sharing safety.
---

# Knowledge Lint

Run the deterministic check first:

```bash
python3 .agents/skills/knowledge-lint/scripts/check_knowledge_base.py --root .
```

The checker never edits content. Its default mode is advisory: it reports canonical-directory, metadata, local-link, source-relationship, topic-map, and selected high-risk-secret findings so an Agent can decide what to repair in the current task.

Interpret the result carefully:

- Fix only the files the user asked to change.
- Treat a privacy match as a stop-and-review signal. Do not print the suspected value in a reply or copy it elsewhere.
- Treat missing sources and stale review dates as evidence gaps, not permission to fabricate a conclusion.
- Run `git diff --check` after approved edits.
- Use `--strict` only when the user explicitly asks for CI or release gating; ordinary maintenance should not be blocked by unrelated diagnostic findings.
