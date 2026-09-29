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


def render_recon_receipt_card(receipt: Mapping[str, Any]) -> None:
    """Render an enterprise-grade Recon Trust Receipt badge."""

    st.markdown("---")
    st.markdown("#### 🛡️ Recon.AI Trust Receipt & Attestation")
    c1, c2, c3 = st.columns(3)
    decision = str(receipt.get("decision", "permit")).upper()
    c1.metric("Policy Status", decision)
    c2.metric("Governance Mode", str(receipt.get("governance_mode", "dry_run")).upper())
    c3.metric("Receipt ID", str(receipt.get("receipt_id", "—"))[:16] + "...")
    st.caption(f"Correlation ID: `{receipt.get('correlation_id', '—')}` · Policy: `{receipt.get('policy_id', '—')}`")

    rc1, rc2 = st.columns(2)
    if receipt.get("receipt_url"):
        rc1.markdown(f"[📄 View Trust Receipt on Recon.AI]({receipt['receipt_url']})")
    if receipt.get("ledger_url"):
        rc2.markdown(f"[⛓️ Confirm Entry in GhostLog Ledger]({receipt['ledger_url']})")


def render_human_review_panel(audit: Mapping[str, Any], api_client: Any | None = None) -> None:
    """Render the Human-In-The-Loop (HITL) Review Panel."""

    human_review = audit.get("human_review")
    decision = str(audit.get("decision", ""))

    if human_review:
        st.markdown("---")
        st.markdown("#### 👨‍⚕️ Human-in-the-Loop Sign-Off Status")
        res = str(human_review.get("decision", "APPROVED"))
        icon = "✅" if res == "APPROVED" else "❌" if res == "REJECTED" else "📋"
        st.success(f"{icon} Review Outcome: **{res}** by **{human_review.get('reviewer_name')}** ({human_review.get('reviewer_role')}) at {human_review.get('timestamp')}")
        if human_review.get("notes"):
            st.info(f"**Clinical Reviewer Notes:** {human_review['notes']}")
        return

    # If pending review (HOLD or ESCALATE)
    if decision in ("HOLD", "ESCALATE"):
        st.markdown("---")
        st.markdown("#### 👨‍⚕️ Clinical Human-in-the-Loop Sign-Off")
        st.warning(f"This case was flagged as **{decision}** and requires authorized human review before clinical action.")

        audit_id = str(audit.get("audit_id", ""))
        with st.container():
            col1, col2 = st.columns([1, 1])
            with col1:
                name = st.text_input("Reviewer Name", value="Dr. Alex Rivera, MD", key=f"rev_name_{audit_id}")
            with col2:
                role = st.selectbox(
                    "Clinical Role",
                    ["Attending Physician (MD/DO)", "Clinical Nurse Specialist (CNS/RN)", "Clinical Pharmacist (PharmD)", "Clinical SME"],
                    key=f"rev_role_{audit_id}",
                )
            notes = st.text_input("Reviewer Notes / Guidance", placeholder="e.g. Approved continuation of current regimen; lab recheck ordered.", key=f"rev_notes_{audit_id}")

            from ui.services import APIClient

            active_client = (
                api_client
                if (api_client is not None and hasattr(api_client, "review_audit"))
                else APIClient()
            )

            def _sync_audit_state(updated_record: Mapping[str, Any]) -> None:
                st.session_state["selected_audit"] = updated_record
                st.session_state["scenario_audit"] = updated_record
                st.session_state["analysis_audit"] = updated_record
                st.session_state.pop("audit_summaries", None)

            b1, b2, b3 = st.columns(3)

            if b1.button("✅ Authorize & Approve", use_container_width=True, type="primary", key=f"btn_app_{audit_id}"):
                if audit_id:
                    try:
                        updated = active_client.review_audit(audit_id, name, role, "APPROVED", notes)
                        _sync_audit_state(updated)
                        st.success("Human authorization signed off and recorded in Recon GhostLog!")
                        st.rerun()
                    except Exception as exc:
                        st.error(f"Sign-off failed: {exc}")

            if b2.button("❌ Reject Proposal", use_container_width=True, key=f"btn_rej_{audit_id}"):
                if audit_id:
                    try:
                        updated = active_client.review_audit(audit_id, name, role, "REJECTED", notes)
                        _sync_audit_state(updated)
                        st.warning("Action rejected and logged in Recon GhostLog.")
                        st.rerun()
                    except Exception as exc:
                        st.error(f"Rejection failed: {exc}")

            if b3.button("📋 Request New Labs", use_container_width=True, key=f"btn_req_{audit_id}"):
                if audit_id:
                    try:
                        updated = active_client.review_audit(audit_id, name, role, "REQUEST_INFO", notes)
                        _sync_audit_state(updated)
                        st.info("Additional clinical lab requested.")
                        st.rerun()
                    except Exception as exc:
                        st.error(f"Request failed: {exc}")


def render_audit_viewer(audit: Mapping[str, Any], api_client: Any | None = None) -> None:
    """Render a complete audit record."""

    columns = st.columns(4)
    columns[0].metric("Decision", audit.get("decision", "—"))
    columns[1].metric("Scenario", audit.get("scenario_id", "—"))
    columns[2].metric("Patient", audit.get("patient_id", "—"))
    columns[3].metric("Version", audit.get("version", "—"))
    st.caption(f"Audit ID: {audit.get('audit_id', '—')} · {audit.get('timestamp', '—')}")

    if audit.get("recon_receipt"):
        render_recon_receipt_card(audit["recon_receipt"])

    render_human_review_panel(audit, api_client=api_client)

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
    if audit.get("recon_ghostlog"):
        with st.expander("🛡️ Recon.AI Execution Timeline (GhostLog)"):
            st.caption("In-process governance trace recorded by Recon TrustGuard")
            for entry in audit["recon_ghostlog"]:
                step_num = entry.get("step", "—")
                kind = entry.get("kind", "event")
                data = entry.get("data", {})
                st.markdown(f"**Step {step_num}: `{kind}`**")
                if "preview" in data:
                    st.text(data["preview"])
                elif "score" in data:
                    st.json(data["score"])
                elif "reason" in data:
                    st.info(f"Gate trigger: {data['reason']}")
                elif data:
                    st.json(data)
    with st.expander("Raw audit JSON"):
        st.json(dict(audit))
        st.code(json.dumps(audit, indent=2), language="json")
