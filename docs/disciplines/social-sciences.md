# Social sciences and management research profile

[فارسی](social-sciences.fa.md) · Version 2.0.0 · Updated 2026-10-31

## Questions and contribution

Questions may concern organizational processes, meaning, experience, institutions, behavior, associations, or causal effects. Select an explanatory, interpretive, descriptive, evaluative, or critical purpose before choosing a method. A local replication, a refined concept, an account of organizational mechanisms, or a documented boundary condition may contribute without claiming universal novelty.

Do not automatically turn every management problem into a questionnaire and structural equation model. Interviews, observation, document analysis, administrative records, experiments, surveys, and mixed approaches serve different questions. An observational association is not automatically an intervention effect.

## Materials, constraints, and sources

Potential materials include interviews, field notes, surveys, policies, service records, organizational documents, or public discourse. Define the unit: employee, interaction, branch, document, or organization. Analyzing many records from one company does not make the company sample large.

Check gatekeeper permission, participant consent, employment power relations, access continuity, instrument permissions, and the risk of identifying people through quotations. The [UK Data Service guidance on text anonymisation](https://ukdataservice.ac.uk/learning-hub/data-producer-support/preparing-data-for-sharing-and-reuse/anonymising-data-and-protecting-participants/anonymisationfortextdata/) explains how rich narrative detail can identify individuals; removing names is insufficient protection. Reference accessed 2026-10-31.

Use original empirical studies for measured claims, primary organizational documents for documented procedures, appropriate statistical agencies for published statistics, and theoretical texts for conceptual arguments. Company publicity is evidence of what a company says, not independent verification of its effects. Distinguish participant testimony, administrative records, researcher interpretation, and AI inference.

## Method and verification

For surveys, justify sampling, construct definitions, instrument adaptation, missing-data handling, and the inferential scope. Translation and apparent fluency do not demonstrate measurement equivalence. For qualitative work, explain case selection, positionality, interpretive approach, coding decisions, and contradictory cases; do not mechanically require the same reliability statistic for all traditions.

For causal questions, articulate a plausible identification strategy and competing explanations. If the design cannot support causality, revise the question. For text mining, inspect selection bias, duplicates, changing terminology, annotation ambiguity, and the difference between statements and verified events. Human review remains necessary for consequential classifications.

## Adapt the generic prompts

State the decision context, stakeholders, access, theoretical orientation if known, unit of analysis, language, and constraints. Ask the model to offer both quantitative and qualitative routes when the question is still open. Require contribution claims to address existing theory or practice, not merely “this country has not been studied.” Protect dissenting and minority accounts when summarizing interviews.

## Completed example: service-rejection remarks

**Illustrative research design; no company findings or evaluation scores are reported.**

Completed prompt:

> I am an IT management Master's student with six months of authorized, de-identified service-rejection remarks and their existing reason labels. One remark may contain multiple reasons. I have three months and a service expert available for weekly review. Help me frame a study that improves the classification taxonomy. Use balanced exploration. Do not assume existing labels are ground truth, infer customer motives, or claim causal effects on service quality. Compare an interpretable human-assisted coding route with a text-classification route. Identify data and validation requirements.

A bounded question is **“How does an expert-reviewed multilabel reason taxonomy represent service-rejection remarks compared with the existing single-label taxonomy?”** The proposed contribution is a defensible taxonomy and an account of its coverage and ambiguity, subject to literature review. It is not a claim that automation improves customer satisfaction.

The plan retains each original remark, assigns a stable record identifier, and creates a documented normalized copy. Experts inspect a diverse development sample, draft definitions and inclusion/exclusion examples, allow multiple reasons, and record disagreements. Hold out a distinct evaluation sample; inspect duplicates before splitting. Evaluate legacy coverage and unsupported assignments separately from agreement with the proposed taxonomy. Use an explicit “insufficient information” label where warranted.

If only distinct remarks are retained, report taxonomy coverage over distinct text rather than operational prevalence over all service events. If one expert is available, document that independent expert agreement remains unmeasured. Never quote identifiable remarks in a public repository.

**Decision:** feasible for a bounded taxonomy study if access and review time are confirmed. **Next validation step:** inspect an authorized sample and establish a labeling protocol before model selection. **Evidence status:** proposed design; no measured improvement.

## Review before proceeding

Does the design answer the question? Are units and access explicit? Can participants be harmed or identified? Are causes distinguished from associations and interpretations? Are negative cases and unresolved disagreements retained?
