# Evaluation protocol — infrastructure, not measured improvement

[فارسی](README.fa.md) · [Cases](cases/scenarios.json) · [Rubric](rubrics/topic-quality.md) · [Baselines](baselines/README.md) · [Status](results/pending-status.json)

Thirty authored scenarios cover five disciplines and six entry conditions per discipline. English and Persian versions carry equivalent constraints; they are separate test inputs. They are illustrative fixtures, not representative samples of all research practice. No model runs or expert ratings have been performed for this version.

## Controlled comparison

1. Freeze the repository commit, scenario file SHA-256, prompt text, source packet, and model configuration. Select a provider/model actually available to the evaluator; record the exact identifier rather than “latest.” Record endpoint, execution date/time, tool availability, reasoning controls, output limit, supported sampling settings and provider defaults that cannot be controlled. Never force an unsupported temperature parameter.
2. Build the legacy and modern prompts using the [baseline mapping](baselines/README.md). Append exactly the same case input. Attach exactly the same evidence packet. Do not silently add evidence to the modern arm. Modern safeguards intrinsic to the template remain part of the intervention. A comparison changes the whole prompt package, not one isolated causal mechanism.
3. Run English and Persian independently, in fresh sessions with no shared conversation history. At least three repetitions per prompt/case/language are recommended; three are an initial planning choice, not a power calculation. Use the seeded planner to randomize arm order. Its seed affects scheduling only; generation may remain nondeterministic.
4. If a prompt asks clarifying questions, save that turn and use a prewritten, identical case-specific answer in both arms. Record all turns, cost/latency if measured, and whether a turn limit was reached. Do not let one arm receive more substantive information. If no answer is available, evaluate the clarification behavior separately and mark final-output ratings unavailable.
5. Preserve raw outputs before any editing. Review source claims against supplied documents or a recorded search. Count unsupported claims and citation errors separately. A real identifier does not prove a citation supports the claim. Evidence packets should contain reusable, rights-cleared material and explicit source locators.
6. Blind and randomize arm labels for at least two qualified discipline reviewers when available. Reviewers score [six dimensions](rubrics/topic-quality.md), flag integrity failures, and explain disagreement. Record expertise and conflicts without publishing personal information. Do not call an author self-check independent expert validation.
7. Report paired differences within case, language and model. Report coverage, missing ratings, repetition variability and reviewer disagreement before an aggregate. With only six cases per discipline, avoid broad superiority claims and avoid treating repetitions as independent research topics. Keep failed, refused and incomplete runs in the denominator with declared handling rules.

## Execute a planning dry run

```bash
python evaluation/plan_runs.py --model MODEL_ID --repetitions 3 --seed 20261031 --output /tmp/research-run-plan.json
```

This writes 360 planned records (30 × 2 languages × 2 arms × 3 repetitions). It calls no model and produces no scores. Review and freeze the manifest before using a provider-specific runner. Do not commit private inputs, credentials, or unredacted raw outputs.

## Recording and checks

Use [run.schema.json](results/run.schema.json) for completed, failed or blocked executions. `null` scores mean unreviewed; zero means reviewed and seriously deficient. Store failed attempts too. A [recording template](results/record-template.md) supports manual work without JSON.

Automated checks can establish JSON structure, case counts, language completeness, duplicate identifiers and presence of expected fields. They cannot establish scholarly novelty, translation quality, source entailment, feasibility, or prompt quality. Citation matching and phrase checks are triage signals requiring human adjudication.

Before a real study, test the run-record schema with one valid and several invalid records, pilot two cases in both languages, predeclare exclusion rules, and agree reviewer anchors. Record any changed rubric or case version. Never backfill an output and label it a historical legacy run.

## Coverage limitations

The six baseline RTF/CTF/TAG/RISE uses intentionally reuse older templates for tasks they did not explicitly support. Report that limitation. Book concepts, article angles, topic criticism and literature synthesis are not directly benchmarked by these thirty initial cases; add separate cases before claiming coverage of all ten templates. Tool execution and multimodal extraction require their own source packets and tests. No empirical benchmark result is delivered here.

## Run infrastructure tests

After installing the repository validation dependencies:

```bash
python evaluation/test_infrastructure.py
```

[Recorded local checks](results/infrastructure-checks.md) distinguish software test results from pending empirical evaluations.
