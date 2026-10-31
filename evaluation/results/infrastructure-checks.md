# Infrastructure checks, 2026-10-31

These are software checks, not evaluations of model outputs.

Executed locally:

```bash
PYTHONPATH=/tmp/research-v2-deps python evaluation/test_infrastructure.py
```

Result: three unittest methods passed. Checks cover thirty schema-valid bilingual scenarios, unique case IDs, all six conditions in each of five disciplines, a deterministic 360-record plan, changed-seed scheduling, rejection of empty model identifiers and nonpositive repetitions, run-schema validity, valid unreviewed/rated/failed synthetic in-memory records, and eleven invalid record mutations. Synthetic records remain in test memory and are not published as empirical runs.

The JSON Schema `date-time` format is not reliably asserted when optional RFC3339 support is absent. A timestamp shape pattern additionally rejects obvious invalid strings; it does not establish that a timestamp corresponds to a real execution. Human provenance review remains necessary.

A CLI dry run also produced 360 planned records with zero model calls. No external model was invoked; no scholarly quality score, reviewer agreement, improvement estimate, citation error rate or latency measurement exists. [Empirical status](pending-status.json) remains pending.
