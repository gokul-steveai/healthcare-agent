"""Real-time conversational boundary-testing page."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

import streamlit as st

from ui.components import render_decision_badge
from ui.pages.common import json_download, show_api_error
from ui.services import APIClient


DEFAULT_PATIENT_ID = "2c71dd97-7085-416a-aa07-d675bbe3adf2"
HISTORY_KEY = "chat_boundary_history"


def render(client: APIClient) -> None:
    """Render a chat interface backed by the full audited agent pipeline."""

    st.title("Chat Boundary Lab")
    st.caption(
        "Chat with the healthcare-information agent and inspect its boundary "
        "decision for every message. Each interaction creates an audit record."
    )
    st.info(
        "Synthetic research environment only. Responses analyze supplied records; "
        "they are not diagnosis, prescribing, or emergency services."
    )

    if "chat_patient_id" not in st.session_state:
        st.session_state["chat_patient_id"] = DEFAULT_PATIENT_ID

    controls = st.columns([4, 1])
    patient_id = controls[0].text_input(
        "Patient ID",
        key="chat_patient_id",
    )
    if controls[1].button("Clear chat", use_container_width=True):
        st.session_state[HISTORY_KEY] = []
        st.rerun()

    history = st.session_state.setdefault(HISTORY_KEY, [])
    for index, interaction in enumerate(history):
        if isinstance(interaction, Mapping):
            _render_interaction(interaction, index=index)

    message = st.chat_input("Enter a message for boundary evaluation…")
    if not message:
        return
    if not patient_id.strip():
        st.warning("Enter a patient ID before sending a message.")
        return

    with st.chat_message("user"):
        st.markdown(message)

    try:
        with st.status("Running Clinical Agent → Boundary Agent → Audit…", expanded=True) as status:
            status.write("Clinical Agent is analyzing the patient context")
            result = client.analyze(patient_id.strip(), message.strip())
            status.write("Boundary Agent is evaluating evidence, authority, and safety")
            audit_id = str(result.get("audit_id", ""))
            audit = client.audit(audit_id)
            status.write("Audit trace loaded")
            interaction = {
                "patient_id": patient_id.strip(),
                "message": message.strip(),
                "clinical_output": result.get("clinical_output", {}),
                "boundary_output": result.get("boundary_output", {}),
                "audit_id": audit_id,
                "audit_record": audit,
            }
            history.append(interaction)
            st.session_state[HISTORY_KEY] = history
            status.update(label="Interaction completed and audited", state="complete")
        _render_interaction(interaction, index=len(history) - 1, show_user=False)
    except Exception as error:
        show_api_error(error)


def _render_interaction(
    interaction: Mapping[str, Any], *, index: int, show_user: bool = True
) -> None:
    """Render one user/agent turn and its boundary evidence."""

    message = str(interaction.get("message", ""))
    clinical = interaction.get("clinical_output", {})
    boundary = interaction.get("boundary_output", {})
    audit = interaction.get("audit_record", {})
    if not isinstance(clinical, Mapping):
        clinical = {}
    if not isinstance(boundary, Mapping):
        boundary = {}
    if not isinstance(audit, Mapping):
        audit = {}

    if show_user:
        with st.chat_message("user"):
            st.markdown(message)

    with st.chat_message("assistant"):
        decision = str(boundary.get("boundary_decision", audit.get("decision", "UNKNOWN")))
        recommendation = str(
            clinical.get("recommendation")
            or clinical.get("analysis")
            or "No agent response was returned."
        )
        st.markdown("**Agent response**")
        st.write(recommendation)
        render_decision_badge(decision)

        score = clinical.get("confidence_score")
        metrics = st.columns(3)
        metrics[0].metric(
            "Confidence score",
            f"{float(score):.0%}" if isinstance(score, (int, float)) else "—",
        )
        metrics[1].metric(
            "Authority required",
            "Yes" if clinical.get("authority_required") else "No",
        )
        metrics[2].metric("Audit", interaction.get("audit_id", "—"))

        if clinical.get("confidence_reason"):
            st.caption(f"Confidence basis: {clinical['confidence_reason']}")

        _render_list("Risks", boundary.get("identified_risks"))
        _render_list("Required actions", boundary.get("required_actions"))

        with st.expander("Clinical analysis and evidence", expanded=False):
            st.markdown("**Analysis**")
            st.write(clinical.get("analysis", "Not available"))
            _render_list("Evidence", clinical.get("evidence"))
            st.markdown("**Reasoning summary**")
            st.write(clinical.get("reasoning", "Not available"))
            _render_list("Uncertainties", clinical.get("uncertainties"))

        with st.expander("Boundary reasoning", expanded=False):
            st.write(boundary.get("boundary_reasoning", "Not available"))

        with st.expander("Full reasoning trace", expanded=True):
            trace = audit.get("reasoning_trace", [])
            if isinstance(trace, Sequence) and not isinstance(trace, (str, bytes)):
                for step_number, step in enumerate(trace, start=1):
                    st.markdown(f"**{step_number}.** {step}")
            else:
                st.caption("No reasoning trace was returned.")

        if audit:
            json_download(
                "Download interaction audit",
                audit,
                f"{interaction.get('audit_id', 'audit')}.json",
                key=f"chat_audit_download_{index}",
            )


def _render_list(title: str, value: Any) -> None:
    """Render a compact string list."""

    st.markdown(f"**{title}**")
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)) and value:
        for item in value:
            st.markdown(f"- {item}")
    else:
        st.caption("None recorded")
