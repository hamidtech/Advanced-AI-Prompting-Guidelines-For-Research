#!/usr/bin/env python3
"""Infrastructure tests only. Synthetic fixtures below are never model results."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).parent


class InfrastructureTests(unittest.TestCase):
    def test_case_coverage(self):
        from collections import Counter
        cases = json.loads((ROOT / "cases/scenarios.json").read_text(encoding="utf-8"))
        schema = json.loads((ROOT / "cases/scenario.schema.json").read_text())
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema, format_checker=FormatChecker()).validate(cases)
        rows = cases["cases"]
        self.assertEqual(len(rows), len({row["id"] for row in rows}))
        self.assertEqual(set(Counter(row["discipline"] for row in rows).values()), {6})
        self.assertEqual(set(Counter(row["condition"] for row in rows).values()), {5})
        for discipline in {row["discipline"] for row in rows}:
            self.assertEqual(len({r["condition"] for r in rows if r["discipline"] == discipline}), 6)

    def test_planner(self):
        spec = importlib.util.spec_from_file_location("planner", ROOT / "plan_runs.py")
        planner = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(planner)
        plan = planner.build_plan("TEST_ONLY_NOT_EXECUTED", 3, 42)
        self.assertEqual(len(plan["runs"]), 360)
        self.assertEqual(len({r["run_id"] for r in plan["runs"]}), 360)
        self.assertTrue(all(r["status"] == "planned" for r in plan["runs"]))
        self.assertEqual(plan, planner.build_plan("TEST_ONLY_NOT_EXECUTED", 3, 42))
        self.assertNotEqual(plan, planner.build_plan("TEST_ONLY_NOT_EXECUTED", 3, 43))
        for repetitions in (0, -1):
            with self.assertRaises(ValueError):
                planner.build_plan("TEST_ONLY", repetitions, 42)
        with self.assertRaises(ValueError):
            planner.build_plan(" ", 1, 42)

    def test_run_record_validation(self):
        schema = json.loads((ROOT / "results/run.schema.json").read_text())
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        # In-memory schema fixture: not persisted as empirical evidence.
        record = {
            "run_id": "SCHEMA_TEST_NOT_AN_EXECUTION", "case_id": "engineering-01",
            "language": "en", "arm": "modern", "repetition": 1,
            "repository_commit": "a" * 40, "prompt_sha256": "b" * 64,
            "scenario_sha256": "c" * 64, "evidence_packet_sha256": None,
            "model_id": "SCHEMA_TEST", "provider": "SCHEMA_TEST",
            "executed_at": "2026-10-31T00:00:00Z", "configuration": {},
            "status": "completed", "raw_output_sha256": "d" * 64,
            "scores": dict.fromkeys(("relevance", "feasibility", "specificity",
                                     "evidence_grounding", "contribution", "clarity")),
            "unsupported_claims": None, "citation_errors": None,
            "review_notes": "Synthetic validation fixture; no model execution.",
            "artifact_locations": dict.fromkeys(("rendered_prompt", "binding_map", "source_packet", "raw_output")),
            "reviewer": None, "integrity_flags": [],
        }
        record["artifact_locations"].update(rendered_prompt="fixture/prompt.txt", binding_map="fixture/bindings.json", raw_output="fixture/output.txt")
        validator.validate(record)
        invalid_mutations = [
            lambda r: r.update(language="de"),
            lambda r: r.update(status="planned"),
            lambda r: r.update(raw_output_sha256=None),
            lambda r: r.update(executed_at="yesterday"),
            lambda r: r.update(repository_commit="main"),
            lambda r: r["scores"].update(feasibility=5),
            lambda r: r["scores"].update(feasibility=3),  # No reviewer means unreviewed.
            lambda r: r.update(citation_errors=-1),
            lambda r: r.update(unknown_field=True),
            lambda r: r["artifact_locations"].update(raw_output=None),
            lambda r: r.pop("model_id"),
        ]
        for mutation in invalid_mutations:
            broken = copy.deepcopy(record)
            mutation(broken)
            self.assertTrue(list(validator.iter_errors(broken)), mutation)
        rated = copy.deepcopy(record)
        rated.update(reviewer={"pseudonym": "R1", "expertise": "Test only",
                               "independent": False, "blinded": False})
        rated["scores"]["clarity"] = 3
        validator.validate(rated)
        failed = copy.deepcopy(record)
        failed.update(status="failed", raw_output_sha256=None)
        validator.validate(failed)


if __name__ == "__main__":
    unittest.main()
