"""Negative tests: shape/provenance must fail when invalid, not just parse JSON."""
import copy
import json
import unittest
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from contracts import evidence_errors, scenario_errors
R=Path(__file__).resolve().parents[2]
class Contracts(unittest.TestCase):
    def setUp(self):
        self.schema=json.loads((R/'catalog/schemas/evidence-record.schema.json').read_text())
        self.validator=Draft202012Validator(self.schema,format_checker=FormatChecker())
        self.record=json.loads((R/'examples/evidence-record.json').read_text())
    def test_valid_fixture(self): self.validator.validate(self.record)
    def test_missing_cannot_contain_fabricated_value(self):
        self.record['fields']['effect_size']['value']='0.93'
        self.assertFalse(self.validator.is_valid(self.record))
    def test_reported_requires_locator(self):
        self.record['fields']['sample'].update(page=None,section=None)
        self.assertFalse(self.validator.is_valid(self.record))
    def test_inference_requires_explanation(self):
        self.record['fields']['generalizability']['note']=''
        self.assertFalse(self.validator.is_valid(self.record))
    def test_unknown_fields_rejected(self):
        self.record['unreviewed_extra']='claim'
        self.assertFalse(self.validator.is_valid(self.record))
    def test_prompt_identifier_and_language(self):
        schema=json.loads((R/'catalog/schemas/prompt-metadata.schema.json').read_text())
        validator=Draft202012Validator(schema)
        for path in (R/'catalog/prompts').glob('*.json'):
            value=json.loads(path.read_text()); validator.validate(value)
            bad=copy.deepcopy(value);bad['languages']=['en'];self.assertFalse(validator.is_valid(bad))
            bad=copy.deepcopy(value);bad['id']='freeform';self.assertFalse(validator.is_valid(bad))
    def test_checked_evidence_requires_reviewer(self):
        self.record['verification'].update(status='checked',reviewer=None)
        self.assertFalse(self.validator.is_valid(self.record))
    def test_evidence_source_id_must_match(self):
        self.record['fields']['sample']['source_id']='OTHER'
        self.assertTrue(evidence_errors(self.record))
    def test_scenario_semantics(self):
        scenarios=json.loads((R/'evaluation/cases/scenarios.json').read_text())
        metadata={}
        for path in (R/'catalog/prompts').glob('*.json'):
            record=json.loads(path.read_text());metadata[record['id']]=record
        self.assertEqual(scenario_errors(scenarios,R,metadata),[])
        duplicated=copy.deepcopy(scenarios)
        duplicated['cases'][1]=copy.deepcopy(duplicated['cases'][0])
        errors=scenario_errors(duplicated,R,metadata)
        self.assertTrue(any('identifiers' in e for e in errors))
        self.assertTrue(any('Expected one' in e for e in errors))
        wrong_path=copy.deepcopy(scenarios)
        wrong_path['cases'][0]['modern_prompt_path']='LICENSE'
        self.assertTrue(any('disagree' in e for e in scenario_errors(wrong_path,R,metadata)))
        self.assertTrue(scenario_errors([],R,metadata))
    def test_scenario_schema_rejects_missing_translation(self):
        schema=json.loads((R/'evaluation/cases/scenario.schema.json').read_text())
        scenarios=json.loads((R/'evaluation/cases/scenarios.json').read_text())
        del scenarios['cases'][0]['input']['fa']
        self.assertFalse(Draft202012Validator(schema).is_valid(scenarios))
class RepositoryFailures(unittest.TestCase):
    def check_mutation(self, mutate, expected):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)/'repo'
            shutil.copytree(R,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
            mutate(root)
            result=subprocess.run([sys.executable,str(root/'automation/scripts/validate.py')],capture_output=True,text=True)
            self.assertEqual(result.returncode,1,result.stderr)
            report=json.loads(result.stdout)
            self.assertEqual(report['status'],'FAIL')
            self.assertTrue(any(expected in error for error in report['errors']),report)
    def test_broken_internal_link_fails(self):
        def mutate(root):
            with (root/'README.md').open('a') as handle:handle.write('\n[Broken](does-not-exist.md)\n')
        self.check_mutation(mutate,'broken link does-not-exist.md')
    def test_missing_translation_fails(self):
        self.check_mutation(lambda root:(root/'catalog/prompts/title-refiner.fa.md').unlink(),'missing fa document')
    def test_malformed_metadata_reports_failure_without_crash(self):
        def mutate(root):
            path=root/'catalog/prompts/interest-discovery.json'
            value=json.loads(path.read_text());value['files']=[];path.write_text(json.dumps(value))
        self.check_mutation(mutate,'files must be an object')
    def test_duplicate_identifier_fails(self):
        def mutate(root):
            path=root/'catalog/prompts/title-refiner.json'
            value=json.loads(path.read_text());value['id']='RP-01';path.write_text(json.dumps(value))
        self.check_mutation(mutate,'Duplicate identifier')
if __name__=='__main__': unittest.main()
