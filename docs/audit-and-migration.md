# Repository audit and migration inventory

Audit date: 2026-10-31. Base: `59e3911`. Inventory recorded before changing existing files.

## Observed state

Five tracked files; eight commits (2024–2026); MIT copyright Hamid Jamali retained. No existing CI, tests, contribution guide, schemas, or agents instructions. All five files and the complete commit log/stat were inspected. The June 2026 README promises a modern guide that is absent from HEAD and history. It describes an update that was not implemented.

## Findings

- `ModernResearchPrompting.md` is a broken root link. Fix with a current compatibility entry point.
- Role labels and RTF/CTF/RASCEF/TAG/RISE are useful organizational mnemonics, not validated scientific standards.
- Creativity wording is sometimes called a setting; text cannot change API temperature. The inspected files do not contain a numeric temperature prescription: do not attribute one to them.
- Gap prompts accept unsourced summaries and named-author examples, then imply novelty without a search protocol or contradiction check.
- English/Persian examples differ in discipline and detail; they are adaptations, not aligned translations.
- Thesis summary demands unavailable fields and mixes paragraph/table instructions. Its sample numerical results and bibliographic descriptions are not verified evidence. Preserve but clearly isolate these examples.
- No privacy, disclosure, authorship responsibility, source locator, evidence status, evaluation protocol, or model capability boundary.
- Reusable: beginner-friendly task families, editable inputs, iterative refinement, and simple output shapes.

## Migration map

| Original | Preserved path | Current replacement | Compatibility |
|---|---|---|---|
| README.md | legacy/2024-gpt-4o/README.md | README.md + README.fa.md | Root retained |
| EnglishGuideline.md | legacy/2024-gpt-4o/EnglishGuideline.md | EnglishGuideline.md links to catalog | Root retained |
| PersianGuideline.md | legacy/2024-gpt-4o/PersianGuideline.md | PersianGuideline.md links to catalog | Root retained |
| ThesisSummaryPrompt.md | legacy/2024-gpt-4o/ThesisSummaryPrompt.md | ThesisSummaryPrompt.md → paper-to-evidence | Root retained |
| LICENSE | legacy/2024-gpt-4o/LICENSE | LICENSE unchanged | Identical bytes |
| ModernResearchPrompting.md (absent) | Not applicable | ModernResearchPrompting.md | Missing link repaired |

The archive directory denotes the original GPT-4o lineage, not the last edit date: its README includes a 2026 change. Original files are copied byte-for-byte. Old root file URLs remain valid; legacy heading fragments may require the archived file because replacement entry points have new headings. Archive links are historical, not current recommendations.
