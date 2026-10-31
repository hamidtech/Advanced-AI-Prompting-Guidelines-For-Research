# Optional automation

[فارسی](README.fa.md)

From the root with Python 3.11 or newer:

```bash
python -m pip install -r requirements-dev.txt
python automation/scripts/validate.py
python -m unittest discover -s automation/scripts -p 'test_*.py'
```

No network or credentials are needed after dependency installation. These checks are documentation and schema checks; they do not execute models or prove academic quality. Archived historical Markdown is exempt from modern lint/link rules but its bytes are checked against the base commit when history is present.

See [evaluation](../evaluation/README.md) for controlled runs. [Provider-neutral response handling](examples/structured-output.md) is intentionally not a live API integration.
