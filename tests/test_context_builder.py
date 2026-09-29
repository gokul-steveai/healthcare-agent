"""Tests for the Synthea patient context builder."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import pytest


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from context_builder import (  # noqa: E402
    PatientNotFoundError,
    build_patient_context,
    get_medications,
    get_observations,
    load_data,
)


PATIENT_ID = "patient-1"


def _write_csvs(directory: Path, *, include_observation: bool = True) -> None:
    """Create a minimal, internally consistent Synthea fixture."""

    pd.DataFrame(
        [
            {
                "Id": PATIENT_ID,
                "GENDER": "F",
                "BIRTHDATE": "1980-06-15",
            }
        ]
    ).to_csv(directory / "patients.csv", index=False)

    pd.DataFrame(
        [
            {
                "PATIENT": PATIENT_ID,
                "DESCRIPTION": "Later condition",
                "START": "2020-02-01",
            },
            {
                "PATIENT": PATIENT_ID,
                "DESCRIPTION": "Earlier condition",
                "START": "2019-01-01",
            },
        ]
    ).to_csv(directory / "conditions.csv", index=False)

    pd.DataFrame(
        [
            {
                "PATIENT": PATIENT_ID,
                "DESCRIPTION": "Example medication",
                "START": "2020-01-01T12:00:00Z",
                "STOP": "",
            }
        ]
    ).to_csv(directory / "medications.csv", index=False)

    observation_rows = []
    if include_observation:
        observation_rows.append(
            {
                "PATIENT": PATIENT_ID,
                "DATE": "2020-03-01T12:30:00Z",
                "DESCRIPTION": "Glucose",
                "VALUE": "110.5",
                "UNITS": "mg/dL",
            }
        )
    pd.DataFrame(
        observation_rows,
        columns=["PATIENT", "DATE", "DESCRIPTION", "VALUE", "UNITS"],
    ).to_csv(directory / "observations.csv", index=False)

    pd.DataFrame(
        [
            {
                "PATIENT": PATIENT_ID,
                "START": "2020-04-01T09:00:00Z",
                "DESCRIPTION": "Wellness encounter",
            }
        ]
    ).to_csv(directory / "encounters.csv", index=False)


def test_valid_patient_builds_sorted_context(tmp_path: Path) -> None:
    """A valid patient should produce the complete normalized structure."""

    _write_csvs(tmp_path)

    context = build_patient_context(PATIENT_ID, tmp_path)

    assert context["patient"] == {
        "id": PATIENT_ID,
        "gender": "F",
        "birthdate": "1980-06-15",
        "age": 39,
    }
    assert [item["description"] for item in context["conditions"]] == [
        "Earlier condition",
        "Later condition",
    ]
    assert context["observations"] == [
        {
            "date": "2020-03-01T12:30:00Z",
            "type": "Glucose",
            "value": "110.5",
            "unit": "mg/dL",
        }
    ]
    assert context["encounters"][0]["date"] == "2020-04-01T09:00:00Z"


def test_invalid_patient_raises_clear_error(tmp_path: Path) -> None:
    """An unknown identifier should not produce an empty pseudo-patient."""

    _write_csvs(tmp_path)

    with pytest.raises(PatientNotFoundError, match="missing-patient"):
        build_patient_context("missing-patient", tmp_path)


def test_missing_values_are_normalized_to_none() -> None:
    """Blank and NaN optional values should be represented safely."""

    frame = pd.DataFrame(
        [
            {
                "PATIENT": PATIENT_ID,
                "DESCRIPTION": pd.NA,
                "START": "2020-01-01",
                "STOP": pd.NA,
            }
        ]
    )

    medications = get_medications(frame, PATIENT_ID)

    assert medications == [
        {
            "description": None,
            "start_date": "2020-01-01",
            "stop_date": None,
        }
    ]


def test_empty_observations_return_empty_list(tmp_path: Path) -> None:
    """A valid patient may have no observation records."""

    _write_csvs(tmp_path, include_observation=False)
    data = load_data(tmp_path)

    assert get_observations(data["observations"], PATIENT_ID) == []
    assert build_patient_context(PATIENT_ID, data=data)["observations"] == []
