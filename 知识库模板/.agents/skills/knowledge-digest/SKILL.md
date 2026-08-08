---
name: knowledge-digest
description: Distill a completed investigation, delivery, incident review, or discussion into durable engineering knowledge without retaining a private transcript. Use when asked to summarize, retain lessons, capture a decision, or turn task outcomes into reusable documentation.
---

# Knowledge Digest

1. Identify the original question, verified evidence, decision or outcome, limitations, and reusable lesson.
2. Put temporary questions and follow-ups in `qa/`; put durable facts in the appropriate canonical directory and decisions in `decisions/`.
3. Create a source record when the conclusion depends on material outside this repository. Do not claim confidence beyond the evidence.
4. Preserve only the minimum useful context. Remove people, organization names, URLs, IDs, credentials, private logs, and raw conversation text.
5. Update the topic map when a new canonical note is created. Link related notes using relative Markdown links at both ends, following `docs/LINKING.md`.
6. Run `knowledge-lint` and report facts, inferences, omissions, and remaining verification work.
