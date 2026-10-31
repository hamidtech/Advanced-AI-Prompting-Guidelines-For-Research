# Advanced AI Prompting Guidelines for Research

From prompt templates to evidence-based AI research workflows — **Version 2.0**.

[راهنمای فارسی](README.fa.md) · [MIT License](LICENSE) · [Contributing](CONTRIBUTING.md)

Choose the task you need to do. You do not need programming, JSON, an API account, or an agent to start. AI suggestions are candidates to investigate; they are not evidence of novelty.

## Layer 1 — Start with your research question

| I want to… | Start here |
|---|---|
| Discover what interests me | [Interest discovery](catalog/prompts/interest-discovery.md) |
| Explore thesis topics | [Thesis brainstormer](catalog/prompts/thesis-brainstormer.md) |
| Find an angle for an article | [Article angles](catalog/prompts/article-angle-explorer.md) |
| Develop a book concept | [Book concepts](catalog/prompts/book-concept-explorer.md) |
| Improve an existing title | [Title refiner](catalog/prompts/title-refiner.md) |

Open a template, replace the fields you know, write “unknown” for the others, and copy its full prompt into a suitable AI tool. Ask it to explain assumptions and evidence boundaries. Check any factual claim against original sources before using it.

## Layer 2 — Build a defensible research workflow

- [Topic to Title](catalog/workflows/topic-to-title.md)
- [Topic Validation](catalog/workflows/topic-validation.md)
- [Gap Verification](catalog/workflows/gap-verification.md)
- [Paper to Evidence](catalog/workflows/paper-to-evidence.md)

Read the [Research Prompt Contract](docs/foundations/prompt-contract.md), [modern interaction guide](docs/foundations/modern-interaction.md), [discipline profiles](docs/disciplines/) and [integrity guidance](docs/integrity/). Tool capabilities and their verification dates are in the [tool guide](docs/tools/).

## Layer 3 — Structure, automate and evaluate

Use [schemas](catalog/schemas/), [synthetic examples](examples/README.md), [optional automation](automation/README.md), and the [evaluation protocol](evaluation/README.md). Thirty bilingual scenarios support controlled comparisons. Empirical model comparisons are **pending**; this release does not claim measured improvements.

## All ten prompts

| ID | English template | فارسی |
|---|---|---|
| RP-01 | [Focused Thesis Brainstormer](catalog/prompts/thesis-brainstormer.md) | [ایده‌پردازی متمرکز پایان‌نامه](catalog/prompts/thesis-brainstormer.fa.md) |
| RP-02 | [Article Angle Explorer](catalog/prompts/article-angle-explorer.md) | [کاوش زاویه‌های مقاله](catalog/prompts/article-angle-explorer.fa.md) |
| RP-03 | [Book Concept Explorer](catalog/prompts/book-concept-explorer.md) | [کاوش ایدهٔ کتاب](catalog/prompts/book-concept-explorer.fa.md) |
| RP-04 | [Cross-Disciplinary Research Title Maker](catalog/prompts/cross-disciplinary-title.md) | [عنوان‌سازی میان‌رشته‌ای](catalog/prompts/cross-disciplinary-title.fa.md) |
| RP-05 | [Research Gap Hypothesis Generator](catalog/prompts/gap-hypothesis.md) | [تولید فرضیهٔ شکاف پژوهشی](catalog/prompts/gap-hypothesis.fa.md) |
| RP-06 | [Research Interest Discovery](catalog/prompts/interest-discovery.md) | [کشف علاقهٔ پژوهشی](catalog/prompts/interest-discovery.fa.md) |
| RP-07 | [Research Topic Critic](catalog/prompts/topic-critic.md) | [نقد موضوع پژوهش](catalog/prompts/topic-critic.fa.md) |
| RP-08 | [Research Title Refiner](catalog/prompts/title-refiner.md) | [اصلاح عنوان پژوهش](catalog/prompts/title-refiner.fa.md) |
| RP-09 | [Evidence-Grounded Literature Synthesizer](catalog/prompts/literature-synthesizer.md) | [ترکیب پیشینه بر پایهٔ شواهد](catalog/prompts/literature-synthesizer.fa.md) |
| RP-10 | [Research Feasibility Assessor](catalog/prompts/feasibility-assessor.md) | [ارزیابی امکان اجرای پژوهش](catalog/prompts/feasibility-assessor.fa.md) |

## Migration and maintenance

The original five files are preserved byte-for-byte in [the historical archive](legacy/2024-gpt-4o/). Root guide URLs remain available as current entry points; historical heading fragments may need the archived versions. The missing [modern guide](ModernResearchPrompting.md) is now implemented. See [audit and migration](docs/audit-and-migration.md), [changelog](CHANGELOG.md), [validation instructions](automation/README.md) and [delivery report](docs/delivery-report.md).

External capabilities are dated snapshots, not promises of access, pricing or universal vendor superiority. Source coverage, Persian quality, publication policies and data permissions must be checked in each project. The author and researcher remain responsible for submitted work.
