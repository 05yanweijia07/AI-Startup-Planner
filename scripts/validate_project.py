#!/usr/bin/env python3
"""Run structural checks for the local AI Startup Planner source package."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SCHEMAS = {
    "project-profile.schema.json",
    "project-state.schema.json",
    "decision-log.schema.json",
    "evidence-registry.schema.json",
    "assumption-registry.schema.json",
    "dependency-graph.schema.json",
    "deliverable-registry.schema.json",
    "version-history.schema.json",
}
EXPECTED_FIXTURES = {
    "project-profile.json": "project-profile.schema.json",
    "project-state.json": "project-state.schema.json",
    "decision-log.json": "decision-log.schema.json",
    "evidence-registry.json": "evidence-registry.schema.json",
    "assumption-registry.json": "assumption-registry.schema.json",
    "dependency-graph.json": "dependency-graph.schema.json",
    "deliverable-registry.json": "deliverable-registry.schema.json",
    "version-history.json": "version-history.schema.json",
}


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def fail(message: str) -> None:
    raise ValueError(message)


def check_skill_frontmatter() -> None:
    content = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = content.find("\n---\n", 4)
    if end < 0:
        fail("SKILL.md frontmatter closing delimiter is missing")
    metadata = yaml.safe_load(content[4:end])
    if not isinstance(metadata, dict) or not metadata.get("name") or not metadata.get("description"):
        fail("SKILL.md frontmatter must define name and description")
    if metadata["name"] != "ai-startup-planner":
        fail("SKILL.md name does not match the registered skill ID")


def check_manifests() -> int:
    skill_manifest = load_yaml(ROOT / "manifest" / "skill-manifest.yaml")
    module_registry = load_yaml(ROOT / "manifest" / "module-registry.yaml")
    tool_registry = load_yaml(ROOT / "manifest" / "tool-registry.yaml")

    if skill_manifest["registries"]["modules"] != "manifest/module-registry.yaml":
        fail("skill manifest module registry path is inconsistent")
    if skill_manifest["registries"]["tools"] != "manifest/tool-registry.yaml":
        fail("skill manifest tool registry path is inconsistent")
    for adapter_path in skill_manifest.get("web_app_adapters", []):
        if not (ROOT / adapter_path).is_file():
            fail(f"skill manifest points to missing adapter: {adapter_path}")

    modules = module_registry["modules"]
    tools = tool_registry["tools"]
    module_ids = [item["module_id"] for item in modules]
    tool_ids = [item["tool_id"] for item in tools]
    if len(module_ids) != len(set(module_ids)):
        fail("module registry contains duplicate module IDs")
    if len(tool_ids) != len(set(tool_ids)):
        fail("tool registry contains duplicate tool IDs")

    allowed_priority = {"MANDATORY", "RECOMMENDED", "OPTIONAL", "EXCLUDED"}
    for module in modules:
        if module["default_priority"] not in allowed_priority:
            fail(f"{module['module_id']} has an unknown priority")
        if module["loading_level"] not in {"L0", "L1", "L2", "L3"}:
            fail(f"{module['module_id']} has an unknown loading level")
        for reference in module.get("references", []):
            path = ROOT / reference
            if not path.exists():
                fail(f"{module['module_id']} points to missing path: {reference}")

    allowed_permissions = {"read_only", "local_write", "external_write", "destructive"}
    for tool in tools:
        if tool["permission"] not in allowed_permissions:
            fail(f"{tool['tool_id']} has an unknown permission class")
        if tool["availability"] != "platform_dependent":
            fail(f"{tool['tool_id']} incorrectly implies runtime availability")

    return len(modules) + len(tools)


def check_schemas_and_fixtures() -> int:
    schema_dir = ROOT / "schemas"
    actual_schemas = {path.name for path in schema_dir.glob("*.json")}
    if actual_schemas != EXPECTED_SCHEMAS:
        fail(f"schema set mismatch; expected {sorted(EXPECTED_SCHEMAS)}, found {sorted(actual_schemas)}")

    fixture_dir = ROOT / "tests" / "fixtures" / "synthetic-project"
    for fixture_name, schema_name in EXPECTED_FIXTURES.items():
        schema = json.loads((schema_dir / schema_name).read_text(encoding="utf-8"))
        instance = json.loads((fixture_dir / fixture_name).read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(Draft202012Validator(schema).iter_errors(instance))
        if errors:
            fail(f"{fixture_name} fails {schema_name}: {errors[0].message}")

    project_ids = {
        json.loads((fixture_dir / name).read_text(encoding="utf-8"))["project_id"]
        for name in EXPECTED_FIXTURES
    }
    if len(project_ids) != 1:
        fail("synthetic fixtures do not share one project_id")
    return len(EXPECTED_FIXTURES)


def check_required_test_docs() -> int:
    required = [
        ROOT / "tests" / "routing" / "routing-scenarios.md",
        ROOT / "tests" / "state-management" / "state-scenarios.md",
        ROOT / "tests" / "financial" / "financial-scenarios.md",
        ROOT / "tests" / "conflict-resolution" / "conflict-scenarios.md",
        ROOT / "tests" / "end-to-end" / "synthetic-project-scenario.md",
        ROOT / "tests" / "adapter-compatibility" / "doubao-deepseek-webapp.md",
        ROOT / "tests" / "RESULTS.md",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        fail(f"required test documentation missing: {missing}")
    return len(required)


def main() -> int:
    try:
        check_skill_frontmatter()
        registry_items = check_manifests()
        fixture_count = check_schemas_and_fixtures()
        test_docs = check_required_test_docs()
    except (OSError, KeyError, TypeError, ValueError, yaml.YAMLError) as error:
        print(f"FAIL: {error}")
        return 1

    print("PASS: Skill metadata and three YAML manifests are consistent")
    print(f"PASS: {registry_items} module/tool entries and all referenced paths are valid")
    print(f"PASS: {fixture_count} schema examples validate and share one project ID")
    print(f"PASS: {test_docs} required test documents are present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
