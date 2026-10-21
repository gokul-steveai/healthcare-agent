"""Regression tests proving the 4 Healthcare Agent Governance Invariants.

Invariant 1: HOLD and ESCALATE must remain machine-distinguishable across every handoff
             with canonical vocabulary (ALLOW -> PROCEED, HOLD, ESCALATE, STOP).
Invariant 2: HOLD cannot expose an approval path while its evidence deficit remains unresolved.
Invariant 3: STOP must be enforced at the backend as a prohibited transition.
Invariant 4: Human review must never create ambiguity that execution authority transferred to the AI.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from audit_agent import (
    ProhibitedTransitionError,
    UnresolvedEvidenceError,
    apply_human_review,
    generate_audit_record,
    load_audit_record,
    save_audit_record,
)
from recon_guard import generate_recon_receipt

CLINICAL_STUB = {
    "analysis": "Historical summary for clinical assessment.",
    "evidence": ["Evidence 1", "Evidence 2"],
    "reasoning": "Clinical reasoning based on verified history.",
    "uncertainties": ["Recent lab results pending."],
    "recommendation": "Maintain regimen pending physician consultation.",
    "confidence_score": 0.88,
    "confidence_reason": "Based on historical documentation.",
    "authority_required": True,
}


def test_invariant_1_canonical_vocabulary_and_receipt_distinguishability() -> None:
    """Invariant 1: Receipts preserve canonical vocabulary and differentiate HOLD vs ESCALATE."""
    # 1. ALLOW maps to canonical PROCEED at contract boundary
    receipt_allow = generate_recon_receipt("scn_allow", boundary_decision="ALLOW")
    assert receipt_allow["governance_state"] == "PROCEED"
    assert receipt_allow["reason"] == "informational_within_bounds"
    assert receipt_allow["decision"] == "PROCEED"

    # 2. HOLD preserves canonical state and evidence-deficit reason
    receipt_hold = generate_recon_receipt("scn_hold", boundary_decision="HOLD")
    assert receipt_hold["governance_state"] == "HOLD"
    assert receipt_hold["reason"] == "evidence_deficit"
    assert receipt_hold["decision"] == "HOLD"

    # 3. ESCALATE preserves canonical state and authority-boundary reason
    receipt_esc = generate_recon_receipt("scn_esc", boundary_decision="ESCALATE")
    assert receipt_esc["governance_state"] == "ESCALATE"
    assert receipt_esc["reason"] == "authority_boundary"
    assert receipt_esc["decision"] == "ESCALATE"

    # 4. STOP preserves canonical state and safety-prohibition reason
    receipt_stop = generate_recon_receipt("scn_stop", boundary_decision="STOP")
    assert receipt_stop["governance_state"] == "STOP"
    assert receipt_stop["reason"] == "safety_prohibition"
    assert receipt_stop["decision"] == "STOP"

    # 5. HOLD and ESCALATE are strictly machine-distinguishable (no collapsed 'requires_approval')
    assert receipt_hold["governance_state"] != receipt_esc["governance_state"]
    assert receipt_hold["reason"] != receipt_esc["reason"]
    assert receipt_hold["decision"] != receipt_esc["decision"]
    assert receipt_hold["decision"] != "requires_approval"
    assert receipt_esc["decision"] != "requires_approval"


def test_invariant_2_unresolved_hold_blocks_approval(tmp_path: Path) -> None:
    """Invariant 2: Unresolved HOLD cannot receive clinical approval at the backend."""
    boundary_hold = {
        "boundary_decision": "HOLD",
        "boundary_reasoning": "Missing serum creatinine lab from past 30 days.",
        "identified_risks": ["Risk of acute kidney injury if renal function degraded."],
        "required_actions": ["Order serum creatinine test before dose titration."],
    }
    audit = generate_audit_record(
        "scn_hold_002",
        "patient_002",
        CLINICAL_STUB,
        boundary_hold,
        audit_id="audit_inv2_hold",
    )
    save_audit_record(audit, tmp_path)

    # Attempting approval on unresolved HOLD must raise UnresolvedEvidenceError
    with pytest.raises(UnresolvedEvidenceError, match="unresolved evidence deficit"):
        apply_human_review(
            "audit_inv2_hold",
            reviewer_name="Dr. Alex Rivera",
            reviewer_role="Attending Physician",
            review_decision="APPROVED",
            audit_directory=tmp_path,
        )

    # REQUEST_INFO is accepted as a valid data-gathering action without clearing the deficit
    updated = apply_human_review(
        "audit_inv2_hold",
        reviewer_name="Dr. Alex Rivera",
        reviewer_role="Attending Physician",
        review_decision="REQUEST_INFO",
        review_notes="Ordered serum creatinine stat.",
        audit_directory=tmp_path,
    )
    assert updated["decision"] == "HOLD"
    assert updated["human_review"]["decision"] == "REQUEST_INFO"
    assert updated["human_review"]["notes"] == "Ordered serum creatinine stat."


def test_invariant_3_backend_stop_enforcement(tmp_path: Path) -> None:
    """Invariant 3: STOP records represent hard safety boundaries and reject all review transitions."""
    boundary_stop = {
        "boundary_decision": "STOP",
        "boundary_reasoning": "Emergency chest pain with ST elevation symptoms.",
        "identified_risks": ["Immediate cardiac arrest danger."],
        "required_actions": ["Dispatch Emergency Medical Services (911)."],
    }
    audit = generate_audit_record(
        "scn_stop_002",
        "patient_002",
        CLINICAL_STUB,
        boundary_stop,
        audit_id="audit_inv3_stop",
    )
    save_audit_record(audit, tmp_path)

    # Any review transition attempt on STOP raises ProhibitedTransitionError
    with pytest.raises(ProhibitedTransitionError, match="Prohibited state transition"):
        apply_human_review(
            "audit_inv3_stop",
            reviewer_name="Dr. Alex Rivera",
            reviewer_role="Attending Physician",
            review_decision="APPROVED",
            audit_directory=tmp_path,
        )

    with pytest.raises(ProhibitedTransitionError, match="Prohibited state transition"):
        apply_human_review(
            "audit_inv3_stop",
            reviewer_name="Dr. Alex Rivera",
            reviewer_role="Attending Physician",
            review_decision="REQUEST_INFO",
            audit_directory=tmp_path,
        )

    # Ensure disk record remains completely unmutated
    loaded = load_audit_record("audit_inv3_stop", tmp_path)
    assert loaded["decision"] == "STOP"
    assert "human_review" not in loaded


def test_invariant_4_authority_separation_and_non_delegation(tmp_path: Path) -> None:
    """Invariant 4: Human review records clinical sign-off with zero AI execution delegation."""
    boundary_esc = {
        "boundary_decision": "ESCALATE",
        "boundary_reasoning": "High-risk dosage titration crosses authority threshold.",
        "identified_risks": ["Potential adverse event if unmonitored."],
        "required_actions": ["Attending physician order validation."],
    }
    audit = generate_audit_record(
        "scn_esc_002",
        "patient_002",
        CLINICAL_STUB,
        boundary_esc,
        audit_id="audit_inv4_esc",
    )
    save_audit_record(audit, tmp_path)

    updated = apply_human_review(
        "audit_inv4_esc",
        reviewer_name="Dr. Alex Rivera",
        reviewer_role="Attending Physician (MD/DO)",
        review_decision="APPROVED",
        review_notes="Validated titration protocol.",
        audit_directory=tmp_path,
    )

    # 1. Governing decision is immutable
    assert updated["decision"] == "ESCALATE"

    # 2. Non-delegation metadata is explicitly serialized
    review = updated["human_review"]
    assert review["decision"] == "APPROVED"
    assert review["carriesExecutionAuthority"] is False
    assert review["executionAuthorityTransferredToAI"] is False

    # 3. Verified approval authority is recorded
    assert (
        review["approvalAuthorityHolder"]
        == "Dr. Alex Rivera (Attending Physician (MD/DO))"
    )

    # 4. No execution-authority holder is inferred
    assert "executionAuthorityHolder" not in review

    # 5. Ghostlog timeline preserves non-delegation tokens
    ghostlog_entry = updated["recon_ghostlog"][-1]
    assert ghostlog_entry["kind"] == "human_review_signoff"
    assert ghostlog_entry["data"]["carriesExecutionAuthority"] is False
    assert ghostlog_entry["data"]["executionAuthorityTransferredToAI"] is False

    # 6. Trust Receipt includes authority attribution
    receipt = generate_recon_receipt("scn_esc_002", boundary_decision="ESCALATE")
    assert receipt["authority_attribution"]["carriesExecutionAuthority"] is False
    assert (
        receipt["authority_attribution"]["executionAuthorityTransferredToAI"] is False
    )
