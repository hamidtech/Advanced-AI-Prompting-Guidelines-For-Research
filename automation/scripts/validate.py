#!/usr/bin/env python3
"""Offline repository contracts. Does not validate scientific truth or external URLs."""
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote
from jsonschema import Draft202012Validator, FormatChecker
from contracts import evidence_errors, scenario_errors

ROOT = Path(__file__).resolve().parents[2]
errors = []
counts = {}
def fail(message): errors.append(message)
def load(path):
    try: return json.loads(path.read_text())
    except (ValueError, UnicodeError) as e:
        fail(f'{path.relative_to(ROOT)}: {e}')
        return None

def check_instance(data, schema, label):
    for e in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(data):
        fail(f'{label}: {list(e.path)} {e.message}')

required = ['README.md','README.fa.md','ModernResearchPrompting.md','VERSION','LICENSE',
            'CONTRIBUTING.md','CHANGELOG.md','docs/audit-and-migration.md',
            'catalog/schemas/prompt-metadata.schema.json','catalog/schemas/workflow-metadata.schema.json',
            'catalog/schemas/evidence-record.schema.json','catalog/schemas/topic-candidate.schema.json',
            'evaluation/README.md','.github/workflows/validate.yml']
for name in required:
    if not (ROOT/name).is_file(): fail(f'Missing required file: {name}')
alljson = {}
for path in ROOT.rglob('*.json'):
    if '.git' in path.parts: continue
    data = load(path)
    if data is not None: alljson[path] = data
    if path.name.endswith('.schema.json') and data is not None:
        try: Draft202012Validator.check_schema(data)
        except Exception as e: fail(f'{path}: invalid schema: {e}')
ids = set()
metadata = {}
for directory, typ, expected in [('prompts','prompt',10),('workflows','workflow',4)]:
    schema = alljson.get(ROOT/f'catalog/schemas/{typ}-metadata.schema.json')
    paths = sorted((ROOT/f'catalog/{directory}').glob('*.json'))
    counts[directory] = len(paths)
    if len(paths) != expected: fail(f'{directory}: expected {expected}, got {len(paths)}')
    for path in paths:
        data = alljson.get(path)
        if not isinstance(data,dict): continue
        if schema: check_instance(data,schema,path.name)
        ident=data.get('id')
        if not isinstance(ident, str):
            fail(f'{path.name}: identifier must be a string'); continue
        if ident in ids: fail(f'Duplicate identifier: {ident}')
        ids.add(ident); metadata[ident]=data
        filemap=data.get('files',{})
        if not isinstance(filemap,dict):
            fail(f'{path.name}: files must be an object'); continue
        for lang in ('en','fa'):
            name=filemap.get(lang,'')
            expected_name=path.stem+('.fa.md' if lang=='fa' else '.md')
            if name != expected_name:
                fail(f'{path.name}: expected {lang} file {expected_name}')
            if not isinstance(name,str): continue
            dest=path.parent/name
            if not name or not dest.is_file(): fail(f'{path.name}: missing {lang} document')
            elif dest.stem.replace('.fa','') != path.stem: fail(f'{path.name}: inconsistent file pair')
    for path in paths:
        en=path.with_suffix('.md'); fa=path.with_name(path.stem+'.fa.md')
        if en.is_file() and fa.is_file():
            en_text=en.read_text();fa_text=fa.read_text()
            placeholders=lambda text:set(re.findall(r'\[([A-Z][A-Z0-9_]+)\]',text))
            if placeholders(en_text)!=placeholders(fa_text): fail(f'{path.name}: bilingual placeholder mismatch')
            if len(re.findall(r'^## ',en_text,re.M))<7 or len(re.findall(r'^## ',fa_text,re.M))<7:
                fail(f'{path.name}: incomplete bilingual section structure')
    for path in (ROOT/f'catalog/{directory}').glob('*.md'):
        if path.name.startswith('README'): continue
        if not path.with_name(path.name.replace('.fa.md','.md')).with_suffix('.json').exists():
            fail(f'{path}: orphan catalog document')
for ident, data in metadata.items():
    refs=([data['workflow_id']] if 'workflow_id' in data else data.get('prompt_ids',[]))
    if not isinstance(refs,list):
        fail(f'{ident}: references must be a list'); continue
    for ref in refs:
        if not isinstance(ref,str) or ref not in ids: fail(f'{ident}: missing reference {ref}')
for folder in ['docs/foundations','docs/disciplines','docs/integrity','docs/tools']:
    for path in (ROOT/folder).glob('*.md'):
        if path.name.endswith('.fa.md'):
            if not path.with_name(path.name.replace('.fa.md','.md')).is_file(): fail(f'Missing English pair: {path}')
        elif not path.with_name(path.stem+'.fa.md').exists(): fail(f'Missing Persian pair: {path}')
if len(list((ROOT/'docs/disciplines').glob('*.fa.md'))) != 5: fail('Expected five discipline pairs')
for filename,schemaname in [('evidence-record','evidence-record'),('topic-candidate','topic-candidate')]:
    instance=alljson.get(ROOT/f'examples/{filename}.json')
    schema=alljson.get(ROOT/f'catalog/schemas/{schemaname}.schema.json')
    if instance is not None and schema: check_instance(instance,schema,filename)
record=alljson.get(ROOT/'examples/evidence-record.json',{})
for error in evidence_errors(record): fail(error)
scenarios=alljson.get(ROOT/'evaluation/cases/scenarios.json')
if scenarios is not None:
    for error in scenario_errors(scenarios,ROOT,metadata): fail(error)
    counts['evaluation_cases']=len(scenarios.get('cases',[])) if isinstance(scenarios,dict) else 0
# Validate evaluation scenario/run fixtures using declared schemas when present.
for schema_path in (ROOT/'evaluation').rglob('*.schema.json'):
    schema=alljson.get(schema_path)
    if not schema: continue
    # Explicit fixtures; pending status is deliberately not an empirical run.
    target = {'scenario.schema.json': ROOT/'evaluation/cases/scenarios.json'}.get(schema_path.name)
    if target and target in alljson:
        value=alljson[target]
        if isinstance(value,list):
            for index,item in enumerate(value): check_instance(item,schema,f'scenario {index}')
        else: check_instance(value,schema,target.name)
run_schema=alljson.get(ROOT/'evaluation/results/run.schema.json')
if run_schema:
    for path,value in alljson.items():
        if path.is_relative_to(ROOT/'evaluation/results') and not path.name.endswith('.schema.json') and path.name!='pending-status.json':
            if isinstance(value,dict) and 'manifest_version' in value:
                continue  # A planning manifest is explicitly not a model execution.
            check_instance(value,run_schema,path.relative_to(ROOT).as_posix())
# Markdown syntax/targets. Archived files retain historical bytes and are exempt.
def anchors(text):
    found=set(); repeats={}
    for line in text.splitlines():
        match=re.match(r'^#{1,6}\s+(.+?)\s*#*$',line)
        if match:
            title=re.sub(r'<[^>]+>','',match.group(1)).lower()
            title=re.sub(r'[^\w\-\s\u200c]','',title).replace(' ','-')
            n=repeats.get(title,0); repeats[title]=n+1
            found.add(title+(f'-{n}' if n else ''))
    return found
mdpaths=[p for p in ROOT.rglob('*.md') if '.git' not in p.parts and 'legacy' not in p.relative_to(ROOT).parts]
counts['markdown']=len(mdpaths)
for path in mdpaths:
    content=path.read_text()
    fence=False
    lines=[]
    for number,line in enumerate(content.splitlines(),1):
        if line.startswith('```'):
            fence=not fence; continue
        if fence: continue
        lines.append(line)
        if line.rstrip()!=line: fail(f'{path.relative_to(ROOT)}:{number}: trailing whitespace')
        if re.match(r'^#{1,6}[^ #]',line): fail(f'{path}:{number}: malformed heading')
    if fence: fail(f'{path}: unclosed code fence')
    if not content.endswith('\n'): fail(f'{path}: no final newline')
    for dest in re.findall(r'\[[^\]\n]+\]\(([^)]+)\)', '\n'.join(lines)):
        dest=dest.strip('<>')
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',dest): continue
        target,_,fragment=dest.partition('#')
        resolved=(path.parent/unquote(target)).resolve() if target else path
        if not resolved.is_relative_to(ROOT): fail(f'{path}: link escapes repo: {dest}'); continue
        if not resolved.exists(): fail(f'{path.relative_to(ROOT)}: broken link {dest}')
        elif fragment and resolved.is_file() and resolved.suffix=='.md':
            if unquote(fragment) not in anchors(resolved.read_text()): fail(f'{path.relative_to(ROOT)}: missing anchor {dest}')
# Check archive bytes against original base without relying on current root wrappers.
for name in ['README.md','EnglishGuideline.md','PersianGuideline.md','ThesisSummaryPrompt.md','LICENSE']:
    path=ROOT/'legacy/2024-gpt-4o'/name
    if not path.exists(): fail(f'Missing archive: {name}'); continue
    result=subprocess.run(['git','show',f'59e3911:{name}'],cwd=ROOT,capture_output=True)
    if result.returncode==0 and path.read_bytes()!=result.stdout: fail(f'Archive altered: {name}')
if (ROOT/'VERSION').exists() and (ROOT/'VERSION').read_text().strip()!='2.0.0': fail('VERSION mismatch')
print(json.dumps({'counts':counts,'errors':errors,'status':'FAIL' if errors else 'PASS'},ensure_ascii=False,indent=2))
sys.exit(bool(errors))
