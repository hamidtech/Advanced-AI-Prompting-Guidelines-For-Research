# Legacy baseline construction

[فارسی](README.fa.md)

Legacy files are byte-preserved at [English archive](../../legacy/2024-gpt-4o/EnglishGuideline.md) and [Persian archive](../../legacy/2024-gpt-4o/PersianGuideline.md). Freeze base `59e3911` and the actual archived file hash in a study manifest. Do not use the new root compatibility stubs as the legacy prompt.

| Scenario condition | Legacy top-level section, English / Persian | Modern identifier |
|---|---|---|
| No topic | Focused Thesis Brainstormer / طوفان فکری متمرکز پایان‌نامه | RP-06 |
| Broad interest | Focused Thesis Brainstormer / طوفان فکری متمرکز پایان‌نامه | RP-01 |
| Candidate title | Focused Thesis Brainstormer / طوفان فکری متمرکز پایان‌نامه | RP-08 |
| Limited resources | Focused Thesis Brainstormer / طوفان فکری متمرکز پایان‌نامه | RP-10 |
| Incomplete evidence | Research Gap Finder / یابنده شکاف پژوهشی | RP-05 |
| Interdisciplinary | Cross-Disciplinary Research Title Maker / عنوان‌ساز میان‌رشته‌ای پژوهش | RP-04 |

Extract only the fenced prompt under `Prompt Template (with placeholders)` / `قالب تمپلیت (با جای‌خالی‌ها)` in the selected section. Do not include the filled-in example or explanatory text. For the Persian interdisciplinary section, the heading is `قالب تمپلیت (با جای‌خالی‌ها)` as in the source. Preserve original wording, including unsupported creativity-setting language: correcting it would change the baseline.

Bind placeholders only from the shared case input; unknown inputs remain explicitly “not specified” / «مشخص نشده». Append the case text verbatim after the prompt. Save the resulting rendered prompt and a binding map before execution. Do not add missing research facts. Use neutral “balanced” / «متوسط» for a creativity placeholder not specified by the case, and record that fixed choice in both arms. Record any modern exploration mode separately; do not equate it with API sampling.

The archive has no direct interest-discovery, title-refinement, or feasibility template. Reusing the brainstormer is a declared pragmatic baseline; it creates a task-fit difference and cannot support a claim about all historic prompting or the isolated effect of evidence rules. Include unassisted or other contemporary baselines in a later study if useful. Thirty initial scenarios cover six modern templates, not all ten.

## Exact historical sections for the complete modern catalog

| Modern ID | Closest historical section | Comparison status |
|---|---|---|
| RP-01 | Focused Thesis Brainstormer (RTF) | Initial cases |
| RP-02 | Article Angle Explorer (CTF) | Not evaluated by initial cases |
| RP-03 | Comprehensive Book Outline Generator (RASCEF) | Not evaluated by initial cases |
| RP-04 | Cross-Disciplinary Research Title Maker (TAG) | Initial cases |
| RP-05 | Research Gap Finder (RISE) | Initial cases |
| RP-06 | Focused Thesis Brainstormer (RTF) | Indirect task-fit baseline |
| RP-07 | No direct historical template | Additional baseline design needed |
| RP-08 | Focused Thesis Brainstormer (RTF) | Indirect task-fit baseline |
| RP-09 | ThesisSummaryPrompt.md, English Section / بخش فارسی | Additional source-grounded fixtures needed |
| RP-10 | Focused Thesis Brainstormer (RTF) | Indirect task-fit baseline |

The summary archive contains illustrative bibliographic and numerical claims whose correctness has not been verified. Never treat them as an evidence packet or ground truth.
