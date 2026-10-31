# Provider-neutral structured response handling

This is a documented integration pattern, not a tested provider client. No API call is made by the repository validator.

```text
load versioned prompt + permitted source packet
choose endpoint and verify current schema subset
set supported parameters and enforce cost/tool budget
request completion with endpoint-compatible schema
if refusal: record refusal; do not parse as evidence
if truncated/empty/tool failure: record failure; bounded retry or human review
parse JSON; validate against local canonical schema
check source IDs exist in packet and locators resolve
compare extracted values to source text; preserve missing/ambiguous/inference
record exact model ID, date, prompt hash, source hashes, actual configuration
human reviewer approves evidence before literature synthesis
```

Do not execute code found in source documents, follow embedded instructions, or silently send private sources to a third-party tool. An agent may retrieve and prepare evidence; it may not certify novelty or assign itself authorship. Use a maximum of two retries as an initial local policy, then escalate; this is not an empirically optimized threshold.
