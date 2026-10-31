"""Semantic checks that JSON Schema cannot express portably."""
from collections import Counter
from pathlib import Path

DISCIPLINES = {'engineering', 'life-sciences', 'social-sciences', 'humanities', 'theology'}
CONDITIONS = {'no-topic', 'broad-interest', 'candidate-title', 'limited-resources',
              'incomplete-evidence', 'interdisciplinary'}

def evidence_errors(record):
    if not isinstance(record, dict):
        return ['Evidence record must be an object']
    source = record.get('source', {})
    fields = record.get('fields', {})
    if not isinstance(source, dict) or not isinstance(fields, dict):
        return ['Evidence source and fields must be objects']
    errors = []
    for name, field in fields.items():
        if not isinstance(field, dict):
            continue  # The JSON Schema reports this shape error.
        source_id = field.get('source_id')
        if source_id is not None and source_id != source.get('id'):
            errors.append(f'{name}: source_id does not identify the record source')
    return errors

def scenario_errors(document, root, metadata):
    if not isinstance(document, dict) or not isinstance(document.get('cases'), list):
        return ['Scenario collection must be an object containing a cases array']
    cases = document['cases']
    errors = []
    if len(cases) != 30:
        errors.append(f'Expected 30 evaluation cases, got {len(cases)}')
    ids = []
    pairs = Counter()
    inputs = {'en': set(), 'fa': set()}
    for case in cases:
        if not isinstance(case, dict):
            errors.append('Each evaluation case must be an object')
            continue
        ident = case.get('id')
        if isinstance(ident, str):
            ids.append(ident)
        pair = (case.get('discipline'), case.get('condition'))
        if all(isinstance(x, str) for x in pair):
            pairs[pair] += 1
        values = case.get('input', {})
        if isinstance(values, dict):
            for language in inputs:
                text = values.get(language)
                if isinstance(text, str):
                    normalized = ' '.join(text.split())
                    if normalized in inputs[language]:
                        errors.append(f'{ident}: duplicate {language} scenario input')
                    inputs[language].add(normalized)
        prompt_id = case.get('modern_prompt_id')
        if prompt_id not in metadata:
            errors.append(f'{ident}: unknown modern_prompt_id {prompt_id}')
        relative = case.get('modern_prompt_path')
        if isinstance(relative, str):
            path = (root / relative).resolve()
            if not path.is_relative_to(root.resolve()) or not path.is_file():
                errors.append(f'{ident}: nonexistent or unsafe modern_prompt_path')
            elif prompt_id in metadata:
                files = metadata[prompt_id].get('files', {})
                filename = files.get('en', '') if isinstance(files, dict) else ''
                expected = root / 'catalog/prompts' / (filename if isinstance(filename,str) else '')
                if path != expected.resolve():
                    errors.append(f'{ident}: prompt path and ID disagree')
    if len(ids) != len(set(ids)):
        errors.append('Evaluation case identifiers must be unique')
    for discipline in DISCIPLINES:
        for condition in CONDITIONS:
            if pairs[(discipline, condition)] != 1:
                errors.append(f'Expected one {discipline}/{condition} case')
    return errors
