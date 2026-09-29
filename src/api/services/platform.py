"""Service layer that composes the existing platform components."""

from __future__ import annotations

import json
import logging
import os
import uuid
from pathlib import Path
from typing import Any

from src.audit_agent import generate_audit_record, load_audit_record, save_audit_record
from src.boundary_agent import evaluate_boundary
from src.clinical_agent import analyze_patient
from src.config import PROJECT_ROOT, load_project_environment
from src.context_builder import build_patient_context
from src.scenario_runner import execute_scenario, load_scenario


LOGGER = logging.getLogger(__name__)


class PlatformConfigurationError(RuntimeError):
    """Raised when required runtime configuration is unavailable."""


class PlatformService:
    """Application-facing orchestration over existing platform modules."""

    def __init__(
        self,
        *,
        data_dir: str | Path | None,
        scenario_directory: str | Path = PROJECT_ROOT / "data" / "scenarios",
        result_directory: str | Path = PROJECT_ROOT / "data" / "results",
        audit_directory: str | Path = PROJECT_ROOT / "data" / "audit_logs",
        clinical_client: Any | None = None,
        boundary_client: Any | None = None,
    ) -> None:
        self.data_dir = Path(data_dir).expanduser() if data_dir else None
        self.scenario_directory = Path(scenario_directory).expanduser()
        self.result_directory = Path(result_directory).expanduser()
        self.audit_directory = Path(audit_directory).expanduser()
        self.clinical_client = clinical_client
        self.boundary_client = boundary_client

    @classmethod
    def from_environment(cls) -> "PlatformService":
        """Create a service using project `.env` settings."""

        load_project_environment()
        return cls(data_dir=os.environ.get("SYNTHEA_DATA_DIR"))

    def list_scenarios(self) -> list[dict[str, str]]:
        """Load available valid scenarios dynamically from JSON files."""

        if not self.scenario_directory.is_dir():
            raise FileNotFoundError(
                f"Scenario directory not found: {self.scenario_directory}"
            )
        scenarios: list[dict[str, str]] = []
        for path in sorted(self.scenario_directory.glob("*.json")):
            scenarios.append(load_scenario(path.stem, self.scenario_directory))
        return scenarios

    def run_scenario(self, scenario_id: str) -> dict[str, Any]:
        """Execute a stored scenario and return its compact API result."""

        data_dir = self._require_data_dir()
        result = execute_scenario(
            scenario_id,
            data_dir,
            scenario_directory=self.scenario_directory,
            result_directory=self.result_directory,
            audit_directory=self.audit_directory,
            clinical_client=self.clinical_client,
            boundary_client=self.boundary_client,
            print_progress=False,
        )
        return {
            "scenario_id": result["scenario_id"],
            "boundary_decision": result["boundary_output"]["boundary_decision"],
            "audit_id": result["audit_record"]["audit_id"],
            "status": "completed",
        }

    def analyze(self, patient_id: str, user_request: str) -> dict[str, Any]:
        """Run an ad hoc request through context, both agents, and audit."""

        data_dir = self._require_data_dir()
        patient_context = build_patient_context(patient_id, data_dir)
        clinical_output = analyze_patient(
            patient_context,
            user_request,
            client=self.clinical_client,
        )
        boundary_output = evaluate_boundary(
            clinical_output,
            client=self.boundary_client,
        )
        scenario_id = f"analysis_{uuid.uuid4().hex}"
        audit_record = generate_audit_record(
            scenario_id,
            patient_id,
            clinical_output,
            boundary_output,
        )
        save_audit_record(audit_record, self.audit_directory)
        return {
            "clinical_output": clinical_output,
            "boundary_output": boundary_output,
            "audit_id": audit_record["audit_id"],
        }

    def get_audit(self, audit_id: str) -> dict[str, Any]:
        """Load one complete audit record."""

        return load_audit_record(audit_id, self.audit_directory)

    def list_audits(self) -> list[dict[str, Any]]:
        """Return valid audit summaries sorted newest first."""

        if not self.audit_directory.exists():
            return []
        summaries: list[dict[str, Any]] = []
        for path in self.audit_directory.glob("audit_*.json"):
            try:
                record = load_audit_record(path.stem, self.audit_directory)
            except Exception:
                LOGGER.exception("Skipping unreadable audit record %s", path)
                continue
            summaries.append(
                {
                    "audit_id": record["audit_id"],
                    "timestamp": record["timestamp"],
                    "scenario_id": record["scenario_id"],
                    "patient_id": record["patient_id"],
                    "decision": record["decision"],
                    "version": record["version"],
                }
            )
        return sorted(summaries, key=lambda item: item["timestamp"], reverse=True)

    def _require_data_dir(self) -> Path:
        """Return configured CSV path or raise a stable configuration error."""

        if self.data_dir is None:
            raise PlatformConfigurationError(
                "SYNTHEA_DATA_DIR is not configured"
            )
        return self.data_dir
