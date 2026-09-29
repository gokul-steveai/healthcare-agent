"""Audit and traceability records for healthcare boundary-testing runs.

This module records agent outputs and structured rationale summaries. It does
not make healthcare decisions and does not attempt to capture private model
chain-of-thought.
"""

from __future__ import annotations

import json
import logging
import os
import tempfile
import uuid
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


LOGGER = logging.getLogger(__name__)

AUDIT_VERSION = "v1"
DEFAULT_AUDIT_DIRECTORY = Path("data") / "audit_logs"
BOUNDARY_DECISIONS = {"ALLOW", "HOLD", "ESCALATE", "STOP"}

CLINICAL_FIELDS = (
    "analysis",
    "evidence",
    "reasoning",
    "uncertainties",
    "recommendation",
    "confidence_score",
    "confidence_reason",
    "authority_required",
)
BOUNDARY_FIELDS = (
    "boundary_decision",
    "boundary_reasoning",
    "identified_risks",
    "required_actions",
)
AUDIT_FIELDS = (
    "audit_id",
    "timestamp",
    "scenario_id",
    "patient_id",
    "decision",
    "clinical_reasoning",
    "boundary_reasoning",
    "evidence_used",
    "identified_risks",
    "required_actions",
    "reasoning_trace",
    "clinical_output",
    "boundary_output",
    "version",
)


class AuditValidationError(ValueError):
    """Raised when agent input or an audit record is structurally invalid."""


class AuditStorageError(RuntimeError):
    """Raised when an audit record cannot be saved or loaded safely."""


def generate_audit_record(
    scenario_id: str,
    patient_id: str,
    clinical_output: Mapping[str, Any],
    boundary_output: Mapping[str, Any],
    *,
    audit_id: str | None = None,
    timestamp: str | None = None,
) -> dict[str, Any]:
    """Create a validated, JSON-serializable audit record.

    Args:
        scenario_id: Stable identifier for the boundary-testing scenario.
        patient_id: Patient or synthetic-patient identifier used in the run.
        clinical_output: Structured Clinical Analysis Agent result.
        boundary_output: Structured Boundary Evaluation Agent result.
        audit_id: Optional caller-supplied identifier, primarily for replay.
        timestamp: Optional ISO-8601 timestamp, primarily for deterministic tests.

    Returns:
        A versioned audit dictionary ready for JSON storage.

    Raises:
        AuditValidationError: If required input is missing, malformed, or not
            JSON serializable.
    """

    scenario = _non_empty_string(scenario_id, "scenario_id")
    patient = _non_empty_string(patient_id, "patient_id")
    clinical = _validate_clinical_output(clinical_output)
    boundary = _validate_boundary_output(boundary_output)

    record_id = _validate_audit_id(audit_id) if audit_id else _new_audit_id()
    record_timestamp = (
        _validate_timestamp(timestamp) if timestamp else _utc_timestamp()
    )
    trace = build_reasoning_trace(
        scenario,
        patient,
        clinical,
        boundary,
    )

    record: dict[str, Any] = {
        "audit_id": record_id,
        "timestamp": record_timestamp,
        "scenario_id": scenario,
        "patient_id": patient,
        "decision": boundary["boundary_decision"],
        "clinical_reasoning": clinical["reasoning"],
        "boundary_reasoning": boundary["boundary_reasoning"],
        "evidence_used": list(clinical["evidence"]),
        "identified_risks": list(boundary["identified_risks"]),
        "required_actions": list(boundary["required_actions"]),
        "reasoning_trace": trace,
        "clinical_output": clinical,
        "boundary_output": boundary,
        "version": AUDIT_VERSION,
    }
    _validate_audit_record(record)
    _ensure_json_serializable(record)

    LOGGER.info(
        "Generated audit record %s for scenario %s with decision %s",
        record_id,
        scenario,
        record["decision"],
    )
    return record


def build_reasoning_trace(
    scenario_id: str,
    patient_id: str,
    clinical_output: Mapping[str, Any],
    boundary_output: Mapping[str, Any],
) -> list[str]:
    """Build a concise, structured trace of the agent evaluation lifecycle.

    The trace describes processing events and recorded findings. Full agent
    rationales remain in their dedicated audit fields.
    """

    scenario = _non_empty_string(scenario_id, "scenario_id")
    patient = _non_empty_string(patient_id, "patient_id")
    clinical = _validate_clinical_output(clinical_output)
    boundary = _validate_boundary_output(boundary_output)

    evidence_count = len(clinical["evidence"])
    uncertainty_count = len(clinical["uncertainties"])
    risk_count = len(boundary["identified_risks"])
    action_count = len(boundary["required_actions"])
    authority = "required" if clinical["authority_required"] else "not required"

    return [
        f"Scenario {scenario} registered",
        f"Patient context loaded for {patient}",
        "Clinical agent analyzed patient history",
        f"Clinical agent recorded {evidence_count} evidence item(s)",
        f"Clinical agent identified {uncertainty_count} uncertainty item(s)",
        (
            "Clinical agent reported confidence "
            f"{clinical['confidence_score']:.2f} and authority {authority}"
        ),
        "Clinical agent generated a bounded recommendation",
        "Boundary agent evaluated evidence sufficiency and uncertainty",
        "Boundary agent evaluated authority requirements and safety concerns",
        f"Boundary agent identified {risk_count} risk(s)",
        f"Boundary agent required {action_count} follow-up action(s)",
        f"Boundary agent selected {boundary['boundary_decision']}",
    ]


def save_audit_record(
    audit_record: Mapping[str, Any],
    directory: str | Path = DEFAULT_AUDIT_DIRECTORY,
    *,
    overwrite: bool = False,
) -> Path:
    """Atomically save an audit record as a JSON file.

    Args:
        audit_record: Record returned by :func:`generate_audit_record`.
        directory: Audit-log directory.
        overwrite: Whether an existing record with the same ID may be replaced.

    Returns:
        Path to the saved JSON file.

    Raises:
        AuditValidationError: If the record is malformed.
        FileExistsError: If the target exists and ``overwrite`` is false.
        AuditStorageError: If storage fails.
    """

    record = dict(audit_record) if isinstance(audit_record, Mapping) else audit_record
    _validate_audit_record(record)
    _ensure_json_serializable(record)

    target_directory = Path(directory).expanduser().resolve()
    target_directory.mkdir(parents=True, exist_ok=True)
    target = target_directory / f"{record['audit_id']}.json"
    if target.exists() and not overwrite:
        raise FileExistsError(f"Audit record already exists: {target}")

    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=target_directory,
            prefix=f".{record['audit_id']}.",
            suffix=".tmp",
            delete=False,
        ) as temporary:
            json.dump(record, temporary, ensure_ascii=False, indent=2)
            temporary.write("\n")
            temporary.flush()
            os.fsync(temporary.fileno())
            temporary_path = Path(temporary.name)

        if target.exists() and not overwrite:
            raise FileExistsError(f"Audit record already exists: {target}")
        temporary_path.replace(target)
    except (OSError, TypeError) as exc:
        raise AuditStorageError(f"Unable to save audit record: {target}") from exc
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()

    LOGGER.info("Saved audit record %s", target)
    return target


def load_audit_record(
    audit_id: str,
    directory: str | Path = DEFAULT_AUDIT_DIRECTORY,
) -> dict[str, Any]:
    """Load and validate an audit record by identifier.

    Args:
        audit_id: Audit identifier without a path or extension.
        directory: Audit-log directory.

    Returns:
        Validated audit dictionary.

    Raises:
        AuditValidationError: If the ID or stored record is malformed.
        FileNotFoundError: If no matching record exists.
        AuditStorageError: If JSON cannot be decoded or read.
    """

    record_id = _validate_audit_id(audit_id)
    target = Path(directory).expanduser().resolve() / f"{record_id}.json"
    if not target.is_file():
        raise FileNotFoundError(f"Audit record not found: {target}")

    try:
        with target.open("r", encoding="utf-8") as source:
            record = json.load(source)
    except (OSError, json.JSONDecodeError) as exc:
        raise AuditStorageError(f"Unable to load audit record: {target}") from exc

    _validate_audit_record(record)
    if record["audit_id"] != record_id:
        raise AuditValidationError("Stored audit ID does not match requested ID")

    LOGGER.info("Loaded audit record %s", target)
    return record


def _validate_clinical_output(output: Mapping[str, Any]) -> dict[str, Any]:
    """Validate the fields needed from the Clinical Analysis Agent."""

    if not isinstance(output, Mapping):
        raise AuditValidationError("clinical_output must be a mapping")
    missing = [field for field in CLINICAL_FIELDS if field not in output]
    if missing:
        raise AuditValidationError(
            f"clinical_output missing required fields: {', '.join(missing)}"
        )

    # Preserve the complete packet for traceability while validating the
    # required contract fields below.
    result = dict(output)
    for field in (
        "analysis",
        "reasoning",
        "recommendation",
        "confidence_reason",
    ):
        result[field] = _non_empty_string(result[field], f"clinical_output.{field}")
    for field in ("evidence", "uncertainties"):
        result[field] = _string_list(result[field], f"clinical_output.{field}")

    score = result["confidence_score"]
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise AuditValidationError(
            "clinical_output.confidence_score must be a number"
        )
    if not 0.0 <= float(score) <= 1.0:
        raise AuditValidationError(
            "clinical_output.confidence_score must be between 0.0 and 1.0"
        )
    result["confidence_score"] = float(score)

    if not isinstance(result["authority_required"], bool):
        raise AuditValidationError(
            "clinical_output.authority_required must be a boolean"
        )
    return result


def _validate_boundary_output(output: Mapping[str, Any]) -> dict[str, Any]:
    """Validate the fields needed from the Boundary Evaluation Agent."""

    if not isinstance(output, Mapping):
        raise AuditValidationError("boundary_output must be a mapping")
    missing = [field for field in BOUNDARY_FIELDS if field not in output]
    if missing:
        raise AuditValidationError(
            f"boundary_output missing required fields: {', '.join(missing)}"
        )

    # Preserve the complete packet for traceability while validating the
    # required contract fields below.
    result = dict(output)
    decision = result["boundary_decision"]
    if decision not in BOUNDARY_DECISIONS:
        raise AuditValidationError(
            "boundary_output.boundary_decision must be ALLOW, HOLD, ESCALATE, or STOP"
        )
    result["boundary_reasoning"] = _non_empty_string(
        result["boundary_reasoning"], "boundary_output.boundary_reasoning"
    )
    for field in ("identified_risks", "required_actions"):
        result[field] = _string_list(result[field], f"boundary_output.{field}")
    return result


def _validate_audit_record(record: Any) -> None:
    """Validate stored audit-record structure and field types."""

    if not isinstance(record, Mapping):
        raise AuditValidationError("audit_record must be a mapping")
    missing = [field for field in AUDIT_FIELDS if field not in record]
    if missing:
        raise AuditValidationError(
            f"audit_record missing required fields: {', '.join(missing)}"
        )

    _validate_audit_id(record["audit_id"])
    _validate_timestamp(record["timestamp"])
    _non_empty_string(record["scenario_id"], "audit_record.scenario_id")
    _non_empty_string(record["patient_id"], "audit_record.patient_id")
    if record["decision"] not in BOUNDARY_DECISIONS:
        raise AuditValidationError("audit_record.decision is invalid")
    _non_empty_string(record["clinical_reasoning"], "audit_record.clinical_reasoning")
    _non_empty_string(record["boundary_reasoning"], "audit_record.boundary_reasoning")
    for field in (
        "evidence_used",
        "identified_risks",
        "required_actions",
        "reasoning_trace",
    ):
        _string_list(record[field], f"audit_record.{field}")
    _validate_clinical_output(record["clinical_output"])
    _validate_boundary_output(record["boundary_output"])
    if record["version"] != AUDIT_VERSION:
        raise AuditValidationError(
            f"audit_record.version must be {AUDIT_VERSION}"
        )


def _non_empty_string(value: Any, field: str) -> str:
    """Validate and normalize a required string."""

    if not isinstance(value, str) or not value.strip():
        raise AuditValidationError(f"{field} must be a non-empty string")
    return value.strip()


def _string_list(value: Any, field: str) -> list[str]:
    """Validate a list containing only non-empty strings."""

    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item.strip() for item in value
    ):
        raise AuditValidationError(f"{field} must be a list of non-empty strings")
    return [item.strip() for item in value]


def _new_audit_id() -> str:
    """Return a collision-resistant audit identifier."""

    return f"audit_{uuid.uuid4().hex}"


def _validate_audit_id(value: Any) -> str:
    """Validate an audit ID and prevent path traversal."""

    audit_id = _non_empty_string(value, "audit_id")
    if not audit_id.startswith("audit_"):
        raise AuditValidationError("audit_id must start with 'audit_'")
    if not all(character.isalnum() or character in {"_", "-"} for character in audit_id):
        raise AuditValidationError("audit_id contains invalid characters")
    return audit_id


def _utc_timestamp() -> str:
    """Return the current UTC timestamp in ISO-8601 form."""

    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _validate_timestamp(value: Any) -> str:
    """Validate and normalize an ISO-8601 timestamp."""

    timestamp = _non_empty_string(value, "timestamp")
    try:
        parsed = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    except ValueError as exc:
        raise AuditValidationError("timestamp must be ISO-8601") from exc
    if parsed.tzinfo is None:
        raise AuditValidationError("timestamp must include a timezone")
    return parsed.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def _ensure_json_serializable(value: Any) -> None:
    """Raise a validation error when a value cannot be represented as JSON."""

    try:
        json.dumps(value, ensure_ascii=False, allow_nan=False)
    except (TypeError, ValueError) as exc:
        raise AuditValidationError("audit_record must be JSON serializable") from exc
