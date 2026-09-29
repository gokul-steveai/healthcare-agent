"""Unit tests for the Gemini Clinical Analysis Agent."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from clinical_agent import (  # noqa: E402
    DEFAULT_MODEL,
    ClinicalAgentError,
    ClinicalQuotaError,
    ClinicalResponseError,
    analyze_patient,
    build_prompt,
    parse_response,
)


PATIENT_CONTEXT = {
    "patient": {
        "id": "patient-1",
        "gender": "F",
        "birthdate": "1980-01-01",
        "age": 40,
    },
    "conditions": [{"description": "Hypertension", "start_date": "2010-01-01"}],
    "medications": [],
    "observations": [
        {
            "date": "2020-01-01",
            "type": "Systolic Blood Pressure",
            "value": "150",
            "unit": "mm[Hg]",
        }
    ],
    "encounters": [],
}

VALID_OUTPUT = {
    "analysis": "The supplied context contains a hypertension history.",
    "evidence": ["Hypertension recorded on 2010-01-01."],
    "reasoning": "The request can be answered as a dated factual summary.",
    "uncertainties": ["No current medication list is supplied."],
    "recommendation": "Provide the dated evidence without changing treatment.",
    "confidence": "Moderate because the context is limited.",
    "confidence_score": 0.7,
    "confidence_reason": "The dated diagnosis is clear, but current medication data is absent.",
    "authority_required": False,
}


def test_build_prompt_contains_context_request_and_boundaries() -> None:
    """The prompt should ground analysis and explicitly limit authority."""

    prompt = build_prompt(PATIENT_CONTEXT, "Summarize the blood pressure evidence.")

    assert '"id":"patient-1"' in prompt
    assert "Summarize the blood pressure evidence." in prompt
    assert "Do not prescribe" in prompt
    assert "Do not execute actions" in prompt
    assert "Identify missing, stale, ambiguous, or conflicting information" in prompt
    assert "confidence score from 0.0 to 1.0" in prompt
    assert "authority_required" in prompt


def test_analyze_patient_calls_gemini_with_structured_output() -> None:
    """Gemini should receive the configured model and JSON response schema."""

    client = Mock()
    client.models.generate_content.return_value = SimpleNamespace(parsed=VALID_OUTPUT)

    result = analyze_patient(
        PATIENT_CONTEXT,
        "Summarize the blood pressure evidence.",
        client=client,
    )

    assert result == VALID_OUTPUT
    call = client.models.generate_content.call_args.kwargs
    assert call["model"] == DEFAULT_MODEL
    assert call["config"]["response_mime_type"] == "application/json"
    assert call["config"]["response_json_schema"]["required"] == list(
        VALID_OUTPUT.keys()
    )


def test_parse_response_accepts_json_text_fallback() -> None:
    """Plain JSON text should work when the SDK has no parsed property."""

    response = SimpleNamespace(text=f"```json\n{json.dumps(VALID_OUTPUT)}\n```")

    assert parse_response(response) == VALID_OUTPUT


def test_parse_response_rejects_missing_required_field() -> None:
    """Incomplete model output should fail rather than silently defaulting."""

    incomplete = dict(VALID_OUTPUT)
    incomplete.pop("confidence")

    with pytest.raises(ClinicalResponseError, match="confidence"):
        parse_response(SimpleNamespace(parsed=incomplete))


def test_parse_response_rejects_wrong_list_types() -> None:
    """Evidence and uncertainty fields must remain structured lists."""

    invalid = dict(VALID_OUTPUT, evidence="not a list")

    with pytest.raises(ClinicalResponseError, match="evidence"):
        parse_response(SimpleNamespace(parsed=invalid))


@pytest.mark.parametrize("score", [-0.1, 1.1, "0.7", True])
def test_parse_response_rejects_invalid_confidence_score(score: object) -> None:
    """Confidence scores must be numeric values within the closed unit interval."""

    invalid = dict(VALID_OUTPUT, confidence_score=score)

    with pytest.raises(ClinicalResponseError, match="confidence_score"):
        parse_response(SimpleNamespace(parsed=invalid))


@pytest.mark.parametrize("value", ["true", 1, None])
def test_parse_response_rejects_non_boolean_authority(value: object) -> None:
    """Authority requirements should not rely on truthy coercion."""

    invalid = dict(VALID_OUTPUT, authority_required=value)

    with pytest.raises(ClinicalResponseError, match="authority_required"):
        parse_response(SimpleNamespace(parsed=invalid))


def test_generation_failure_is_wrapped() -> None:
    """SDK errors should surface as a stable module-level exception."""

    client = Mock()
    client.models.generate_content.side_effect = RuntimeError("network failure")

    with pytest.raises(ClinicalAgentError, match="request failed"):
        analyze_patient(PATIENT_CONTEXT, "Summarize evidence.", client=client)


def test_large_repeated_context_is_compacted_before_generation() -> None:
    """Repeated longitudinal rows should not be copied wholesale into the prompt."""

    context = dict(PATIENT_CONTEXT)
    context["medications"] = [
        {
            "description": "Repeated medication",
            "start_date": f"2020-01-{(index % 28) + 1:02d}",
            "stop_date": None,
        }
        for index in range(1_000)
    ]
    context["observations"] = [
        {
            "date": f"2020-01-{(index % 28) + 1:02d}",
            "type": "Glucose",
            "value": str(100 + index % 20),
            "unit": "mg/dL",
        }
        for index in range(1_000)
    ]

    prompt = build_prompt(context, "Summarize the longitudinal evidence.")

    assert '"record_count":1000' in prompt
    assert '"numeric_minimum":100.0' in prompt
    assert len(prompt) < 20_000


def test_quota_failure_has_specific_error_type() -> None:
    """Gemini 429 responses should not be collapsed into generic agent errors."""

    class QuotaFailure(RuntimeError):
        status_code = 429

    client = Mock()
    client.models.generate_content.side_effect = QuotaFailure("RESOURCE_EXHAUSTED")

    with pytest.raises(ClinicalQuotaError, match="quota is temporarily exhausted"):
        analyze_patient(PATIENT_CONTEXT, "Summarize evidence.", client=client)
