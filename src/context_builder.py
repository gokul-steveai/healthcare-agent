"""Build normalized patient context objects from Synthea CSV exports.

This module performs data loading and transformation only. It does not make
clinical decisions or invoke AI agents.
"""

from __future__ import annotations

import logging
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping

import pandas as pd


LOGGER = logging.getLogger(__name__)

REQUIRED_FILES: Mapping[str, str] = {
    "patients": "patients.csv",
    "conditions": "conditions.csv",
    "medications": "medications.csv",
    "observations": "observations.csv",
    "encounters": "encounters.csv",
}

DataFrames = dict[str, pd.DataFrame]
PatientContext = dict[str, Any]


class PatientNotFoundError(ValueError):
    """Raised when a patient identifier is absent from ``patients.csv``."""


def load_data(data_dir: str | Path) -> DataFrames:
    """Load the required Synthea CSV files from ``data_dir``.

    Values are loaded as strings so identifiers, codes, and displayed values
    retain their source representation. Empty CSV cells are normalized later.

    Args:
        data_dir: Directory containing the five required CSV files.

    Returns:
        A mapping from logical dataset name to pandas DataFrame.

    Raises:
        FileNotFoundError: If the directory or a required CSV file is missing.
        ValueError: If a required CSV file cannot be parsed.
    """

    directory = Path(data_dir).expanduser()
    if not directory.is_dir():
        raise FileNotFoundError(f"Synthea data directory not found: {directory}")

    frames: DataFrames = {}
    for name, filename in REQUIRED_FILES.items():
        path = directory / filename
        if not path.is_file():
            raise FileNotFoundError(f"Required Synthea file not found: {path}")

        try:
            frames[name] = pd.read_csv(path, dtype=str, keep_default_na=False)
        except (pd.errors.ParserError, UnicodeDecodeError) as exc:
            raise ValueError(f"Unable to parse Synthea file: {path}") from exc

        LOGGER.info("Loaded %s with %d records", filename, len(frames[name]))

    return frames


def get_patient(
    patients: pd.DataFrame,
    patient_id: str,
    *,
    reference_date: date | datetime | str | None = None,
) -> dict[str, str | int | None]:
    """Return normalized demographics for one patient.

    Args:
        patients: Contents of ``patients.csv``.
        patient_id: Synthea patient identifier.
        reference_date: Date at which age is calculated. Defaults to today.

    Returns:
        A patient dictionary containing id, gender, birthdate, and age.

    Raises:
        PatientNotFoundError: If ``patient_id`` is not present.
        ValueError: If required columns are absent.
    """

    _require_columns(patients, {"Id", "GENDER", "BIRTHDATE"}, "patients.csv")
    matches = patients.loc[patients["Id"].astype(str) == str(patient_id)]
    if matches.empty:
        raise PatientNotFoundError(f"Patient not found: {patient_id}")

    row = matches.iloc[0]
    birthdate = _normalize_date(row.get("BIRTHDATE"))
    age = _calculate_age(birthdate, reference_date)

    return {
        "id": _safe_string(row.get("Id")),
        "gender": _safe_string(row.get("GENDER")),
        "birthdate": birthdate,
        "age": age,
    }


def get_conditions(
    conditions: pd.DataFrame, patient_id: str
) -> list[dict[str, str | None]]:
    """Return a patient's conditions sorted by start date."""

    _require_columns(
        conditions, {"PATIENT", "DESCRIPTION", "START"}, "conditions.csv"
    )
    rows = _patient_rows(conditions, patient_id, "START")
    return [
        {
            "description": _safe_string(row.get("DESCRIPTION")),
            "start_date": _normalize_date(row.get("START")),
        }
        for _, row in rows.iterrows()
    ]


def get_medications(
    medications: pd.DataFrame, patient_id: str
) -> list[dict[str, str | None]]:
    """Return a patient's medications sorted by start date."""

    _require_columns(
        medications,
        {"PATIENT", "DESCRIPTION", "START", "STOP"},
        "medications.csv",
    )
    rows = _patient_rows(medications, patient_id, "START")
    return [
        {
            "description": _safe_string(row.get("DESCRIPTION")),
            "start_date": _normalize_date(row.get("START")),
            "stop_date": _normalize_date(row.get("STOP")),
        }
        for _, row in rows.iterrows()
    ]


def get_observations(
    observations: pd.DataFrame, patient_id: str
) -> list[dict[str, str | None]]:
    """Return a patient's observations sorted chronologically.

    Synthea's ``DESCRIPTION`` is exposed as ``type`` because it identifies the
    measured quantity, while the source ``TYPE`` column describes the value's
    storage type (for example, numeric or text).
    """

    _require_columns(
        observations,
        {"PATIENT", "DATE", "DESCRIPTION", "VALUE", "UNITS"},
        "observations.csv",
    )
    rows = _patient_rows(observations, patient_id, "DATE")
    return [
        {
            "date": _normalize_datetime(row.get("DATE")),
            "type": _safe_string(row.get("DESCRIPTION")),
            "value": _safe_string(row.get("VALUE")),
            "unit": _safe_string(row.get("UNITS")),
        }
        for _, row in rows.iterrows()
    ]


def get_encounters(
    encounters: pd.DataFrame, patient_id: str
) -> list[dict[str, str | None]]:
    """Return a patient's encounters sorted chronologically."""

    _require_columns(
        encounters, {"PATIENT", "START", "DESCRIPTION"}, "encounters.csv"
    )
    rows = _patient_rows(encounters, patient_id, "START")
    return [
        {
            "date": _normalize_datetime(row.get("START")),
            "type": _safe_string(row.get("DESCRIPTION")),
        }
        for _, row in rows.iterrows()
    ]


def build_patient_context(
    patient_id: str,
    data_dir: str | Path | None = None,
    *,
    data: Mapping[str, pd.DataFrame] | None = None,
) -> PatientContext:
    """Build a complete normalized context for ``patient_id``.

    Supply either ``data_dir`` for normal file loading or ``data`` for an
    already-loaded mapping, which is useful for repeated calls and tests.
    Age is calculated at the latest dated record in the patient's context so
    historical datasets produce a stable value. If no clinical record has a
    valid date, age is calculated at the current date.

    Args:
        patient_id: Synthea patient identifier.
        data_dir: Directory containing the Synthea CSV files.
        data: Optional preloaded mapping returned by :func:`load_data`.

    Returns:
        A JSON-serializable dictionary containing patient demographics,
        conditions, medications, observations, and encounters.

    Raises:
        ValueError: If neither or both data sources are supplied, or if a
            required dataset/column is missing.
        PatientNotFoundError: If ``patient_id`` does not exist.
    """

    if (data_dir is None) == (data is None):
        raise ValueError("Provide exactly one of data_dir or data")

    frames = dict(data) if data is not None else load_data(data_dir)  # type: ignore[arg-type]
    missing_frames = set(REQUIRED_FILES) - set(frames)
    if missing_frames:
        names = ", ".join(sorted(missing_frames))
        raise ValueError(f"Missing required datasets: {names}")

    # Validate existence before doing the more expensive child-table work.
    get_patient(frames["patients"], patient_id)

    conditions = get_conditions(frames["conditions"], patient_id)
    medications = get_medications(frames["medications"], patient_id)
    observations = get_observations(frames["observations"], patient_id)
    encounters = get_encounters(frames["encounters"], patient_id)
    reference_date = _latest_context_date(
        conditions, medications, observations, encounters
    )
    patient = get_patient(
        frames["patients"], patient_id, reference_date=reference_date
    )

    context: PatientContext = {
        "patient": patient,
        "conditions": conditions,
        "medications": medications,
        "observations": observations,
        "encounters": encounters,
    }
    LOGGER.info(
        "Built patient context: conditions=%d medications=%d observations=%d encounters=%d",
        len(conditions),
        len(medications),
        len(observations),
        len(encounters),
    )
    return context


def _require_columns(
    frame: pd.DataFrame, required: set[str], source_name: str
) -> None:
    """Raise a descriptive error when required source columns are absent."""

    missing = required - set(frame.columns)
    if missing:
        names = ", ".join(sorted(missing))
        raise ValueError(f"{source_name} is missing required columns: {names}")


def _patient_rows(
    frame: pd.DataFrame, patient_id: str, date_column: str
) -> pd.DataFrame:
    """Filter one patient and perform a stable chronological sort."""

    rows = frame.loc[frame["PATIENT"].astype(str) == str(patient_id)].copy()
    if rows.empty:
        return rows

    rows["_sort_date"] = pd.to_datetime(rows[date_column], errors="coerce", utc=True)
    rows["_source_order"] = range(len(rows))
    rows = rows.sort_values(
        ["_sort_date", "_source_order"], na_position="last", kind="stable"
    )
    return rows.drop(columns=["_sort_date", "_source_order"])


def _safe_string(value: Any) -> str | None:
    """Convert a CSV value to a stripped string or ``None`` when missing."""

    if value is None or pd.isna(value):
        return None
    normalized = str(value).strip()
    return normalized or None


def _normalize_date(value: Any) -> str | None:
    """Normalize a date-like value to ``YYYY-MM-DD`` when possible."""

    text = _safe_string(value)
    if text is None:
        return None
    parsed = pd.to_datetime(text, errors="coerce", utc=True)
    return parsed.strftime("%Y-%m-%d") if not pd.isna(parsed) else text


def _normalize_datetime(value: Any) -> str | None:
    """Normalize a timestamp to an ISO-8601 string when possible."""

    text = _safe_string(value)
    if text is None:
        return None
    parsed = pd.to_datetime(text, errors="coerce", utc=True)
    if pd.isna(parsed):
        return text
    if parsed.hour == parsed.minute == parsed.second == parsed.microsecond == 0:
        return parsed.strftime("%Y-%m-%d")
    return parsed.isoformat().replace("+00:00", "Z")


def _calculate_age(
    birthdate: str | None, reference_date: date | datetime | str | None
) -> int | None:
    """Calculate completed years at ``reference_date``."""

    if birthdate is None:
        return None
    birth = pd.to_datetime(birthdate, errors="coerce")
    if pd.isna(birth):
        return None

    if reference_date is None:
        reference = pd.Timestamp(date.today())
    else:
        reference = pd.to_datetime(reference_date, errors="coerce", utc=True)
        if pd.isna(reference):
            return None
        reference = reference.tz_localize(None)

    age = reference.year - birth.year
    if (reference.month, reference.day) < (birth.month, birth.day):
        age -= 1
    return max(age, 0)


def _latest_context_date(*collections: list[dict[str, Any]]) -> str | None:
    """Find the latest valid date represented in normalized child records."""

    candidates: list[pd.Timestamp] = []
    for records in collections:
        for record in records:
            for field in ("date", "start_date", "stop_date"):
                value = record.get(field)
                if value:
                    parsed = pd.to_datetime(value, errors="coerce", utc=True)
                    if not pd.isna(parsed):
                        candidates.append(parsed)

    return max(candidates).isoformat() if candidates else None
