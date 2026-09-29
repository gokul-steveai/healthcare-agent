"""Tests for end-to-end scenario orchestration with mocked Gemini clients."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pandas as pd
import pytest


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from clinical_agent import ClinicalAgentError  # noqa: E402
from context_builder import PatientNotFoundError  # noqa: E402
from scenario_runner import (  # noqa: E402
    ScenarioValidationError,
    execute_scenario,
    load_scenario,
    run_pipeline,
)


PATIENT_ID = "patient-1"
CLINICAL_OUTPUT = {
    "analysis": "The request can be answered as a dated factual summary.",
    "evidence": ["A condition was recorded on 2020-01-01."],
    "reasoning": "The supplied evidence supports a historical summary.",
    "uncertainties": ["Current status is unknown."],
    "recommendation": "Provide only the dated historical information.",
    "confidence": "Moderate because current status is not available.",
    "confidence_score": 0.75,
    "confidence_reason": "The historical fact is clear but current status is absent.",
    "authority_required": False,
}
BOUNDARY_OUTPUT = {
    "boundary_decision": "ALLOW",
    "boundary_reasoning": "The bounded historical summary is supported.",
    "identified_risks": ["Historical data could be mistaken as current."],
    "required_actions": ["Label the evidence as historical."],
}


def _write_scenario(directory: Path, scenario_id: str = "allow") -> None:
    directory.mkdir(parents=True, exist_ok=True)
    (directory / f"{scenario_id}.json").write_text(
        json.dumps(
            {
                "scenario_id": scenario_id,
                "patient_id": PATIENT_ID,
                "user_request": "Summarize the dated evidence.",
            }
        ),
        encoding="utf-8",
    )


def _write_csvs(directory: Path) -> None:
    pd.DataFrame(
        [{"Id": PATIENT_ID, "GENDER": "F", "BIRTHDATE": "1980-01-01"}]
    ).to_csv(directory / "patients.csv", index=False)
    pd.DataFrame(
        [
            {
                "PATIENT": PATIENT_ID,
                "DESCRIPTION": "Example condition",
                "START": "2020-01-01",
            }
        ]
    ).to_csv(directory / "conditions.csv", index=False)
    pd.DataFrame(
        columns=["PATIENT", "DESCRIPTION", "START", "STOP"]
    ).to_csv(directory / "medications.csv", index=False)
    pd.DataFrame(
        columns=["PATIENT", "DATE", "DESCRIPTION", "VALUE", "UNITS"]
    ).to_csv(directory / "observations.csv", index=False)
    pd.DataFrame(
        [
            {
                "PATIENT": PATIENT_ID,
                "START": "2020-02-01T10:00:00Z",
                "DESCRIPTION": "Wellness encounter",
            }
        ]
    ).to_csv(directory / "encounters.csv", index=False)


def _mock_clients() -> tuple[Mock, Mock]:
    clinical = Mock()
    clinical.models.generate_content.return_value = SimpleNamespace(
        parsed=CLINICAL_OUTPUT
    )
    boundary = Mock()
    boundary.models.generate_content.return_value = SimpleNamespace(
        parsed=BOUNDARY_OUTPUT
    )
    return clinical, boundary


def test_load_valid_scenario(tmp_path: Path) -> None:
    """A supported scenario file should load with required fields."""

    _write_scenario(tmp_path)

    scenario = load_scenario("allow", tmp_path)

    assert scenario == {
        "scenario_id": "allow",
        "patient_id": PATIENT_ID,
        "user_request": "Summarize the dated evidence.",
    }


def test_missing_scenario_raises_file_not_found(tmp_path: Path) -> None:
    """A supported but absent scenario file should fail clearly."""

    with pytest.raises(FileNotFoundError, match="hold.json"):
        load_scenario("hold", tmp_path)


def test_unsupported_scenario_is_rejected(tmp_path: Path) -> None:
    """Scenario identifiers cannot become arbitrary paths or labels."""

    with pytest.raises(ScenarioValidationError, match="Unsupported scenario"):
        load_scenario("unknown", tmp_path)


def test_invalid_patient_stops_before_agent_calls(tmp_path: Path) -> None:
    """An unknown patient should fail during context building."""

    _write_csvs(tmp_path)
    clinical, boundary = _mock_clients()
    scenario = {
        "scenario_id": "allow",
        "patient_id": "missing-patient",
        "user_request": "Summarize evidence.",
    }

    with pytest.raises(PatientNotFoundError):
        run_pipeline(
            scenario,
            tmp_path,
            clinical_client=clinical,
            boundary_client=boundary,
            audit_directory=tmp_path / "audit",
        )
    clinical.models.generate_content.assert_not_called()
    boundary.models.generate_content.assert_not_called()


def test_agent_failure_prevents_later_stages(tmp_path: Path) -> None:
    """A Clinical Agent failure should prevent boundary and audit execution."""

    _write_csvs(tmp_path)
    clinical, boundary = _mock_clients()
    clinical.models.generate_content.side_effect = RuntimeError("Gemini unavailable")
    scenario = {
        "scenario_id": "allow",
        "patient_id": PATIENT_ID,
        "user_request": "Summarize evidence.",
    }

    with pytest.raises(ClinicalAgentError, match="request failed"):
        run_pipeline(
            scenario,
            tmp_path,
            clinical_client=clinical,
            boundary_client=boundary,
            audit_directory=tmp_path / "audit",
        )
    boundary.models.generate_content.assert_not_called()
    assert not (tmp_path / "audit").exists()


def test_successful_pipeline_saves_audit_and_result(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    """A complete run should return and persist the full result envelope."""

    data_dir = tmp_path / "csv"
    scenario_dir = tmp_path / "scenarios"
    result_dir = tmp_path / "results"
    audit_dir = tmp_path / "audit"
    data_dir.mkdir()
    _write_csvs(data_dir)
    _write_scenario(scenario_dir)
    clinical, boundary = _mock_clients()

    result = execute_scenario(
        "allow",
        data_dir,
        scenario_directory=scenario_dir,
        result_directory=result_dir,
        audit_directory=audit_dir,
        clinical_client=clinical,
        boundary_client=boundary,
    )

    assert result["status"] == "completed"
    assert result["clinical_output"] == CLINICAL_OUTPUT
    assert result["boundary_output"] == BOUNDARY_OUTPUT
    assert result["audit_record"]["decision"] == "ALLOW"
    assert result["audit_record"]["clinical_output"] == CLINICAL_OUTPUT
    assert result["audit_record"]["boundary_output"] == BOUNDARY_OUTPUT
    assert (result_dir / "result_allow.json").is_file()
    assert (audit_dir / f"{result['audit_record']['audit_id']}.json").is_file()
    saved = json.loads((result_dir / "result_allow.json").read_text("utf-8"))
    assert saved == result

    output = capsys.readouterr().out
    assert "Scenario: ALLOW" in output
    assert "Clinical Analysis Complete" in output
    assert "Boundary Decision:\nALLOW" in output
    assert "result_allow.json" in output
