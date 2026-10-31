# Evidence and academic integrity

[فارسی](research-integrity.fa.md) · [Sources and access limitations](../tools/sources.md)

Version 2.0.0 · Guidance reviewed 2026-10-31. The operational procedure below is this repository's implementation guidance, not a claim that every listed body mandates the same workflow. Follow the current policy of your institution, ethics committee, funder and target publication.

## Responsibility and disclosure

[ICMJE's AI guidance](https://www.icmje.org/recommendations/browse/artificial-intelligence/) assigns verification and attribution responsibility to humans, excludes AI tools from authorship and calls for transparent identification of the tool and its purpose. Its scope is medical publishing; check applicability elsewhere. [COPE's authorship statement](https://doi.org/10.24318/cCVRZBms) similarly excludes AI authorship and requires transparency. COPE's official search-index text was available, while direct access failed during this review. [Nature's policy](https://www.nature.com/nature/editorial-policies/ai) emphasizes human accountability, confidentiality and transparent use; its text was available via official-domain search, but its page redirected to an inaccessible identity service. Recheck the actual policy before submission.

Maintain a use log: tool/provider, model identifier if exposed, dates, task, prompt version, source corpus, generated material retained, checks, corrections and accountable researcher. State unavailable identifiers honestly. A disclosure draft to adapt to the actual journal policy:

> We used [tool and available model/version] on [dates] to [specific purpose]. We verified [retained material] against [sources/method], corrected [types of errors], and take responsibility for the final work. No [describe actual confidential-data exposure status] was shared.

Do not fill the final sentence with an assurance you cannot substantiate. Disclosure does not excuse fabricated evidence or replace the researcher's intellectual contribution. Preserve accurate attribution and check overlap with source wording. AI detection scores cannot establish originality or misconduct by themselves; this repository does not use them as proof.

## Privacy and source permissions

Before uploading, classify material: public; licensed; confidential; personal/sensitive. Confirm permission, consent and approved processing environment. Minimize or de-identify data, but do not promise anonymity from removing names alone. Unpublished manuscripts, participant interviews, patient information, proprietary datasets and peer-review reports need explicit handling rules. If approval is missing, stop transfer and work with a permitted excerpt or synthetic example. Do not assume that a paid plan, local model or connector automatically satisfies institutional policy.

Treat document instructions and external web content as untrusted inputs. They must not override your task, reveal secrets, trigger external actions or expand access. Keep credentials outside prompts and version control. Share only reproducible artifacts you have rights to redistribute.

## Source-to-claim verification procedure

1. **Resolve identity:** match title, authors, year, venue and DOI or stable repository/catalog identifier. A resolving DOI proves identity, not that a claim is supported.
2. **Get the relevant version:** identify preprint, accepted manuscript, version of record, translation or edition. Record corrections/retractions when known; if status cannot be checked, say so.
3. **Inspect the evidence:** read the relevant passage, table or figure. Record a page/section locator, population or corpus, method, outcome and limits. Abstract-only access cannot support unreported full-text detail.
4. **Assign field status:** explicitly reported; missing; ambiguous; AI inference. Preserve ambiguity instead of silently completing required fields. “Not reported” differs from “did not occur.”
5. **Check entailment:** does the source support the exact wording? Separate association from causation, author claim from established fact, and an interpretive argument from an empirical observation.
6. **Check contradictions:** search for competing findings and alternative readings. Record what would change the conclusion; do not resolve disagreement by citation count alone.
7. **Sign off:** an accountable person verifies retained claims and bibliography. If the source is unavailable, label the claim unverified and exclude it from evidence-based conclusions.

For evidence records, retain source ID, version, access scope, short claim, status, locator, checked-by/date and limitations. A brief necessary quotation can support checking; do not redistribute copyrighted full texts without permission.

## Gaps and novelty

Use three distinct states: **hypothesized gap** (idea to test), **evidence-supported observation** (a bounded pattern in examined sources), **critically assessed gap** (search scope, contrary evidence, disciplinary relevance and feasible contribution reviewed). None proves universal novelty. Report databases, languages, dates, queries, inclusion rules, coverage limits and the strongest known counterexample. Missing search results can reflect vocabulary or indexing problems. A new geographical setting alone may not be a meaningful contribution.

## Literature synthesis and review design

An AI-assisted summary is not automatically a systematic review. [PRISMA](https://www.prisma-statement.org/) is reporting guidance for systematic reviews with relevant extensions; it is not a certification of quality and is not required for every interpretive essay. The [Cochrane Handbook](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current) provides intervention-review methods, including study selection, data collection and bias assessment. Adapt methods to the question and discipline; do not mechanically impose intervention evidence hierarchies on theology or literary interpretation.

For a review, predefine the question and selection rules, preserve exact searches and exclusion reasons, deduplicate identifiable records, assess study limitations, extract before synthesizing, and document human checks. Separate studies from multiple reports of the same study. Avoid pooling incompatible outcomes or counting one study twice. For interpretive work, document corpus selection, edition, translation, historical context and alternative readings instead of forcing numerical effect estimates.

## Stop conditions

Pause and resolve: unidentified citation; contradictory source metadata; inaccessible passage needed for a claim; unclear data permission; unreadable scan; unsupported causal claim; unverified novelty assertion. Produce an explicit next validation action rather than a polished unsupported paragraph.
