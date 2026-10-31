# Version 2.0 delivery report

[فارسی](delivery-report.fa.md) · Prepared 2026-10-31 · [Independent review](independent-review.md)

## Audit and architecture

The base commit is `59e3911714f1d9f0ee39d4222bb37aa976cf3358`. Five original files and eight commits were inspected. The README advertised a missing modern guide; legacy prompts blurred idea generation and verified gaps, lacked source provenance and omitted privacy/disclosure. No CI, schemas or evaluation existed. [Audit and migration inventory](audit-and-migration.md) records findings before root files changed.

The implementation stays Markdown-first: Layer 1 offers copyable task templates; Layer 2 adds evidence-aware workflows; Layer 3 adds optional JSON/automation/evaluation. No API or programming is required for the first two layers. [English](../README.md) and [Persian](../README.fa.md) entry points navigate by user task. MIT license and attribution are unchanged.

## Migration

Five original files are preserved byte-for-byte in `legacy/2024-gpt-4o/`; archive equality is checked against the base commit. README is replaced by layered EN/FA entry points; EnglishGuideline and PersianGuideline become current links with archive references; ThesisSummaryPrompt routes to evidence extraction before synthesis. ModernResearchPrompting now exists. Root filenames are compatible; historical heading fragments may require archive URLs. The archive label reflects GPT-4o lineage, not the last edit date.

## Prompt library

Ten complete EN/FA pairs and JSON metadata are in [catalog/prompts](../catalog/prompts/): RP-01 Thesis Brainstormer; RP-02 Article Angle Explorer; RP-03 Book Concept Explorer; RP-04 Cross-Disciplinary Title; RP-05 Gap Hypothesis; RP-06 Interest Discovery; RP-07 Topic Critic; RP-08 Title Refiner; RP-09 Literature Synthesizer; RP-10 Feasibility Assessor. Each includes editable/explained inputs, use boundaries, full prompt, fully substituted example, follow-ups, failure modes and version. Examples are editor-authored illustrations, not measured model outputs.

## Workflows and disciplines

| Workflow | Delivered output |
|---|---|
| [WF-01 Topic to Title](../catalog/workflows/topic-to-title.md) | Interest map, shortlist and bounded provisional title |
| [WF-02 Topic Validation](../catalog/workflows/topic-validation.md) | Relevance, feasibility, contribution assessment and decision dossier |
| [WF-03 Gap Verification](../catalog/workflows/gap-verification.md) | Search/extraction/contradiction trail and qualified assessment |
| [WF-04 Paper to Evidence](../catalog/workflows/paper-to-evidence.md) | Locatable evidence records followed by checked prose |

Each workflow has an aligned Persian pair, stage prompts, intermediate outputs, error recovery, checkpoints and worked illustration. Engineering, life sciences, social sciences/management, humanities, and theology have complete EN/FA [profiles](disciplines/). Interpretive and normative work is not forced into experimental designs.

## Research updates

The [prompt contract](foundations/prompt-contract.md) preserves historical mnemonics as organizational aids, without scientific-validation claims. Exploration instructions are separated from API temperature. [Modern interaction](foundations/modern-interaction.md) addresses reasoning, context, OCR, structured output, untrusted documents and bounded tool workflows. [Tool matrix](tools/capability-matrix.md), [model snapshot](tools/models.md), [source register](tools/sources.md), and [integrity guide](integrity/research-integrity.md) distinguish observed documentation from tested access and source reporting from inference. Sources include official providers, scholarly infrastructure, ICMJE, COPE, Nature, PRISMA and Cochrane, with access dates and failed retrievals retained.

## Validation and evaluation

Implemented Draft 2020-12 schemas cover prompt metadata, workflow metadata, evidence records and topic candidates. Evaluation adds case and execution-record schemas. Offline validation checks required files, JSON/schema validity, stable IDs, catalog references, language pairs/placeholders, internal links/heading fragments, basic formatting, historical bytes, and thirty balanced unique bilingual cases. Negative tests reject invalid provenance, missing translations, duplicate IDs, malformed metadata and broken links.

Commands used from the repository root (dependency installed in a temporary local path during authoring):

```bash
python automation/scripts/validate.py
python -m unittest discover -s automation/scripts -p 'test_*.py'
python evaluation/test_infrastructure.py
python evaluation/plan_runs.py --model MODEL_ID --repetitions 3 --seed 20261031 --output /tmp/research-run-plan.json
```

Fourteen automation tests and three evaluation infrastructure test methods passed. The latter include valid and eleven invalid execution-record mutations and a deterministic 360-record planning manifest. Final local validator: **PASS** (10 prompts, 4 workflows, 30 cases, 79 current Markdown documents; no errors). Remote CI status is reported with the pull request; CI execution is separate from installing its workflow. The SHA-pinned read-only workflow runs all three validation commands, without secrets or privileged triggers. Mermaid source uses standard flowchart syntax; a live GitHub rendering check is not a measured test in this report.

Thirty evaluation scenarios cover six entry conditions in each of five disciplines. Protocol, exact historical baseline mapping, provisional six-dimension rubric and honest pending status exist. **Zero research-model calls, zero expert ratings, and no empirical improvement estimates.** The initial scenarios directly exercise six of ten templates; book/article/critique/synthesis, multimodal extraction and tool execution need additional cases before claims of full evaluation coverage.

## Independent QA and limits

A separate AI reviewer checked academic validity, technical guidance, accessibility, both languages, structure, privacy/security, citation handling and evaluation method. Fixes strengthened checked-evidence reviewer requirements, source-ID agreement, language-file pairing, malformed-data handling, scenario balance/references and mutation tests. [Review record](independent-review.md) distinguishes AI review from qualified human disciplinary validation.

No commercial model API or signed-in product capability was tested. COPE/Nature direct retrieval was blocked; official-domain search text supported bounded statements and is labeled accordingly. Elicit API retrieval timed out; SciSpace API contract and ResearchRabbit export formats remain unverified. Source checks do not prove vendor claims or exhaustive literature coverage. Broad empirical validation and native-speaker/expert review remain pending. Do not infer scientific quality from passing CI.

## GitHub delivery and next steps

Dedicated branch: `v2/evidence-based-research-workflows`, based on the audited main commit. Changes are prepared for a draft PR against main; no merge, release publication, settings or visibility change is authorized or performed. The PR conversation and branch commit history are the authoritative transport record.

Version 2.1 priorities: (1) recruit bilingual discipline reviewers and pilot paired runs with a predeclared protocol; (2) add rights-cleared source packets and cases for the four currently unbenchmarked templates plus OCR/tool failures; (3) recheck volatile product/API and blocked policy sources; (4) calibrate rubric anchors and translation agreement before reporting comparative scores. These are future work, not completed experiments.
