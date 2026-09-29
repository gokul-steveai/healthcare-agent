"""Scenario Runner page."""

from collections.abc import Mapping
import streamlit as st
from ui.components import render_audit_viewer, render_decision_card
from ui.pages.common import json_download, show_api_error
from ui.services import APIClient


def render(client: APIClient) -> None:
    st.title("Scenario Runner")
    st.caption("Run predefined cases without exposing expected labels to the agents.")
    try:
        scenarios = client.scenarios()
    except Exception as error:
        show_api_error(error)
        return
    if not scenarios:
        st.info("No scenarios are currently available.")
        return
    by_id = {str(item["scenario_id"]): item for item in scenarios}
    decision_order = {"allow": 0, "hold": 1, "escalate": 2, "stop": 3}
    options = sorted(by_id, key=lambda value: (decision_order.get(value, 99), value))
    selected_id = st.selectbox("Boundary test scenario", options, format_func=lambda value: value.upper())
    selected = by_id[selected_id]
    with st.expander("Scenario input", expanded=True):
        st.markdown(f"**Patient ID:** `{selected.get('patient_id', '—')}`")
        st.write(selected.get("user_request", ""))
    if st.button("Run Scenario", type="primary", use_container_width=True):
        try:
            with st.status("Executing multi-agent pipeline…", expanded=True) as status:
                result = client.run_scenario(selected_id)
                status.write("Loading complete audit trace")
                audit = client.audit(str(result["audit_id"]))
                st.session_state["scenario_result"], st.session_state["scenario_audit"] = result, audit
                status.update(label="Scenario completed", state="complete")
        except Exception as error:
            show_api_error(error)
    result, audit = st.session_state.get("scenario_result"), st.session_state.get("scenario_audit")
    if not isinstance(result, Mapping) or not isinstance(audit, Mapping):
        return

    audit_id = audit.get("audit_id") or result.get("audit_id")
    if audit_id and "human_review" not in audit:
        try:
            latest = client.audit(str(audit_id))
            if latest.get("human_review"):
                audit = latest
                st.session_state["scenario_audit"] = latest
        except Exception:
            pass

    st.divider()
    columns = st.columns(3)
    columns[0].metric("Scenario ID", result.get("scenario_id", "—"))
    columns[1].metric("Boundary decision", result.get("boundary_decision", "—"))
    hr = audit.get("human_review")
    status_label = f"Reviewed ({hr.get('decision')})" if hr else result.get("status", "—")
    columns[2].metric("Status", status_label)
    st.code(str(result.get("audit_id", "")), language=None)
    render_audit_viewer(audit, api_client=client)
    json_download("Download Audit JSON", audit, f"{audit.get('audit_id', 'audit')}.json", key="scenario_audit_download")
