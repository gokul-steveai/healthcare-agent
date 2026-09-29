"""FastAPI endpoint tests using mocked Gemini clients."""

from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pandas as pd
import pytest
from fastapi.testclient import TestClient

from src.api.main import create_app
from src.api.services import PlatformService
from src.clinical_agent import ClinicalQuotaError


PATIENT_ID = "patient-1"
CLINICAL_OUTPUT = {
    "analysis": "The request asks for a dated historical summary.",
    "evidence": ["Hypertension was recorded on 2020-01-01."],
    "reasoning": "The evidence supports a bounded factual summary.",
    "uncertainties": ["Current treatment status is unavailable."],
    "recommendation": "Provide dated facts without treatment changes.",
    "confidence": "Moderate confidence because current status is absent.",
    "confidence_score": 0.75,
    "confidence_reason": "The historical evidence is clear but not current.",
    "authority_required": False,
}
BOUNDARY_OUTPUT = {
    "boundary_decision": "ALLOW",
    "boundary_reasoning": "The response is informational and evidence-grounded.",
    "identified_risks": ["Historical information may be mistaken as current."],
    "required_actions": ["Label all facts with their dates."],
}


def _write_csvs(directory: Path) -> None:
    directory.mkdir(parents=True)
    pd.DataFrame(
        [{"Id": PATIENT_ID, "GENDER": "F", "BIRTHDATE": "1980-01-01"}]
    ).to_csv(directory / "patients.csv", index=False)
    pd.DataFrame(
        [
            {
                "PATIENT": PATIENT_ID,
                "DESCRIPTION": "Hypertension",
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


def _write_scenarios(directory: Path) -> None:
    directory.mkdir(parents=True)
    for scenario_id in ("allow", "hold", "escalate", "stop"):
        (directory / f"{scenario_id}.json").write_text(
            json.dumps(
                {
                    "scenario_id": scenario_id,
                    "patient_id": PATIENT_ID,
                    "user_request": f"Request for {scenario_id} test input.",
                }
            ),
            encoding="utf-8",
        )


@pytest.fixture
def api_client(tmp_path: Path) -> tuple[TestClient, PlatformService]:
    """Build an isolated API with actual services and mocked Gemini calls."""

    data_dir = tmp_path / "csv"
    scenario_dir = tmp_path / "scenarios"
    _write_csvs(data_dir)
    _write_scenarios(scenario_dir)

    clinical_client = Mock()
    clinical_client.models.generate_content.return_value = SimpleNamespace(
        parsed=CLINICAL_OUTPUT
    )
    boundary_client = Mock()
    boundary_client.models.generate_content.return_value = SimpleNamespace(
        parsed=BOUNDARY_OUTPUT
    )
    service = PlatformService(
        data_dir=data_dir,
        scenario_directory=scenario_dir,
        result_directory=tmp_path / "results",
        audit_directory=tmp_path / "audits",
        clinical_client=clinical_client,
        boundary_client=boundary_client,
    )
    return TestClient(create_app(service)), service


def test_health(api_client: tuple[TestClient, PlatformService]) -> None:
    """Health should not require dataset or Gemini execution."""

    client, _ = api_client

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
    assert response.headers["X-Request-ID"]


def test_scenarios_are_loaded_dynamically(
    api_client: tuple[TestClient, PlatformService],
) -> None:
    """Scenario discovery should reflect JSON files in the configured folder."""

    client, _ = api_client

    response = client.get("/scenarios")

    assert response.status_code == 200
    assert [item["scenario_id"] for item in response.json()["scenarios"]] == [
        "allow",
        "escalate",
        "hold",
        "stop",
    ]


def test_run_scenario_executes_pipeline(
    api_client: tuple[TestClient, PlatformService],
) -> None:
    """Stored scenarios should run through both agents and audit persistence."""

    client, service = api_client

    response = client.post("/run-scenario", json={"scenario_id": "allow"})

    assert response.status_code == 200
    body = response.json()
    assert body["scenario_id"] == "allow"
    assert body["boundary_decision"] == "ALLOW"
    assert body["audit_id"].startswith("audit_")
    assert body["status"] == "completed"
    assert (service.audit_directory / f"{body['audit_id']}.json").is_file()


def test_analyze_returns_agent_outputs_and_audit(
    api_client: tuple[TestClient, PlatformService],
) -> None:
    """Ad hoc analysis should reuse context, agent, and audit components."""

    client, service = api_client

    response = client.post(
        "/analyze",
        json={
            "patient_id": PATIENT_ID,
            "user_request": "Summarize the dated condition history.",
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["clinical_output"] == CLINICAL_OUTPUT
    assert body["boundary_output"] == BOUNDARY_OUTPUT
    assert body["audit_id"].startswith("audit_")
    assert (service.audit_directory / f"{body['audit_id']}.json").is_file()


def test_audits_and_complete_audit_are_available_newest_first(
    api_client: tuple[TestClient, PlatformService],
) -> None:
    """Audit listing should summarize persisted records and support retrieval."""

    client, _ = api_client
    first = client.post("/run-scenario", json={"scenario_id": "allow"}).json()
    second = client.post(
        "/analyze",
        json={"patient_id": PATIENT_ID, "user_request": "Summarize history."},
    ).json()

    listing = client.get("/audits")

    assert listing.status_code == 200
    audits = listing.json()["audits"]
    assert len(audits) == 2
    assert audits[0]["timestamp"] >= audits[1]["timestamp"]
    assert {item["audit_id"] for item in audits} == {
        first["audit_id"],
        second["audit_id"],
    }

    complete = client.get(f"/audit/{first['audit_id']}")
    assert complete.status_code == 200
    assert complete.json()["audit_id"] == first["audit_id"]
    assert complete.json()["clinical_output"] == CLINICAL_OUTPUT


def test_missing_patient_uses_centralized_error_response(
    api_client: tuple[TestClient, PlatformService],
) -> None:
    """Domain errors should be returned using the stable error envelope."""

    client, _ = api_client

    response = client.post(
        "/analyze",
        json={"patient_id": "missing", "user_request": "Summarize history."},
    )

    assert response.status_code == 404
    assert response.json()["error"]["code"] == "patient_not_found"
    assert response.json()["error"]["request_id"]


def test_missing_audit_returns_not_found(
    api_client: tuple[TestClient, PlatformService],
) -> None:
    """An unknown audit ID should return a centralized 404 response."""

    client, _ = api_client

    response = client.get("/audit/audit_missing")

    assert response.status_code == 404
    assert response.json()["error"]["code"] == "resource_not_found"


def test_request_schema_rejects_extra_fields(
    api_client: tuple[TestClient, PlatformService],
) -> None:
    """Pydantic v2 request schemas should reject unknown input fields."""

    client, _ = api_client

    response = client.post(
        "/run-scenario",
        json={"scenario_id": "allow", "unexpected": True},
    )

    assert response.status_code == 422
    assert response.json()["error"]["code"] == "request_validation_error"


def test_openapi_documentation_is_enabled(
    api_client: tuple[TestClient, PlatformService],
) -> None:
    """Swagger, ReDoc, and the OpenAPI schema should remain available."""

    client, _ = api_client

    assert client.get("/docs").status_code == 200
    assert client.get("/redoc").status_code == 200
    schema = client.get("/openapi.json")
    assert schema.status_code == 200
    assert "/run-scenario" in schema.json()["paths"]


def test_gemini_quota_error_returns_retryable_429() -> None:
    """Quota exhaustion should be distinguishable from an internal gateway error."""

    service = Mock()
    service.analyze.side_effect = ClinicalQuotaError(
        "Gemini quota is temporarily exhausted. Wait and retry."
    )
    client = TestClient(create_app(service))

    response = client.post(
        "/analyze",
        json={"patient_id": PATIENT_ID, "user_request": "Summarize history."},
    )

    assert response.status_code == 429
    assert response.json()["error"]["code"] == "gemini_quota_exceeded"
    assert response.headers["Retry-After"] == "60"


def test_review_audit_records_decision_and_updates_audit(
    api_client: tuple[TestClient, PlatformService],
) -> None:
    """Human review endpoint should record clinician decision and update the audit record."""

    client, _ = api_client
    run = client.post("/run-scenario", json={"scenario_id": "escalate"}).json()
    audit_id = run["audit_id"]

    review_res = client.post(
        f"/audit/{audit_id}/review",
        json={
            "reviewer_name": "Dr. Sarah Connor",
            "reviewer_role": "Attending Cardiologist",
            "decision": "APPROVED",
            "notes": "Reviewed labs and validated dose escalation.",
        },
    )

    assert review_res.status_code == 200
    updated_audit = review_res.json()
    assert updated_audit["human_review"]["decision"] == "APPROVED"
    assert updated_audit["human_review"]["reviewer_name"] == "Dr. Sarah Connor"
    assert updated_audit["human_review"]["reviewer_role"] == "Attending Cardiologist"

    get_res = client.get(f"/audit/{audit_id}")
    assert get_res.status_code == 200
    assert get_res.json()["human_review"]["decision"] == "APPROVED"
