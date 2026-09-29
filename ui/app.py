"""Streamlit entrypoint for Healthcare AI Boundary Testing."""

from __future__ import annotations

import sys
from pathlib import Path
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from ui.pages import audit_explorer, chat_boundary_lab, dashboard, patient_analysis, scenario_runner
from ui.services import APIClient


st.set_page_config(page_title="Healthcare AI Boundary Testing", page_icon="🛡️", layout="wide", initial_sidebar_state="expanded")


def get_api_client() -> APIClient:
    client = st.session_state.get("api_client")
    if not isinstance(client, APIClient) or not hasattr(client, "review_audit"):
        client = APIClient()
        st.session_state["api_client"] = client
    return client


def _apply_theme() -> None:
    st.markdown(
        """<style>
        :root{--navy:#12324b;--teal:#0f766e}.stApp{background:linear-gradient(180deg,#f8fbfd 0%,#fff 38%);color:#172b3a}
        [data-testid="stSidebarNav"]{display:none!important}
        [data-testid="stSidebar"]{background:#eef5f7;border-right:1px solid #d8e5e9}h1,h2,h3{color:var(--navy);letter-spacing:-.02em}
        [data-testid="stSidebar"] *{color:#172b3a}.stMarkdown,.stCaption,p,label{color:#253746}
        .decision-badge{display:inline-block;padding:.35rem .75rem;border-radius:999px;font-weight:700}.decision-card{border-left:6px solid;border-radius:12px;padding:1rem 1.25rem;margin:.75rem 0 1rem}
        .decision-label{color:#5f6b76;font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em}.decision-value{font-size:1.55rem;font-weight:800;margin:.2rem 0}.decision-reason{color:#25313b;line-height:1.5}
        .architecture-flow{max-width:680px;margin:1rem auto;text-align:center}.flow-node{background:#fff;border:1px solid #cbdde3;border-radius:10px;padding:.65rem;font-weight:700;box-shadow:0 3px 10px rgba(18,50,75,.06)}
        .flow-arrow{color:var(--teal);font-size:1.35rem;line-height:1.35}.flow-decisions{background:#f2f8f7;border:1px solid #bcd9d4;border-radius:10px;padding:.75rem;font-weight:700}
        [data-testid="stMetric"]{background:#fff;border-radius:10px;padding:.75rem}</style>""",
        unsafe_allow_html=True,
    )


def main() -> None:
    _apply_theme()
    client = get_api_client()
    st.sidebar.markdown("## 🛡️ Boundary Testing")
    st.sidebar.caption("Healthcare AI governance research")
    page = st.sidebar.radio("Navigation", ("Dashboard", "Scenario Runner", "Patient Analysis", "Chat Boundary Lab", "Audit Explorer"), label_visibility="collapsed")
    st.sidebar.divider()
    st.sidebar.caption(f"Backend: `{client.base_url}`")
    st.sidebar.warning("Synthetic research environment — not for clinical care.")
    pages = {"Dashboard": dashboard.render, "Scenario Runner": scenario_runner.render, "Patient Analysis": patient_analysis.render, "Chat Boundary Lab": chat_boundary_lab.render, "Audit Explorer": audit_explorer.render}
    pages[page](client)


if __name__ == "__main__":
    main()
