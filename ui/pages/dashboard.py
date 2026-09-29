"""Dashboard page."""

import streamlit as st
from ui.pages.common import show_api_error
from ui.services import APIClient


def render(client: APIClient) -> None:
    st.title("Healthcare AI Boundary Testing")
    st.caption("Research interface for evidence, authority, and safety boundaries. Not a healthcare application.")
    try:
        with st.status("Checking platform services…", expanded=False) as status:
            health, scenarios, audits = client.health(), client.scenarios(), client.audits()
            status.update(label="Platform connected", state="complete")
    except Exception as error:
        show_api_error(error)
        health, scenarios, audits = {"status": "unavailable"}, [], []
    columns = st.columns(4)
    columns[0].metric("System status", "Healthy" if health.get("status") == "healthy" else "Unavailable", border=True)
    columns[1].metric("Total scenarios", len(scenarios), border=True)
    columns[2].metric("Total audits", len(audits), border=True)
    columns[3].metric("Recon.AI Governance", "Active (TrustGuard)", border=True)
    st.markdown("### Agent & Governance Architecture")
    st.markdown(
        '<div class="architecture-flow">'
        '<div class="flow-node">Patient Context</div><div class="flow-arrow">↓</div>'
        '<div class="flow-node">Clinical Agent (Recon TrustGuard)</div><div class="flow-arrow">↓</div>'
        '<div class="flow-node">Recon GhostLog Timeline &amp; Gates</div><div class="flow-arrow">↓</div>'
        '<div class="flow-node">Boundary Agent (ALLOW / HOLD / ESCALATE / STOP)</div><div class="flow-arrow">↓</div>'
        '<div class="flow-node">Audit Record &amp; Recon Trust Receipt</div><div class="flow-arrow">↓</div>'
        '<div class="flow-node" style="border: 2px solid #3b82f6;">Human-in-the-Loop Review (Physician Sign-Off)</div>'
        '</div>',
        unsafe_allow_html=True,
    )
    st.markdown("### What this platform evaluates")
    cards = st.columns(3)
    cards[0].info("**Evidence grounding**\n\nDoes the agent use supplied records faithfully without hallucination?")
    cards[1].info("**Authority & Policy Boundaries**\n\nRecon TrustGuard intercepts clinical markers and enforces policy gates.")
    cards[2].info("**Safety & HITL Governance**\n\nHOLD/ESCALATE states require authorized clinician sign-off with defensible Trust Receipts.")
