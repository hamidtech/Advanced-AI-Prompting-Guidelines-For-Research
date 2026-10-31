#!/usr/bin/env python3
"""Create a randomized planning manifest. No network, model calls or scores."""
import argparse
import hashlib
import json
from pathlib import Path
import random


def build_plan(model, repetitions, seed):
    if repetitions < 1:
        raise ValueError("repetitions must be positive")
    if not model.strip():
        raise ValueError("model identifier must not be empty")
    source = Path(__file__).parent / "cases" / "scenarios.json"
    cases = json.loads(source.read_text(encoding="utf-8"))["cases"]
    rng = random.Random(seed)
    records = []
    for case in cases:
        for language in ("en", "fa"):
            for repetition in range(1, repetitions + 1):
                arms = ["legacy", "modern"]
                rng.shuffle(arms)
                for arm in arms:
                    records.append({
                        "run_id": f"{case['id']}-{language}-{repetition}-{arm}",
                        "case_id": case["id"], "language": language,
                        "repetition": repetition, "arm": arm,
                        "model_id": model, "status": "planned",
                        "modern_prompt_id": case["modern_prompt_id"],
                    })
    return {"manifest_version": "2.0.0", "seed": seed,
            "scenario_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "notice": "Planning only: no model executions or empirical results.",
            "runs": records}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True)
    parser.add_argument("--repetitions", type=int, default=3)
    parser.add_argument("--seed", type=int, default=20261031)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        plan = build_plan(args.model, args.repetitions, args.seed)
    except ValueError as error:
        parser.error(str(error))
    # Refuse accidental overwrite of a recorded plan or output.
    with args.output.open("x", encoding="utf-8") as handle:
        json.dump(plan, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"Planned {len(plan['runs'])} runs; executed 0 model calls.")


if __name__ == "__main__":
    main()
