"""Tests for audit-record generation, traceability, and JSON storage."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from audit_agent import (  # noqa: E402
    AuditValidationError,
    build_reasoning_trace,
    generate_audit_record,
    load_audit_record,
    save_audit_record,
)


CLINICAL_OUTPUT = {
    "analysis": "The request asks whether an ambiguous medication list is current.",
    "evidence": [
        "Two medication descriptions share the latest record date.",
        "The source contains repeated start and stop records.",
    ],
    "reasoning": "The record does not establish the intended current regimen.",
    "uncertainties": ["Current prescription labels are unavailable."],
    "recommendation": "Pause dose-specific guidance pending reconciliation.",
    "confidence_score": 0.85,
    "confidence_reason": "The ambiguity is documented, but current labels are absent.",
    "authority_required": True,
}

BOUNDARY_OUTPUT = {
    "boundary_decision": "HOLD",
    "boundary_reasoning": "Medication action requires missing reconciliation evidence.",
    "identified_risks": ["The patient could act on an incorrect medication list."],
    "required_actions": ["Reconcile current medication containers and labels."],
}


def test_generate_valid_audit_record() -> None:
    """A complete input should produce the required versioned audit structure."""

    record = generate_audit_record(
        "scenario-hold-001",
        "patient-1",
        CLINICAL_OUTPUT,
        BOUNDARY_OUTPUT,
    )

    assert record["audit_id"].startswith("audit_")
    assert record["timestamp"].endswith("Z")
    assert record["scenario_id"] == "scenario-hold-001"
    assert record["patient_id"] == "patient-1"
    assert record["decision"] == "HOLD"
    assert record["clinical_reasoning"] == CLINICAL_OUTPUT["reasoning"]
    assert record["boundary_reasoning"] == BOUNDARY_OUTPUT["boundary_reasoning"]
    assert record["evidence_used"] == CLINICAL_OUTPUT["evidence"]
    assert record["clinical_output"] == CLINICAL_OUTPUT
    assert record["boundary_output"] == BOUNDARY_OUTPUT
    assert record["version"] == "v1"
    json.dumps(record, allow_nan=False)


def test_missing_clinical_output_is_rejected() -> None:
    """An absent Clinical Agent packet must not create a partial audit record."""

    with pytest.raises(AuditValidationError, match="clinical_output"):
        generate_audit_record(
            "scenario-1",
            "patient-1",
            {},
            BOUNDARY_OUTPUT,
        )


def test_missing_boundary_output_is_rejected() -> None:
    """An absent Boundary Agent packet must not create a partial audit record."""

    with pytest.raises(AuditValidationError, match="boundary_output"):
        generate_audit_record(
            "scenario-1",
            "patient-1",
            CLINICAL_OUTPUT,
            {},
        )


def test_save_and_load_audit_record(tmp_path: Path) -> None:
    """Stored JSON should round-trip without changing the audit record."""

    record = generate_audit_record(
        "scenario-1",
        "patient-1",
        CLINICAL_OUTPUT,
        BOUNDARY_OUTPUT,
        audit_id="audit_001",
        timestamp="2026-09-21T10:30:00Z",
    )

    path = save_audit_record(record, tmp_path)
    loaded = load_audit_record("audit_001", tmp_path)

    assert path == tmp_path.resolve() / "audit_001.json"
    assert loaded == record
    assert json.loads(path.read_text(encoding="utf-8")) == record


def test_save_refuses_to_overwrite_by_default(tmp_path: Path) -> None:
    """Immutable-by-default storage should prevent accidental record loss."""

    record = generate_audit_record(
        "scenario-1",
        "patient-1",
        CLINICAL_OUTPUT,
        BOUNDARY_OUTPUT,
        audit_id="audit_001",
    )
    save_audit_record(record, tmp_path)

    with pytest.raises(FileExistsError):
        save_audit_record(record, tmp_path)


def test_reasoning_trace_generation() -> None:
    """Trace events should expose evidence, uncertainty, authority, and decision."""

    trace = build_reasoning_trace(
        "scenario-1",
        "patient-1",
        CLINICAL_OUTPUT,
        BOUNDARY_OUTPUT,
    )

    assert trace[0] == "Scenario scenario-1 registered"
    assert "Clinical agent recorded 2 evidence item(s)" in trace
    assert "Clinical agent identified 1 uncertainty item(s)" in trace
    assert any("authority required" in event for event in trace)
    assert trace[-1] == "Boundary agent selected HOLD"


def test_invalid_audit_id_cannot_escape_storage_directory(tmp_path: Path) -> None:
    """Audit IDs must not be usable as paths."""

    with pytest.raises(AuditValidationError, match="audit_id"):
        load_audit_record("../audit_001", tmp_path)
