# Independent implementation review

[فارسی](independent-review.fa.md) · Review date: 2026-10-31

This review was conducted by a separate AI agent from the content authors. It is an independent implementation pass within this task, not external peer review, human disciplinary approval, or empirical validation of prompt quality. The parent implementation agent also reviewed content and source claims.

## Scope and findings

| Perspective | Reviewed evidence | Finding and action |
|---|---|---|
| Academic validity | Prompt contract, topic critic, synthesis prompt, gap and paper workflows, evaluation protocol | Ideas remain hypotheses; source identity is separate from entailment; no universal novelty claim. Requested clarification of synthesis-only missing-source wording when reused in other prompt types. |
| AI technical accuracy | Foundation guidance, model/tool snapshot, source register, API handling pattern | Model-specific controls are separated from prose exploration modes; local schema compliance is not factual accuracy or universal provider compatibility. No live provider integration was tested. |
| Interdisciplinary accessibility | Five EN/FA discipline profiles, especially humanities and theology | Interpretive, historical, normative and empirical approaches retain distinct evidence criteria. Feasibility examples expose missing access and supervision instead of implying resources exist. |
| English/Persian quality | Paired file structure, placeholder sets, sample full prompts and completed examples | Equivalent fields are checked automatically; sampled Persian passages preserve the evidence safeguards. Machine checks do not certify translation quality or naturalness; a human academic editor remains desirable. |
| Structure and maintainability | Catalog metadata, schemas, validator, negative tests, root entrypoints | Fixed exact language filenames, missing reverse pairs, mismatched placeholders, evaluation ID/path disagreement and malformed metadata handling. Required-file and internal-link checks identify missing targets. |
| Security and privacy | CI permissions, action pins, automation examples, integrity guidance | CI is read-only, credential persistence disabled, no service secrets needed. Documents are untrusted data; permission and privacy checks precede transfers. API examples are patterns, not secretly executed integrations. |
| Citation accuracy | Historical archive, source register, paper-to-evidence examples | Historical references are explicitly unverified; new worked evidence is labeled synthetic. The source register distinguishes opened pages from search-only/failed retrieval. This reviewer did not independently retrieve every official URL or certify vendor claims. |
| Evaluation methodology | Thirty scenarios, provisional rubric, baseline mapping, run schema and planner | No fabricated benchmark results. Five disciplines × six conditions are enforced, duplicate cases rejected, EN/FA separate, model/configuration/turn handling declared. Review scores remain null without an evaluator. Repetitions are not treated as independent research topics. |

## Corrections made during this pass

- Canonical evidence schema now requires a nonempty reviewer for `checked` records, rather than restricting only the bundled fixture.
- Semantic validation rejects evidence fields pointing to a different source ID.
- Evaluation validation enforces 30 unique cases, one case per discipline/condition pair, distinct bilingual inputs, valid prompt IDs and matching paths.
- Catalog validation checks exact English/Persian filenames, placeholder parity and minimum section structure; incomplete or malformed metadata fails cleanly.
- Four mutation tests prove that a broken internal link, missing translation, duplicate prompt ID and malformed metadata fail validation rather than slipping through or crashing.
- Trailing whitespace was removed from current Markdown without changing historical archive bytes.
- Evaluation run-schema tests were added to CI. The evaluation author strengthened artifact and reviewer requirements after review feedback.

## Checks actually run

```bash
PYTHONPATH=/tmp/research-v2-deps python -m unittest discover -s automation/scripts -p 'test_*.py'
PYTHONPATH=/tmp/research-v2-deps python -m unittest discover -s evaluation -p 'test_*.py'
PYTHONPATH=/tmp/research-v2-deps python automation/scripts/validate.py
git diff 59e3911 HEAD --check -- . ':(exclude)legacy/**'
```

Final review checks: **14 automation tests passed**, **3 evaluation infrastructure tests passed**, and the **full repository validator passed** with 10 prompts, 4 workflows, 30 cases and 79 current Markdown files. The two initially missing delivery-report links were resolved. Synthesis-only missing-source restrictions were removed from the other nine prompt types. `git diff 59e3911 HEAD --check -- . ':(exclude)legacy/**'` returned no errors for current files. The archived originals retain historical trailing whitespace intentionally; an unrestricted staged/base diff reports that whitespace, so it is excluded from the current-content check. These are local checks, not a claim that GitHub-hosted CI or live models were executed.

## Remaining validation boundaries

No real model comparison, reviewer-rating study, commercial API call, signed-in product test, exhaustive external-link scan, GitHub-rendered Mermaid inspection, or human disciplinary/bilingual review was performed by this reviewer. Mermaid decision branches were inspected as source. No measured superiority, full literature coverage, or scientific validity is inferred from passing software checks.
