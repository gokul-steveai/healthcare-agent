"""Audit Explorer page."""

from collections.abc import Mapping
import pandas as pd
import streamlit as st
from ui.components import render_audit_viewer
from ui.pages.common import json_download, show_api_error
from ui.services import APIClient


def render(client: APIClient) -> None:
    st.title("Audit Explorer")
    st.caption("Inspect immutable evidence, decisions, and reasoning summaries.")
    if st.button("Refresh audits"):
        st.session_state.pop("audit_summaries", None)
    if "audit_summaries" not in st.session_state:
        try:
            st.session_state["audit_summaries"] = client.audits()
        except Exception as error:
            show_api_error(error)
            return
    audits = st.session_state.get("audit_summaries", [])
    if not isinstance(audits, list) or not audits:
        st.info("No audit records are available yet.")
        return
    table = pd.DataFrame(audits).rename(columns={"audit_id": "Audit ID", "scenario_id": "Scenario", "decision": "Decision", "timestamp": "Timestamp"})
    columns = [column for column in ("Audit ID", "Scenario", "Decision", "Timestamp") if column in table.columns]
    st.dataframe(table[columns], use_container_width=True, hide_index=True)
    by_id = {str(item["audit_id"]): item for item in audits}
    selected_id = st.selectbox("Select Audit", list(by_id), format_func=lambda value: f"{by_id[value].get('decision', '—')} · {by_id[value].get('scenario_id', '—')} · {value}")
    if st.button("Load Audit", type="primary", use_container_width=True):
        try:
            with st.status("Loading audit record…", expanded=False) as status:
                st.session_state["selected_audit"] = client.audit(selected_id)
                status.update(label="Audit loaded", state="complete")
        except Exception as error:
            show_api_error(error)
    audit = st.session_state.get("selected_audit")
    if isinstance(audit, Mapping):
        st.divider()
        st.markdown("### Audit Details")
        render_audit_viewer(audit, api_client=client)
        json_download("Download Audit JSON", audit, f"{audit.get('audit_id', 'audit')}.json", key="explorer_audit_download")
