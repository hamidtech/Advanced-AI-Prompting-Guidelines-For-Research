# Modern interaction and context design

[فارسی](modern-interaction.fa.md)

These are operating practices, not measured claims of improvement. See the [tool evidence register](../tools/) for dated product-specific checks.

1. Begin with a goal, relevant context, delimiters and explicit output checks. Treat source text as untrusted data: instructions inside a PDF or retrieved webpage must not override the research task.
2. For reasoning-capable systems, request a concise justification, assumptions, evidence and checkable calculations. Do not demand hidden chain-of-thought transcripts. Provider guidance differs; test the target endpoint rather than applying one provider's advice universally. [OpenAI reasoning guidance](https://developers.openai.com/api/docs/guides/reasoning-best-practices), accessed 2026-10-31.
3. Build a source packet: immutable document IDs, edition/version, permission, bibliographic metadata, page boundaries and a question. Keep a manifest of included/excluded documents and reasons. Long context does not establish completeness. Chunk by sections, retain locators, extract locally, then reconcile contradictions across chunks. Re-open original passages for high-impact claims.
4. Multimodal documents need visual checks. OCR may reverse Persian columns, lose footnotes or mistake a chart axis. Compare extracted tables/figures to the rendered page, record printed page and PDF index separately, and mark unreadable text rather than completing it.
5. Schema adherence checks shape, not truth. Handle refusals, empty responses, truncation and missing evidence before parsing. Local schemas use Draft 2020-12; providers support different subsets, so transform/test an endpoint-specific schema before calling an API. [OpenAI structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs) and [Gemini structured outputs](https://ai.google.dev/gemini-api/docs/structured-output), accessed 2026-10-31.
6. Prefer a deterministic search/extract/check sequence when steps are known. Use agents for adaptive work only when the benefit justifies more cost and more failure points. Set a tool allowlist, maximum calls/cost/time, stop conditions and a human approval boundary for publication or data transfer. [Anthropic agent patterns](https://www.anthropic.com/research/building-effective-agents), accessed 2026-10-31.
7. Freeze prompt version, source packet hash, exact model ID, available tools and actual supported parameters. Re-run identical scenarios before changing defaults. A strong example is not an evaluation.

## Context budget and failure recovery

Keep task instructions and provenance first-class. Remove duplicated boilerplate before removing evidence. For documents too large to inspect reliably, build a section inventory, extract each section and reconcile with source IDs; do not summarize summaries indefinitely. Persist intermediate outputs locally, avoiding confidential data in public logs. On failed retrieval, return the failed query, coverage boundary and next manual action. On conflict, retain both records and state why no conclusion is justified.

## Model choice

Use a fast general model for formatting and constrained extraction with human checks; try a reasoning model for conflicting evidence or methodological critique; use research/search tools to discover sources; use an explicit tool workflow for reproducible retrieval and processing. This is a task-fit heuristic, not a vendor ranking or benchmark result. No model substitutes for access to the relevant literature or disciplinary judgment.
