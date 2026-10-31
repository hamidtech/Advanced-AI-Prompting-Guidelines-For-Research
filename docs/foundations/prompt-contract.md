# Research Prompt Contract

[فارسی](prompt-contract.fa.md)

This is a repository design convention, not an experimentally validated universal formula. Start with the smallest contract that makes your task reviewable.

| Element | Requirement | What to write |
|---|---|---|
| Research goal | Required | The decision or artifact needed; distinguish ideation from verification |
| Context | Required, may be unknown | Discipline, audience and stage; say “not decided” instead of inventing a method |
| Evidence | Required status; documents task-dependent | Supplied source IDs, search access, or explicitly “none yet” |
| Constraints | Required status | Time, data access, ethics, language, budget; unknown is allowed |
| Expected output | Required | A short list, comparison, extraction table or machine-readable object |
| Verification | Required | Who checks which claims, against which original material |
| Evaluation and iteration | Required stopping rule | Criteria for revision, maximum cycles, and escalation to a supervisor |

For brainstorming, an evidence status of “hypothesis only” is acceptable. For claims about published results, source support and locators are essential. Role/persona, examples, technical parameters and JSON are optional. Ask at most three focused questions when missing information would change a decision; do not turn uncertainty into a long mandatory questionnaire.

## Copyable minimal contract

```text
Goal: explore a manageable Master's topic in my discipline.
Context: IT management; early stage; method not decided.
Evidence: none supplied; ideas are hypotheses, not verified gaps.
Constraints: six months; only public non-personal data; Persian output.
Output: three candidate problems, resources, uncertainties and next checks.
Verification: do not invent sources; I will verify access and search literature.
Iteration: shortlist only after evidence and feasibility checks; ask up to three critical questions.
```

## Historical mnemonics

| Pattern | Expansion | Useful for | What it omits / risk |
|---|---|---|---|
| RTF | Role, Task, Format | Small well-bounded requests | Persona can imply authority; no evidence check |
| CTF | Context, Task, Format | Situating article exploration | Constraints and verification remain implicit |
| RASCEF | Role, Action, Steps, Context, Examples, Format | Longer book outlines | Too many imposed steps; examples can anchor outcomes |
| TAG | Task, Action, Goal | Keeping a deliverable tied to purpose | Little guidance on provenance or quality |
| RISE | Role, Input, Steps, Expectation | Source-oriented extraction | Input may itself be false or incomplete |

Retain useful labels but add evidence status, constraints and review criteria. None of these acronyms is presented here as a scientific standard. See the [migration inventory](../audit-and-migration.md).

## Exploration modes

Conservative: stay close to supplied concepts. Balanced: offer familiar and adjacent approaches. Exploratory: include plausible combinations with explicit feasibility checks. Unconventional: challenge assumptions and propose unusual interpretations, marking speculative parts. These describe requested ideation behavior; they do not set API temperature or guarantee diversity, novelty or truth. Sampling controls are endpoint/model-dependent. Record actual API parameters if used; never infer them from prose.
