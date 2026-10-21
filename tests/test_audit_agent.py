"""Tests for audit-record generation, traceability, and JSON storage."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from audit_agent import (
    AuditValidationError,
    ProhibitedTransitionError,
    UnresolvedEvidenceError,
    apply_human_review,
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


def test_apply_human_review_updates_audit_and_ghostlog(tmp_path: Path) -> None:
    """Human review should record clinician approval and stamp onto the Recon GhostLog."""

    escalate_boundary = {
        "boundary_decision": "ESCALATE",
        "boundary_reasoning": "Dose adjustment requires qualified provider oversight.",
        "identified_risks": ["Dose escalation requires monitoring."],
        "required_actions": ["Physician review and validation."],
    }
    record = generate_audit_record(
        "scenario-esc-001",
        "patient-1",
        CLINICAL_OUTPUT,
        escalate_boundary,
        audit_id="audit_rev_001",
        recon_ghostlog=[{"step": 1, "kind": "recon_init", "data": {}}],
    )
    save_audit_record(record, tmp_path)

    updated = apply_human_review(
        "audit_rev_001",
        reviewer_name="Dr. Sarah Connor",
        reviewer_role="Attending Cardiologist",
        review_decision="APPROVED",
        review_notes="Approved with caution; dose verified.",
        audit_directory=tmp_path,
    )

    # Invariant 4: Original decision remains immutable
    assert updated["decision"] == "ESCALATE"
    assert updated["human_review"]["decision"] == "APPROVED"
    assert updated["human_review"]["reviewer_name"] == "Dr. Sarah Connor"
    assert updated["human_review"]["reviewer_role"] == "Attending Cardiologist"
    assert updated["human_review"]["carriesExecutionAuthority"] is False
    assert updated["human_review"]["executionAuthorityTransferredToAI"] is False
    assert (
        updated["human_review"]["approvalAuthorityHolder"]
        == "Dr. Sarah Connor (Attending Cardiologist)"
    )
    assert "executionAuthorityHolder" not in updated["human_review"]
    assert "human_review_signoff" in [
        entry["kind"] for entry in updated["recon_ghostlog"]
    ]
    assert any("Human Review APPROVED" in trace for trace in updated["reasoning_trace"])
    loaded = load_audit_record("audit_rev_001", tmp_path)
    assert loaded["human_review"] == updated["human_review"]


def test_apply_human_review_rejects_approval_on_hold(tmp_path: Path) -> None:
    """Approval on a HOLD audit record must be rejected while evidence is unresolved."""

    record = generate_audit_record(
        "scenario-hold-001",
        "patient-1",
        CLINICAL_OUTPUT,
        BOUNDARY_OUTPUT,  # boundary_decision is HOLD
        audit_id="audit_hold_001",
    )
    save_audit_record(record, tmp_path)

    with pytest.raises(UnresolvedEvidenceError, match="unresolved evidence deficit"):
        apply_human_review(
            "audit_hold_001",
            reviewer_name="Dr. Sarah Connor",
            reviewer_role="Attending Cardiologist",
            review_decision="APPROVED",
            audit_directory=tmp_path,
        )

    # Information requests (REQUEST_INFO) remain permitted without clearing deficit
    updated = apply_human_review(
        "audit_hold_001",
        reviewer_name="Dr. Sarah Connor",
        reviewer_role="Attending Cardiologist",
        review_decision="REQUEST_INFO",
        audit_directory=tmp_path,
    )
    assert updated["decision"] == "HOLD"
    assert updated["human_review"]["decision"] == "REQUEST_INFO"


def test_apply_human_review_rejects_transitions_on_stop(tmp_path: Path) -> None:
    """STOP audit records represent hard safety boundaries and cannot receive review transitions."""

    stop_boundary = {
        "boundary_decision": "STOP",
        "boundary_reasoning": "Patient presents with acute chest pain emergency.",
        "identified_risks": ["Life-threatening cardiac emergency."],
        "required_actions": ["Direct patient to emergency medical services (911)."],
    }
    record = generate_audit_record(
        "scenario-stop-001",
        "patient-1",
        CLINICAL_OUTPUT,
        stop_boundary,
        audit_id="audit_stop_001",
    )
    save_audit_record(record, tmp_path)

    with pytest.raises(ProhibitedTransitionError, match="Prohibited state transition"):
        apply_human_review(
            "audit_stop_001",
            reviewer_name="Dr. Sarah Connor",
            reviewer_role="Attending Cardiologist",
            review_decision="APPROVED",
            audit_directory=tmp_path,
        )

    # Disk record remains unmutated
    loaded = load_audit_record("audit_stop_001", tmp_path)
    assert "human_review" not in loaded
