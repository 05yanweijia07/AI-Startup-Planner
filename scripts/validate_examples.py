#!/usr/bin/env python3
"""Validate synthetic project fixtures against schemas and cross-file references."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "synthetic-project"

PAIRS = {
    "project-profile.json": "project-profile.schema.json",
    "project-state.json": "project-state.schema.json",
    "decision-log.json": "decision-log.schema.json",
    "evidence-registry.json": "evidence-registry.schema.json",
    "assumption-registry.json": "assumption-registry.schema.json",
    "dependency-graph.json": "dependency-graph.schema.json",
    "deliverable-registry.json": "deliverable-registry.schema.json",
    "version-history.json": "version-history.schema.json",
}


def read_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def main() -> int:
    errors: list[str] = []
    documents: dict[str, dict[str, Any]] = {}

    for fixture_name, schema_name in PAIRS.items():
        fixture_path = FIXTURE_DIR / fixture_name
        schema_path = SCHEMA_DIR / schema_name
        try:
            schema = read_json(schema_path)
            document = read_json(fixture_path)
            Draft202012Validator.check_schema(schema)
            validator = Draft202012Validator(schema, format_checker=FormatChecker())
            for error in validator.iter_errors(document):
                location = "/".join(str(part) for part in error.absolute_path) or "<root>"
                errors.append(f"{fixture_name} at {location}: {error.message}")
            documents[fixture_name] = document
        except (OSError, json.JSONDecodeError, ValueError) as error:
            errors.append(f"{fixture_name}: {error}")

    if not errors:
        profile = documents["project-profile.json"]
        project_id = profile["project_id"]
        for name, document in documents.items():
            if document.get("project_id") != project_id:
                errors.append(f"{name}: project_id does not match project-profile.json")

        decisions = {item["decision_id"] for item in documents["decision-log.json"]["decisions"]}
        evidence = {item["evidence_id"] for item in documents["evidence-registry.json"]["evidence"]}
        assumptions = {item["assumption_id"] for item in documents["assumption-registry.json"]["assumptions"]}
        graph_nodes = {item["node_id"] for item in documents["dependency-graph.json"]["nodes"]}

        state = documents["project-state.json"]
        for gate, gate_data in state["gate_statuses"].items():
            for ref in gate_data["evidence_refs"]:
                if ref not in evidence:
                    errors.append(f"project-state.json {gate}: unknown evidence ref {ref}")
            decision_ref = gate_data.get("decision_ref")
            if decision_ref is not None and decision_ref not in decisions:
                errors.append(f"project-state.json {gate}: unknown decision ref {decision_ref}")

        for decision in documents["decision-log.json"]["decisions"]:
            for ref in decision["evidence_refs"]:
                if ref not in evidence:
                    errors.append(f"decision-log.json {decision['decision_id']}: unknown evidence ref {ref}")

        for assumption in documents["assumption-registry.json"]["assumptions"]:
            for ref in assumption["evidence_refs"]:
                if ref not in evidence:
                    errors.append(f"assumption-registry.json {assumption['assumption_id']}: unknown evidence ref {ref}")

        graph = documents["dependency-graph.json"]
        for edge in graph["edges"]:
            if edge["from"] not in graph_nodes or edge["to"] not in graph_nodes:
                errors.append(f"dependency-graph.json: edge endpoint missing ({edge['from']} -> {edge['to']})")

        for deliverable in documents["deliverable-registry.json"]["deliverables"]:
            for ref in deliverable["assumption_refs"]:
                if ref not in assumptions:
                    errors.append(f"deliverable-registry.json {deliverable['deliverable_id']}: unknown assumption ref {ref}")

    if errors:
        print("FAIL: example validation found issues")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: {len(PAIRS)} schemas and synthetic fixture documents validated")
    print("PASS: project IDs and checked evidence, decision, assumption, and graph references are consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
