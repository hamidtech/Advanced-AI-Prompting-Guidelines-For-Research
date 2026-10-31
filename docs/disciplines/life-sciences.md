# Life sciences and biology research profile

[فارسی](life-sciences.fa.md) · Version 2.0.0 · Updated 2026-10-31

## Questions and contribution

Separate descriptive questions (what is present), associations (what varies together), mechanisms (how a process works), and interventions (what changes an outcome). Biology includes field observation, taxonomy, laboratory research, computational analysis, and evidence synthesis; a clinical trial is not the default design.

A contribution can be a carefully bounded replication, a characterized biological resource, a reproducible analysis, or a synthesis resolving conflicting evidence. An association or in-silico prediction does not establish a biological mechanism or clinical efficacy.

## Materials, constraints, and sources

Materials may include specimens, sequences, microscopy images, ecological records, laboratory notebooks, public datasets, or published studies. Record organism, population, tissue, experimental unit, provenance, assay, and relevant environmental conditions. Do not confuse repeated measurements of one specimen with independent biological replicates.

Check ethical approval, consent or reuse conditions, biosafety, specimen availability, batch effects, training requirements, and equipment time before suggesting work. Identifiable health records and potentially identifying genomic data require an approved handling route. Do not send them to a consumer AI service merely because names were removed. Do not use an AI-generated protocol as operational authorization.

Search original studies and appropriate discipline databases; verify dataset accession identifiers and versions against the hosting repository. Use reviews for orientation, then inspect underlying studies. [EQUATOR's reporting-guideline library](https://equator-network.org/reporting-guidelines/index.html) routes health research to design-specific guidance; reporting checklists are not substitutes for design or risk-of-bias appraisal. See its [explicit distinction between reporting and study design](https://equator-network.org/reporting-guidelines/qualitative-research-standards-challenges-and-guidelines/). References accessed 2026-10-31.

## Method and verification

Specify the biological question before choosing a model. Distinguish discovery from confirmatory analysis. Plan controls, confounders, independent units, missing data, multiple testing, and sample-size justification with an appropriate supervisor or statistician. No universal sample size or model architecture is prescribed here.

For public-data reanalysis, inspect inclusion criteria, assay compatibility, batch structure, annotation quality, and leakage. Confirm whether a validation dataset is independent. Report effect sizes and uncertainty where appropriate, not just significance thresholds. For synthesis, preserve differences in organism, exposure, assay, and design instead of pooling incompatible findings.

## Adapt the generic prompts

Provide the organism/population, biological level, approved materials, study design, resources, timeline, and whether data collection is possible. Ask for an explicit distinction between observed results, proposed mechanisms, and speculation. Require a verification task for every accession, citation, and asserted mechanism. If ethics approval, essential metadata, or valid controls are missing, stop or redesign before making final recommendations.

## Completed example: public expression-data reanalysis

**Illustrative planning example; no dataset or result is asserted.**

Completed prompt:

> I am a Master's biology student with four months, basic R skills, and no wet-lab access. I want to study whether a stress-response expression signature is stable across two independently collected plant datasets. I do not yet have verified accession identifiers. Propose a feasibility checklist and a bounded question. Use conservative exploration. Do not invent repositories, sample sizes, genes, effect sizes, or citations. State what must be checked before analysis and which claims the design cannot support.

A bounded candidate is **“Cross-dataset stability of a prespecified stress-response gene signature in one plant species.”** First choose the species and stress definition, then find actual datasets with accessible raw or suitably processed data and sufficient metadata. The contribution, if supported by literature review, is an assessment of reproducibility under stated conditions rather than discovery of a new stress mechanism.

The plan needs a prespecified signature obtained from a verified source, independent datasets with compatible tissues and exposures, an accession/version log, and justified normalization. Batch and treatment must not be inseparable. If one dataset lacks a control or has confounded conditions, record that and narrow the analysis or reject it. Define the stability measure and uncertainty approach before examining the final comparison.

**Decision:** conditional; data availability and comparability remain unknown. **Next validation step:** manually verify two candidate dataset records, their files, reuse conditions, and sample annotations. **Evidence status:** planning only. Even a consistent signature would not prove causal regulation or usefulness in humans. A negative replication can still be informative when the comparison is valid.

## Review before proceeding

Are biological units clear? Are controls and permissions adequate? Can the source records be inspected? Are proposed mechanisms labeled as hypotheses? Does the conclusion match the organism and study design?
