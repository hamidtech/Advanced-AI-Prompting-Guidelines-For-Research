# Engineering research profile

[فارسی](engineering.fa.md) · Version 2.0.0 · Updated 2026-10-31

## Questions and contribution

Engineering work can investigate performance, reliability, safety, mechanisms, design trade-offs, or the conditions under which an established method fails. A contribution might be a well-characterized design, an independently reproduced result, a negative result, a dataset, or a deployment constraint. A new algorithm name or a higher score on one convenient split does not establish useful novelty.

Ask whether the target is prediction, explanation, optimization, measurement, or system design. Keep those purposes distinct. An optimization result depends on the objective and constraints; prediction accuracy alone does not establish a physical explanation.

## Materials, constraints, and evidence

Possible materials include sensor logs, drawings, simulations, laboratory measurements, maintenance records, code, and standards. Record units, calibration, sampling frequency, missingness, equipment limits, and provenance. Obtain authorization before sending plant data, intellectual property, or security-sensitive diagrams to an external model.

Use original experimental papers, technical reports with accessible methods, manufacturer documentation for equipment specifications, and applicable standards for requirements. A manufacturer claim is not independent evidence of comparative performance. Check the standard edition and local applicability. The [NIST measurement-process handbook](https://www.nist.gov/publications/nistsematech-engineering-statistics-handbook-chapter-2-measurement-process) addresses calibration, repeatability, reproducibility, stability, and uncertainty; use it to build a measurement checklist rather than to certify a new experiment. Reference accessed 2026-10-31.

## Method and verification

- For predictive models, define the deployment population, separate development from final evaluation, and split by time, device, or site where the deployment question requires it. Prevent repeated observations from leaking across splits.
- For simulation, distinguish numerical verification from empirical validation. Record solver, boundary conditions, assumptions, convergence criteria, and sensitivity analyses.
- For physical experiments, plan controls, repetitions, calibration, uncertainty reporting, and an appropriate safety review with a qualified supervisor.
- Compare against a credible simple baseline and the current operational procedure. Specify failure costs and resource use, not only an aggregate score.

AI may draft code or propose test conditions. A domain expert must check dimensional consistency, boundary cases, unsafe operating conditions, and whether the proposed measurement is possible. Never treat a simulation output or model-generated table as a real measurement.

## Adapt the generic prompts

Add system boundaries, operating range, available equipment, budget, data permissions, and the metric that changes a real decision. Permit “not currently feasible” and replication as useful outcomes. Require each proposed topic to identify a baseline, an experiment or validation route, and the strongest alternative explanation. For safety-critical work, require review before physical execution; a language model cannot approve operation.

## Completed example: a bounded design decision

**Illustrative planning example; no experiment has been run.**

Completed prompt:

> I am a Master's student in mechanical engineering with 12 weeks and permission to use anonymized hourly temperature and electrical-load records from three noncritical pumps. I cannot collect fault labels or alter pump operation. Propose three researchable questions about anomaly detection. Use balanced exploration. Distinguish unusual observations from diagnosed faults. For each question state required fields, a simple baseline, a temporal evaluation plan, failure costs, and what evidence would invalidate the proposal. Do not claim novelty or invent performance.

One defensible candidate is: **“Stability of pump-load anomaly alerts under seasonal operating shifts.”** The problem is whether an alert threshold calibrated during one operating period remains useful in another. A possible contribution is a documented failure boundary, conditional on literature review. Required resources are authorized logs, timestamps, an operating-period definition, and an engineer who can assess a small alert sample. Candidate methods are a rolling robust threshold and a simple statistical baseline; an elaborate deep model is optional rather than presumed necessary.

A workable plan checks timestamp quality first, reserves the latest period for evaluation, and compares alert rate and engineer-reviewed alert usefulness. Without validated fault labels, it must not report fault-detection recall. If operating context is absent, conclusions are restricted to statistical alert behavior. If three pumps share the same site, the study cannot establish generalization to other sites.

**Decision:** provisionally feasible for a methods comparison, pending data inspection and literature search. **Next validation step:** inspect one authorized week, establish units and missingness, and search for studies on distribution shift in industrial anomaly detection. **Evidence status:** proposed; no empirical performance or verified novelty.

## Review before proceeding

Can another engineer reproduce the setup? Are units and constraints explicit? Does the evaluation match deployment? Are safety and permissions resolved? Is the claimed contribution bounded by what was actually measured?
