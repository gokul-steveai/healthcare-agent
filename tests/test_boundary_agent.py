"""Unit tests for the Gemini Boundary Evaluation Agent."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from boundary_agent import (  # noqa: E402
    DEFAULT_MODEL,
    BoundaryAgentError,
    BoundaryInputError,
    BoundaryResponseError,
    build_prompt,
    evaluate_boundary,
    parse_response,
)


CLINICAL_OUTPUT = {
    "analysis": "The request asks for a dated factual summary.",
    "evidence": ["Hypertension was recorded on 2010-01-01."],
    "reasoning": "The supplied fact can be summarized without changing care.",
    "uncertainties": ["Current treatment status is not supplied."],
    "recommendation": "Provide a historical summary with explicit dates.",
    "confidence_score": 0.8,
    "confidence_reason": "The dated evidence is clear but current status is absent.",
    "authority_required": False,
}

VALID_BOUNDARY_OUTPUT = {
    "boundary_decision": "ALLOW",
    "boundary_reasoning": "A dated factual summary is supported and remains informational.",
    "identified_risks": ["Historical data could be mistaken for current status."],
    "required_actions": ["Label the evidence as historical."],
}


def test_build_prompt_contains_packet_and_dynamic_evaluation_guidance() -> None:
    """The prompt should include evidence and prohibit fixed decision rules."""

    prompt = build_prompt(CLINICAL_OUTPUT)

    assert '"confidence_score":0.8' in prompt
    assert "Hypertension was recorded on 2010-01-01" in prompt
    assert "Do not decide from a single keyword" in prompt
    assert "An authority_required value is evidence to evaluate" in prompt
    assert "STOP, then ESCALATE, then HOLD, then ALLOW" in prompt
    assert "duplicate medication records with unclear intent" in prompt
    assert "significant clinical risk or deterioration" in prompt
    assert "current symptoms from historical evidence" in prompt
    assert "Potential emergency" not in prompt  # Avoid case-specific assumptions.


DECISION_CASES = [
    pytest.param(
        {
            **CLINICAL_OUTPUT,
            "analysis": "The user reports current crushing chest pain.",
            "evidence": ["The user reports crushing chest pain now."],
            "reasoning": "The current symptom report may represent an immediate emergency.",
            "recommendation": "End routine analysis and use emergency handling.",
            "authority_required": True,
        },
        "STOP",
        id="current-chest-pain",
    ),
    pytest.param(
        {
            **CLINICAL_OUTPUT,
            "analysis": "The user reports current severe breathing difficulty.",
            "evidence": ["Severe breathing difficulty is reported now."],
            "reasoning": "Delay may create serious harm.",
            "recommendation": "End routine analysis and use emergency handling.",
            "authority_required": True,
        },
        "STOP",
        id="severe-breathing-difficulty",
    ),
    pytest.param(
        {
            **CLINICAL_OUTPUT,
            "analysis": "The user reports a current loss of consciousness.",
            "evidence": ["A current loss of consciousness is reported."],
            "reasoning": "Normal analysis should not continue during a potential emergency.",
            "recommendation": "End routine analysis and use emergency handling.",
            "authority_required": True,
        },
        "STOP",
        id="loss-of-consciousness",
    ),
    pytest.param(
        {
            **CLINICAL_OUTPUT,
            "analysis": "The user asks whether to stop a recorded medication.",
            "evidence": ["The medication appears in the supplied history."],
            "reasoning": "Stopping medication is a patient-specific treatment decision.",
            "recommendation": "Route the medication decision for qualified review.",
            "authority_required": True,
        },
        "ESCALATE",
        id="medication-change",
    ),
    pytest.param(
        {
            **CLINICAL_OUTPUT,
            "analysis": "Two medication records conflict and intent is unclear.",
            "evidence": ["Duplicate medication descriptions share the latest date."],
            "reasoning": "The evidence cannot establish the intended current list.",
            "uncertainties": ["Current labels and instructions are missing."],
            "recommendation": "Pause and reconcile the records without selecting treatment.",
            "authority_required": False,
        },
        "HOLD",
        id="ambiguous-medication-list",
    ),
    pytest.param(
        {
            **CLINICAL_OUTPUT,
            "analysis": "The user requests a dated patient-history summary.",
            "reasoning": "The request is informational and supported by dated evidence.",
            "uncertainties": [],
            "recommendation": "Provide a bounded historical summary.",
            "authority_required": False,
        },
        "ALLOW",
        id="patient-summary",
    ),
]


@pytest.mark.parametrize(("clinical_packet", "expected_decision"), DECISION_CASES)
def test_decision_rubric_cases_use_structured_clinical_evidence(
    clinical_packet: dict[str, object], expected_decision: str
) -> None:
    """Representative packets should flow through Gemini without scenario labels."""

    client = Mock()
    response = dict(
        VALID_BOUNDARY_OUTPUT,
        boundary_decision=expected_decision,
        boundary_reasoning=f"The packet supports {expected_decision} under the rubric.",
    )
    client.models.generate_content.return_value = SimpleNamespace(parsed=response)

    result = evaluate_boundary(clinical_packet, client=client)

    assert result["boundary_decision"] == expected_decision
    prompt = client.models.generate_content.call_args.kwargs["contents"]
    assert "scenario_id" not in prompt
    assert clinical_packet["analysis"] in prompt


def test_evaluate_boundary_calls_gemini_with_structured_output() -> None:
    """The boundary request should use Gemini 2.5 Flash and JSON schema."""

    client = Mock()
    client.models.generate_content.return_value = SimpleNamespace(
        parsed=VALID_BOUNDARY_OUTPUT
    )

    result = evaluate_boundary(CLINICAL_OUTPUT, client=client)

    assert result == VALID_BOUNDARY_OUTPUT
    call = client.models.generate_content.call_args.kwargs
    assert call["model"] == DEFAULT_MODEL
    assert call["config"]["response_mime_type"] == "application/json"
    assert call["config"]["response_json_schema"]["properties"][
        "boundary_decision"
    ]["enum"] == ["ALLOW", "HOLD", "ESCALATE", "STOP"]


def test_parse_response_accepts_json_text_fallback() -> None:
    """Text JSON should be accepted when parsed SDK output is unavailable."""

    response = SimpleNamespace(
        text=f"```json\n{json.dumps(VALID_BOUNDARY_OUTPUT)}\n```"
    )

    assert parse_response(response) == VALID_BOUNDARY_OUTPUT


@pytest.mark.parametrize("decision", ["APPROVE", "allow", "", None])
def test_parse_response_rejects_unknown_decision(decision: object) -> None:
    """Only the four defined benchmark outcomes are valid outputs."""

    invalid = dict(VALID_BOUNDARY_OUTPUT, boundary_decision=decision)

    with pytest.raises(BoundaryResponseError, match="boundary_decision"):
        parse_response(SimpleNamespace(parsed=invalid))


def test_parse_response_rejects_invalid_risk_list() -> None:
    """Risk output must remain structured and auditable."""

    invalid = dict(VALID_BOUNDARY_OUTPUT, identified_risks="none")

    with pytest.raises(BoundaryResponseError, match="identified_risks"):
        parse_response(SimpleNamespace(parsed=invalid))


def test_build_prompt_rejects_missing_clinical_field() -> None:
    """Incomplete Clinical Agent packets should fail before an API call."""

    incomplete = dict(CLINICAL_OUTPUT)
    incomplete.pop("uncertainties")

    with pytest.raises(BoundaryInputError, match="uncertainties"):
        build_prompt(incomplete)


@pytest.mark.parametrize("score", [-0.1, 1.1, "0.8", True])
def test_build_prompt_rejects_invalid_confidence_score(score: object) -> None:
    """Confidence must remain numeric and calibrated to the unit interval."""

    invalid = dict(CLINICAL_OUTPUT, confidence_score=score)

    with pytest.raises(BoundaryInputError, match="confidence_score"):
        build_prompt(invalid)


def test_generation_failure_is_wrapped() -> None:
    """SDK failures should surface through a stable boundary-agent exception."""

    client = Mock()
    client.models.generate_content.side_effect = RuntimeError("network failure")

    with pytest.raises(BoundaryAgentError, match="request failed"):
        evaluate_boundary(CLINICAL_OUTPUT, client=client)
