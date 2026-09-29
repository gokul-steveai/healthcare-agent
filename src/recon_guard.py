"""Recon.AI SDK Guard & GhostLog Timeline integration for Healthcare Boundary Agents.

This module provides a non-invasive control layer around the Primary Clinical Agent
using Recon.AI's TrustGuard, PolicyEngine, and GhostLog timeline.
It operates in offline dry_run mode by default, maintaining full backward compatibility.
"""

from __future__ import annotations

import logging
import os
from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

try:
    from .clinical_agent import ClinicalAgentError, analyze_patient
except ImportError:
    from clinical_agent import ClinicalAgentError, analyze_patient

LOGGER = logging.getLogger(__name__)

try:
    from reconai import GhostLog, ReconConfig, TrustGuard
    HAS_RECON = True
except ImportError:
    HAS_RECON = False


DEFAULT_APPROVAL_MARKERS = (
    "medication",
    "prescribe",
    "adjust dose",
    "change dosage",
    "titrate",
    "stop medication",
    "discontinue",
    "start medication",
    "clinical review is needed",
    "qualified healthcare provider",
)

DEFAULT_BLOCKED_MARKERS = (
    "emergency",
    "chest pain",
    "immediate danger",
    "call 911",
    "life-threatening",
)


import uuid
from datetime import datetime, timezone


@dataclass(frozen=True)
class GuardedClinicalResult:
    """Container holding clinical output and associated Recon governance metadata."""

    clinical_output: dict[str, Any]
    ghostlog_timeline: list[dict[str, Any]] = field(default_factory=list)
    recon_decision: str = "permit"
    recon_receipt: dict[str, Any] = field(default_factory=dict)
    is_guarded: bool = False


def generate_recon_receipt(
    scenario_id: str,
    boundary_decision: str,
    correlation_id: str | None = None,
) -> dict[str, Any]:
    """Generate a structured Recon.AI Trust Receipt matching production schema."""

    cid = correlation_id or f"tacorr_{uuid.uuid4().hex}"
    receipt_id = f"receipt_{uuid.uuid4().hex}"
    ledger_id = f"ledger_{uuid.uuid4().hex}"

    if boundary_decision == "ALLOW":
        decision = "permit"
    elif boundary_decision in ("HOLD", "ESCALATE"):
        decision = "requires_approval"
    else:
        decision = "blocked"

    now_iso = datetime.now(timezone.utc).isoformat()
    is_dry_run = os.getenv("RECON_DRY_RUN", "true").lower() == "true"

    return {
        "correlation_id": cid,
        "receipt_id": receipt_id,
        "ledger_entry_id": ledger_id,
        "decision": decision,
        "policy_id": f"policy_healthcare_{scenario_id}",
        "issued_at": now_iso,
        "receipt_url": f"https://reconai.net/trust-receipts/{cid}",
        "ledger_url": f"https://reconai.net/ghostlog?highlight={cid}",
        "governance_mode": "dry_run" if is_dry_run else "live",
    }


class _ClinicalAgentAdapter:
    """Adapts analyze_patient to Recon's .invoke({"input": ...}) protocol."""

    def __init__(
        self,
        patient_context: Mapping[str, Any],
        analyze_kwargs: dict[str, Any],
    ) -> None:
        self.patient_context = patient_context
        self.analyze_kwargs = analyze_kwargs
        self.captured_clinical_output: dict[str, Any] | None = None

    def invoke(self, payload: dict[str, Any]) -> dict[str, Any]:
        user_request = str(payload.get("input", ""))
        clinical_output = analyze_patient(
            self.patient_context,
            user_request,
            **self.analyze_kwargs,
        )
        self.captured_clinical_output = clinical_output
        recommendation = str(clinical_output.get("recommendation", ""))
        return {"output": recommendation}


def guarded_analyze_patient(
    patient_context: Mapping[str, Any],
    user_request: str,
    *,
    approval_markers: tuple[str, ...] | None = None,
    blocked_markers: tuple[str, ...] | None = None,
    **analyze_kwargs: Any,
) -> GuardedClinicalResult:
    """Analyze a patient request with Recon TrustGuard monitoring and GhostLog timeline.

    If Recon is disabled or unavailable, seamlessly falls back to standard analyze_patient().

    Args:
        patient_context: Normalized patient context dictionary.
        user_request: User healthcare information request.
        approval_markers: Keyword markers requiring HITL approval.
        blocked_markers: Keyword markers requiring immediate policy block.
        **analyze_kwargs: Additional kwargs passed to analyze_patient (client, api_key, model).

    Returns:
        GuardedClinicalResult containing validated clinical_output and ghostlog_timeline.
    """

    recon_enabled = (
        os.getenv("RECON_ENABLED", "true").lower() == "true" and HAS_RECON
    )

    if not recon_enabled:
        LOGGER.debug("Recon guard disabled or unavailable; running native clinical analysis")
        clinical_output = analyze_patient(
            patient_context, user_request, **analyze_kwargs
        )
        return GuardedClinicalResult(
            clinical_output=clinical_output,
            ghostlog_timeline=[],
            recon_decision="bypassed",
            is_guarded=False,
        )

    dry_run = os.getenv("RECON_DRY_RUN", "true").lower() == "true"
    team_id = os.getenv("RECON_TEAM_ID", "healthcare_boundary_framework")

    config = ReconConfig(
        dry_run=dry_run,
        team_id=team_id,
        enable_ghostlog=True,
    )

    policy_kwargs = {
        "approval_markers": approval_markers or DEFAULT_APPROVAL_MARKERS,
        "blocked_markers": blocked_markers or DEFAULT_BLOCKED_MARKERS,
        "approval_below_score": 0.7,
    }

    ghostlog = GhostLog()
    adapter = _ClinicalAgentAdapter(patient_context, analyze_kwargs)

    try:
        guard = TrustGuard(
            adapter,
            config=config,
            ghostlog=ghostlog,
            **policy_kwargs,
        )

        # Trigger Recon-guarded run
        guard.invoke({"input": user_request})

        timeline = ghostlog.to_list()
        event_kinds = [e.get("kind") for e in timeline]

        if "policy_blocked" in event_kinds:
            decision = "blocked"
        elif "requires_approval" in event_kinds:
            decision = "requires_approval"
        else:
            decision = "permit"

        clinical_output = adapter.captured_clinical_output
        if clinical_output is None:
            # Fallback if for any reason invoke was bypassed
            clinical_output = analyze_patient(
                patient_context, user_request, **analyze_kwargs
            )

        return GuardedClinicalResult(
            clinical_output=clinical_output,
            ghostlog_timeline=timeline,
            recon_decision=decision,
            is_guarded=True,
        )

    except ClinicalAgentError:
        raise
    except Exception:
        LOGGER.exception("Recon TrustGuard encountered error; falling back to native clinical analysis")
        if adapter.captured_clinical_output is not None:
            clinical_output = adapter.captured_clinical_output
        else:
            clinical_output = analyze_patient(
                patient_context, user_request, **analyze_kwargs
            )
        return GuardedClinicalResult(
            clinical_output=clinical_output,
            ghostlog_timeline=[],
            recon_decision="error_fallback",
            is_guarded=False,
        )
