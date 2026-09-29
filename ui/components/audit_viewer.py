"""Reusable clinical, boundary, and audit renderers."""

from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from typing import Any

import streamlit as st

from .decision_card import render_decision_card


def render_string_list(title: str, values: Any, *, empty: str = "None recorded") -> None:
    st.markdown(f"**{title}**")
    if isinstance(values, Sequence) and not isinstance(values, (str, bytes)) and values:
        for value in values:
            st.markdown(f"- {value}")
    else:
        st.caption(empty)


def render_clinical_output(clinical: Mapping[str, Any]) -> None:
    """Render Clinical Agent fields."""

    st.markdown("#### Clinical Analysis")
    st.write(clinical.get("analysis", "Not available"))
    render_string_list("Evidence", clinical.get("evidence"))
    st.markdown("**Reasoning**")
    st.write(clinical.get("reasoning", "Not available"))
    render_string_list("Uncertainties", clinical.get("uncertainties"))
    st.markdown("**Recommendation**")
    st.write(clinical.get("recommendation", "Not available"))
    columns = st.columns(3)
    columns[0].metric("Confidence", clinical.get("confidence", "—"))
    score = clinical.get("confidence_score")
    columns[1].metric("Confidence score", f"{float(score):.0%}" if isinstance(score, (int, float)) else "—")
    columns[2].metric("Authority required", "Yes" if clinical.get("authority_required") else "No")
    if clinical.get("confidence_reason"):
        st.caption(f"Confidence basis: {clinical['confidence_reason']}")


def render_boundary_output(boundary: Mapping[str, Any]) -> None:
    """Render Boundary Agent fields."""

    st.markdown("#### Boundary Analysis")
    render_decision_card(str(boundary.get("boundary_decision", "UNKNOWN")), str(boundary.get("boundary_reasoning", "")))
    render_string_list("Identified risks", boundary.get("identified_risks"))
    render_string_list("Required actions", boundary.get("required_actions"))


def render_audit_viewer(audit: Mapping[str, Any]) -> None:
    """Render a complete audit record."""

    columns = st.columns(4)
    columns[0].metric("Decision", audit.get("decision", "—"))
    columns[1].metric("Scenario", audit.get("scenario_id", "—"))
    columns[2].metric("Patient", audit.get("patient_id", "—"))
    columns[3].metric("Version", audit.get("version", "—"))
    st.caption(f"Audit ID: {audit.get('audit_id', '—')} · {audit.get('timestamp', '—')}")
    render_decision_card(str(audit.get("decision", "UNKNOWN")), str(audit.get("boundary_reasoning", "")))
    render_string_list("Evidence used", audit.get("evidence_used"))
    render_string_list("Identified risks", audit.get("identified_risks"))
    render_string_list("Required actions", audit.get("required_actions"))
    render_string_list("Reasoning trace", audit.get("reasoning_trace"))
    with st.expander("Clinical Agent output"):
        value = audit.get("clinical_output", {})
        render_clinical_output(value) if isinstance(value, Mapping) else st.json(value)
    with st.expander("Boundary Agent output"):
        value = audit.get("boundary_output", {})
        render_boundary_output(value) if isinstance(value, Mapping) else st.json(value)
    with st.expander("Raw audit JSON"):
        st.json(dict(audit))
        st.code(json.dumps(audit, indent=2), language="json")
