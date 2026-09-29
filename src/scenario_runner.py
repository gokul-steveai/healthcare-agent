"""Orchestrate healthcare boundary-testing scenarios end to end.

Pipeline: scenario -> patient context -> Clinical Agent -> Boundary Agent ->
Audit Agent -> persisted result. Scenario names select inputs only and are not
provided to the reasoning agents.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import tempfile
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

try:  # Support package imports used by ASGI servers.
    from .audit_agent import (
        DEFAULT_AUDIT_DIRECTORY,
        generate_audit_record,
        save_audit_record,
    )
    from .boundary_agent import evaluate_boundary
    from .clinical_agent import analyze_patient
    from .config import load_project_environment
    from .context_builder import build_patient_context
    from .recon_guard import generate_recon_receipt, guarded_analyze_patient
except ImportError:  # pragma: no cover - legacy direct-script execution.
    from audit_agent import (
        DEFAULT_AUDIT_DIRECTORY,
        generate_audit_record,
        save_audit_record,
    )
    from boundary_agent import evaluate_boundary
    from clinical_agent import analyze_patient
    from config import load_project_environment
    from context_builder import build_patient_context
    from recon_guard import generate_recon_receipt, guarded_analyze_patient


LOGGER = logging.getLogger(__name__)

SUPPORTED_SCENARIOS = ("allow", "hold", "escalate", "stop")
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCENARIO_DIRECTORY = PROJECT_ROOT / "data" / "scenarios"
DEFAULT_RESULT_DIRECTORY = PROJECT_ROOT / "data" / "results"
SCENARIO_FIELDS = ("scenario_id", "patient_id", "user_request")
RESULT_FIELDS = (
    "scenario_id",
    "patient_id",
    "clinical_output",
    "boundary_output",
    "audit_record",
    "status",
)


class ScenarioRunnerError(RuntimeError):
    """Base error for scenario orchestration failures."""


class ScenarioValidationError(ValueError):
    """Raised when a scenario or result has invalid structure."""


def load_scenario(
    scenario_id: str,
    scenario_directory: str | Path = DEFAULT_SCENARIO_DIRECTORY,
) -> dict[str, str]:
    """Load and validate one supported scenario JSON file.

    Args:
        scenario_id: One of ``allow``, ``hold``, ``escalate``, or ``stop``.
        scenario_directory: Directory containing scenario JSON files.

    Returns:
        Validated scenario dictionary.

    Raises:
        ScenarioValidationError: If the identifier or JSON structure is invalid.
        FileNotFoundError: If the scenario file does not exist.
        ScenarioRunnerError: If the file cannot be decoded or read.
    """

    normalized_id = _validate_scenario_id(scenario_id)
    path = Path(scenario_directory).expanduser().resolve() / f"{normalized_id}.json"
    if not path.is_file():
        raise FileNotFoundError(f"Scenario not found: {path}")

    try:
        with path.open("r", encoding="utf-8") as source:
            scenario = json.load(source)
    except (OSError, json.JSONDecodeError) as exc:
        raise ScenarioRunnerError(f"Unable to load scenario: {path}") from exc

    return _validate_scenario(scenario, expected_id=normalized_id)


def run_pipeline(
    scenario: Mapping[str, Any],
    data_dir: str | Path,
    *,
    clinical_client: Any | None = None,
    boundary_client: Any | None = None,
    clinical_api_key: str | None = None,
    boundary_api_key: str | None = None,
    audit_directory: str | Path = DEFAULT_AUDIT_DIRECTORY,
) -> dict[str, Any]:
    """Execute all pipeline stages for an already-loaded scenario.

    The scenario identifier is retained for audit metadata but is not included
    in either Gemini prompt, preventing the expected test label from biasing an
    agent decision.

    Args:
        scenario: Valid scenario mapping.
        data_dir: Directory containing Synthea CSV files.
        clinical_client: Optional injected Google Gen AI client.
        boundary_client: Optional independently injected Google Gen AI client.
        clinical_api_key: Optional key used if a Clinical client is created.
        boundary_api_key: Optional key used if a Boundary client is created.
        audit_directory: JSON audit-log directory.

    Returns:
        Completed structured result containing all agent outputs.
    """

    validated = _validate_scenario(scenario)
    patient_context = build_patient_context(validated["patient_id"], data_dir)
    LOGGER.info("Patient context loaded for scenario %s", validated["scenario_id"])

    guarded_result = guarded_analyze_patient(
        patient_context,
        validated["user_request"],
        client=clinical_client,
        api_key=clinical_api_key,
    )
    clinical_output = guarded_result.clinical_output
    LOGGER.info("Clinical analysis completed for scenario %s", validated["scenario_id"])

    # Only the Clinical Agent packet is supplied. The scenario ID and expected
    # benchmark category are deliberately withheld from the Boundary Agent.
    boundary_output = evaluate_boundary(
        clinical_output,
        client=boundary_client,
        api_key=boundary_api_key,
    )
    LOGGER.info(
        "Boundary evaluation completed for scenario %s", validated["scenario_id"]
    )

    recon_receipt = generate_recon_receipt(
        scenario_id=validated["scenario_id"],
        boundary_decision=boundary_output["boundary_decision"],
    )
    audit_record = generate_audit_record(
        scenario_id=validated["scenario_id"],
        patient_id=validated["patient_id"],
        clinical_output=clinical_output,
        boundary_output=boundary_output,
        recon_ghostlog=guarded_result.ghostlog_timeline,
        recon_receipt=recon_receipt,
    )
    save_audit_record(audit_record, audit_directory)

    return {
        "scenario_id": validated["scenario_id"],
        "patient_id": validated["patient_id"],
        "clinical_output": clinical_output,
        "boundary_output": boundary_output,
        "audit_record": audit_record,
        "status": "completed",
    }


def execute_scenario(
    scenario_id: str,
    data_dir: str | Path,
    *,
    scenario_directory: str | Path = DEFAULT_SCENARIO_DIRECTORY,
    result_directory: str | Path = DEFAULT_RESULT_DIRECTORY,
    audit_directory: str | Path = DEFAULT_AUDIT_DIRECTORY,
    clinical_client: Any | None = None,
    boundary_client: Any | None = None,
    clinical_api_key: str | None = None,
    boundary_api_key: str | None = None,
    print_progress: bool = True,
) -> dict[str, Any]:
    """Load, run, save, and optionally print one scenario's result."""

    scenario = load_scenario(scenario_id, scenario_directory)
    result = run_pipeline(
        scenario,
        data_dir,
        clinical_client=clinical_client,
        boundary_client=boundary_client,
        clinical_api_key=clinical_api_key,
        boundary_api_key=boundary_api_key,
        audit_directory=audit_directory,
    )
    result_path = save_result(result, result_directory)

    if print_progress:
        decision = result["boundary_output"]["boundary_decision"]
        audit_name = f"{result['audit_record']['audit_id']}.json"
        print(f"Scenario: {scenario['scenario_id'].upper()}")
        print("\nClinical Analysis Complete")
        print(f"\nBoundary Decision:\n{decision}")
        print(f"\nAudit Created:\n{audit_name}")
        print(f"\nResult Saved:\n{result_path.name}")

    return result


def save_result(
    result: Mapping[str, Any],
    result_directory: str | Path = DEFAULT_RESULT_DIRECTORY,
) -> Path:
    """Atomically persist a completed pipeline result as JSON."""

    normalized = _validate_result(result)
    directory = Path(result_directory).expanduser().resolve()
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / f"result_{normalized['scenario_id']}.json"
    temporary_path: Path | None = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=directory,
            prefix=f".result_{normalized['scenario_id']}.",
            suffix=".tmp",
            delete=False,
        ) as temporary:
            json.dump(normalized, temporary, ensure_ascii=False, indent=2)
            temporary.write("\n")
            temporary.flush()
            os.fsync(temporary.fileno())
            temporary_path = Path(temporary.name)
        temporary_path.replace(target)
    except (OSError, TypeError, ValueError) as exc:
        raise ScenarioRunnerError(f"Unable to save result: {target}") from exc
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()

    LOGGER.info("Saved scenario result %s", target)
    return target


def _validate_scenario(
    scenario: Mapping[str, Any], *, expected_id: str | None = None
) -> dict[str, str]:
    """Validate and normalize a scenario mapping."""

    if not isinstance(scenario, Mapping):
        raise ScenarioValidationError("scenario must be a mapping")
    missing = [field for field in SCENARIO_FIELDS if field not in scenario]
    if missing:
        raise ScenarioValidationError(
            f"scenario missing required fields: {', '.join(missing)}"
        )

    scenario_id = _validate_scenario_id(scenario["scenario_id"])
    if expected_id is not None and scenario_id != expected_id:
        raise ScenarioValidationError(
            f"Scenario file ID '{scenario_id}' does not match '{expected_id}'"
        )
    patient_id = _non_empty_string(scenario["patient_id"], "patient_id")
    user_request = _non_empty_string(scenario["user_request"], "user_request")
    return {
        "scenario_id": scenario_id,
        "patient_id": patient_id,
        "user_request": user_request,
    }


def _validate_result(result: Mapping[str, Any]) -> dict[str, Any]:
    """Validate the final pipeline-result envelope before persistence."""

    if not isinstance(result, Mapping):
        raise ScenarioValidationError("result must be a mapping")
    missing = [field for field in RESULT_FIELDS if field not in result]
    if missing:
        raise ScenarioValidationError(
            f"result missing required fields: {', '.join(missing)}"
        )
    normalized = {field: result[field] for field in RESULT_FIELDS}
    normalized["scenario_id"] = _validate_scenario_id(normalized["scenario_id"])
    normalized["patient_id"] = _non_empty_string(
        normalized["patient_id"], "patient_id"
    )
    if normalized["status"] != "completed":
        raise ScenarioValidationError("result status must be 'completed'")
    for field in ("clinical_output", "boundary_output", "audit_record"):
        if not isinstance(normalized[field], Mapping):
            raise ScenarioValidationError(f"result {field} must be a mapping")
        normalized[field] = dict(normalized[field])
    try:
        json.dumps(normalized, allow_nan=False)
    except (TypeError, ValueError) as exc:
        raise ScenarioValidationError("result must be JSON serializable") from exc
    return normalized


def _validate_scenario_id(value: Any) -> str:
    """Validate a supported scenario identifier without path interpretation."""

    scenario_id = _non_empty_string(value, "scenario_id").lower()
    if scenario_id not in SUPPORTED_SCENARIOS:
        supported = ", ".join(SUPPORTED_SCENARIOS)
        raise ScenarioValidationError(
            f"Unsupported scenario '{scenario_id}'; expected one of: {supported}"
        )
    return scenario_id


def _non_empty_string(value: Any, field: str) -> str:
    """Validate and strip a required string."""

    if not isinstance(value, str) or not value.strip():
        raise ScenarioValidationError(f"{field} must be a non-empty string")
    return value.strip()


def _resolve_cli_data_dir(explicit: str | None) -> Path:
    """Resolve Synthea data from a CLI argument or environment variable."""

    load_project_environment()
    value = explicit or os.environ.get("SYNTHEA_DATA_DIR")
    if not value:
        raise ScenarioValidationError(
            "Synthea data directory is required; pass --data-dir or set "
            "SYNTHEA_DATA_DIR"
        )
    return Path(value).expanduser()


def main(argv: Sequence[str] | None = None) -> int:
    """Run one supported scenario from the command line."""

    parser = argparse.ArgumentParser(
        description="Run a healthcare AI boundary-testing scenario."
    )
    parser.add_argument("scenario_id", choices=SUPPORTED_SCENARIOS)
    parser.add_argument(
        "--data-dir",
        help="Synthea CSV directory; defaults to SYNTHEA_DATA_DIR.",
    )
    args = parser.parse_args(argv)

    try:
        execute_scenario(
            args.scenario_id,
            _resolve_cli_data_dir(args.data_dir),
        )
    except Exception as exc:
        LOGGER.error("Scenario execution failed: %s", exc)
        parser.exit(1, f"Error: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
