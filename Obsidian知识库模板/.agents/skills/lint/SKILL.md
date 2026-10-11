---
name: lint
description: "Run a read-only structure and privacy check over this Obsidian knowledge base template. Use when asked to lint, audit, inspect, or check note structure, links, or maintainability."
---

# Lint

Run:

```bash
python3 scripts/check_template.py --root .
```

The checker is read-only and reports missing structure, missing frontmatter, required examples, and basic privacy markers. Explain failures and obtain approval before fixing files.
