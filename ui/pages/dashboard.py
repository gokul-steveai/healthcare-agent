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
    columns = st.columns(3)
    columns[0].metric("System status", "Healthy" if health.get("status") == "healthy" else "Unavailable", border=True)
    columns[1].metric("Total scenarios", len(scenarios), border=True)
    columns[2].metric("Total audits", len(audits), border=True)
    st.markdown("### Agent workflow")
    st.markdown(
        '<div class="architecture-flow"><div class="flow-node">Patient Context</div><div class="flow-arrow">↓</div>'
        '<div class="flow-node">Clinical Agent</div><div class="flow-arrow">↓</div><div class="flow-node">Boundary Agent</div>'
        '<div class="flow-arrow">↓</div><div class="flow-decisions">🟢 ALLOW &nbsp; 🟠 HOLD &nbsp; 🟡 ESCALATE &nbsp; 🔴 STOP</div>'
        '<div class="flow-arrow">↓</div><div class="flow-node">Audit Trail</div></div>',
        unsafe_allow_html=True,
    )
    st.markdown("### What this platform evaluates")
    cards = st.columns(3)
    cards[0].info("**Evidence grounding**\n\nDoes the agent use supplied records faithfully?")
    cards[1].info("**Authority boundaries**\n\nDoes it avoid unsupported clinical action?")
    cards[2].info("**Safety governance**\n\nDoes it hold, escalate, or stop appropriately?")
