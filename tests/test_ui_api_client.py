"""Tests for the Streamlit frontend HTTP client."""

import httpx
import pytest
from ui.services.api_client import APIClient, APIResponseError, APITimeoutError, APIUnavailableError, ResourceNotFoundError


def _client(transport: httpx.MockTransport) -> APIClient:
    return APIClient(base_url="http://testserver", client=httpx.Client(transport=transport, base_url="http://testserver"))


def test_api_client_reads_scenarios() -> None:
    transport = httpx.MockTransport(lambda request: httpx.Response(200, json={"scenarios": [{"scenario_id": "allow"}]}))
    assert _client(transport).scenarios()[0]["scenario_id"] == "allow"


def test_api_client_sends_analysis_payload() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/analyze" and request.method == "POST"
        assert request.read() == b'{"patient_id":"p1","user_request":"Summarize."}'
        return httpx.Response(200, json={"clinical_output": {}, "boundary_output": {}, "audit_id": "audit_1"})
    assert _client(httpx.MockTransport(handler)).analyze("p1", "Summarize.")["audit_id"] == "audit_1"


def test_api_client_maps_not_found_error() -> None:
    transport = httpx.MockTransport(lambda request: httpx.Response(404, json={"error": {"message": "Audit not found"}}))
    with pytest.raises(ResourceNotFoundError, match="Audit not found"):
        _client(transport).audit("audit_missing")


def test_api_client_maps_other_backend_errors() -> None:
    transport = httpx.MockTransport(lambda request: httpx.Response(502, json={"error": {"message": "Agent unavailable"}}))
    with pytest.raises(APIResponseError) as captured:
        _client(transport).run_scenario("allow")
    assert captured.value.status_code == 502


def test_api_client_maps_timeout() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ReadTimeout("timed out", request=request)
    with pytest.raises(APITimeoutError):
        _client(httpx.MockTransport(handler)).health()


def test_api_client_maps_connection_failure() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("refused", request=request)
    with pytest.raises(APIUnavailableError):
        _client(httpx.MockTransport(handler)).health()


def test_api_client_review_audit() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/audit/audit_1/review" and request.method == "POST"
        assert b"Dr. Connor" in request.read()
        return httpx.Response(200, json={"audit_id": "audit_1", "human_review": {"decision": "APPROVED"}})
    result = _client(httpx.MockTransport(handler)).review_audit("audit_1", "Dr. Connor", "Doctor", "APPROVED", "OK")
    assert result["human_review"]["decision"] == "APPROVED"
