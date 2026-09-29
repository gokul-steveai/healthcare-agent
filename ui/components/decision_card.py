"""Color-coded boundary decision components."""

from __future__ import annotations

import html
import streamlit as st


DECISION_STYLES = {
    "ALLOW": ("🟢", "#137333", "#e6f4ea"),
    "HOLD": ("🟠", "#9a4d00", "#fff1dc"),
    "ESCALATE": ("🟡", "#755600", "#fff8d6"),
    "STOP": ("🔴", "#b3261e", "#fce8e6"),
}


def render_decision_badge(decision: str) -> None:
    """Render a compact boundary-decision badge."""

    normalized = decision.upper()
    emoji, color, background = DECISION_STYLES.get(normalized, ("⚪", "#4b5563", "#f3f4f6"))
    st.markdown(
        f'<span class="decision-badge" style="color:{color};background:{background};">{emoji} {html.escape(normalized)}</span>',
        unsafe_allow_html=True,
    )


def render_decision_card(decision: str, reasoning: str | None = None) -> None:
    """Render a prominent boundary-decision card."""

    normalized = decision.upper()
    emoji, color, background = DECISION_STYLES.get(normalized, ("⚪", "#4b5563", "#f3f4f6"))
    rationale = f'<div class="decision-reason">{html.escape(reasoning)}</div>' if reasoning else ""
    st.markdown(
        f'<div class="decision-card" style="border-color:{color};background:{background};">'
        '<div class="decision-label">Boundary decision</div>'
        f'<div class="decision-value" style="color:{color};">{emoji} {html.escape(normalized)}</div>{rationale}</div>',
        unsafe_allow_html=True,
    )
