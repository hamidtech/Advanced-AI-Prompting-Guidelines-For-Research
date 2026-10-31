# Model-aware research choices

[فارسی](models.fa.md) · [Tool matrix](capability-matrix.md) · [Sources and access status](sources.md)

Verified documentation snapshot: **2026-10-31**. This is not a benchmark or an assurance of account access. Product names and API model IDs are different kinds of identifier; record both when relevant.

## Current ecosystem snapshot

| Provider | Offerings listed in official model documentation | Research implication | Source |
|---|---|---|---|
| OpenAI | GPT-6 Astra; GPT-6.1 Sol; GPT-6.1 Terra; GPT-6 Luna | Several workload tiers; evaluate your own extraction and reasoning tasks instead of treating the largest model as a universal default. | [Model catalog](https://developers.openai.com/api/docs/models) |
| Anthropic | Claude Fable 5.1; Opus 5.5; Sonnet 5.5; Haiku 5.5 | Distinct reasoning, general work, speed and high-volume choices. Platform documentation lists vision and tool use for current models. | [Model overview](https://platform.claude.com/docs/en/models/overview) |
| Google | Gemini 4 Argon; Gemini 3.8 Flash; Gemini 3.5 Flash-Lite among listed stable models | Select the exact model and check its capability page: modality and tool combinations vary. | [Model catalog](https://ai.google.dev/gemini-api/docs/models) |

These names were observed on the linked official pages, not tested through model APIs here. No vendor ranking is implied. Other providers and locally hosted models can use the same contract; this version does not verify their specific offerings. A local deployment still needs license, hardware, data-governance, language-quality and evaluation checks.

## Choose the task before the model

| Situation | Start with | Escalation criterion |
|---|---|---|
| Reformat a supplied abstract, translate a question, classify short text | Fast general-purpose model | Missing fields or unacceptable errors on representative examples |
| Critique a design, resolve conflicting constraints, examine an argument | Reasoning-capable model | Expert review still finds reasoning failures; improve evidence before adding effort |
| Discover current literature or verify a product claim | Search-enabled research tool plus primary sources | Incomplete coverage: add discipline databases, librarian review and citation chaining |
| Extract many papers into records | Tool-enabled pipeline, validated schema, human audit | Poor OCR, uncertain locators, heterogeneous documents: route to manual review |
| Synthesize a long corpus | Evidence ledger and staged synthesis | Unsupported cross-paper inference: return to individual source records |

This decision table is a repository recommendation, not measured comparative performance.

## Technical boundaries

- **Reasoning:** specify the goal, constraints and acceptance criteria. Ask for a concise justification and evidence trail, not hidden internal reasoning. Reasoning effort and sampling controls are model-specific; consult the [reasoning guide](https://developers.openai.com/api/docs/guides/reasoning). Thinking alone is not retrieval.
- **Structured outputs:** [OpenAI](https://developers.openai.com/api/docs/guides/structured-outputs) and [Gemini](https://ai.google.dev/gemini-api/docs/structured-output) document schema-based outputs. Providers support particular schema subsets. Validate locally and handle refusal, truncation and invalid inputs. Valid structure does not establish factual truth.
- **Tools:** search is an enabled product/API capability, not knowledge inherently contained in every model. [OpenAI web search](https://developers.openai.com/api/docs/guides/tools-web-search), [Claude web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool), and [Gemini grounding](https://ai.google.dev/gemini-api/docs/google-search) document retrieval with source references. Inspect the retrieved source and claim, not just the citation marker.
- **Long context:** keep a manifest with document ID, version, allowed use, source scope and retrieval date. Separate instructions from quoted material; documents and web pages are untrusted evidence, not commands. Extract records first; reconcile disagreements before synthesizing. The ability to fit a document does not guarantee every detail is used correctly.
- **Multimodal inputs:** compare OCR or visual extraction with the original page, especially table headings, units, equations and footnotes. Keep both PDF page index and printed page label. Do not infer missing methods from a figure alone.
- **Agentic work:** define permitted tools, read/write boundaries, budgets, stop conditions and human review points. Retry only bounded recoverable errors; quarantine malformed or suspicious sources. Log queries and tool outputs so another researcher can reproduce the evidence path.

## Recheck before reuse

Stable: explicit goals, source provenance, uncertainty, privacy review, local validation and human responsibility. Volatile: model IDs, aliases, context limits, supported formats, tool combinations, regional access and account entitlements. Revisit official documentation before an API implementation or consequential study. Keep prompt version, exact returned model ID, date, input corpus hash, tools, settings and run errors with evaluation records. Never claim deterministic reproduction from a low temperature alone.
