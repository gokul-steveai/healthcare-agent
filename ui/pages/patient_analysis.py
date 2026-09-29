"""Patient Analysis page."""

from collections.abc import Mapping
import streamlit as st
from ui.components import render_audit_viewer, render_boundary_output, render_clinical_output
from ui.pages.common import json_download, show_api_error
from ui.services import APIClient


def render(client: APIClient) -> None:
    st.title("Patient Analysis")
    st.caption("Submit a synthetic patient-context question for boundary evaluation.")
    with st.form("patient_analysis_form"):
        patient_id = st.text_input("Patient ID", value="2c71dd97-7085-416a-aa07-d675bbe3adf2")
        user_request = st.text_area("User Request", value="My kidney measurements changed. Should I stop metformin?", height=130)
        submitted = st.form_submit_button("Analyze", type="primary", use_container_width=True)
    if submitted:
        if not patient_id.strip() or not user_request.strip():
            st.warning("Patient ID and user request are required.")
        else:
            try:
                with st.status("Analyzing patient context…", expanded=True) as status:
                    result = client.analyze(patient_id.strip(), user_request.strip())
                    st.session_state["analysis_result"] = result
                    status.update(label="Analysis completed", state="complete")
            except Exception as error:
                show_api_error(error)
    result = st.session_state.get("analysis_result")
    if not isinstance(result, Mapping):
        return
    st.divider()
    audit_id = result.get("audit_id")
    if audit_id:
        try:
            audit = client.audit(str(audit_id))
            render_audit_viewer(audit, api_client=client)
            json_download("Download Audit JSON", audit, f"{audit_id}.json", key="analysis_download")
            return
        except Exception:
            pass

    clinical, boundary = result.get("clinical_output", {}), result.get("boundary_output", {})
    if isinstance(clinical, Mapping):
        render_clinical_output(clinical)
    if isinstance(boundary, Mapping):
        render_boundary_output(boundary)
    st.markdown("#### Audit ID")
    st.code(str(result.get("audit_id", "")), language=None)
    json_download("Download Analysis JSON", result, f"analysis_{result.get('audit_id', 'result')}.json", key="analysis_download")
