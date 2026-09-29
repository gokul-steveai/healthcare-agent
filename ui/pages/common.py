"""Shared page helpers."""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any

import streamlit as st

from ui.services import APIClientError, APITimeoutError, APIUnavailableError, ResourceNotFoundError


def show_api_error(error: Exception) -> None:
    if isinstance(error, APIUnavailableError):
        st.error("Backend unavailable. Start FastAPI and verify `API_BASE_URL`.")
    elif isinstance(error, APITimeoutError):
        st.warning("The request timed out. The agents may still be processing; try again.")
    elif isinstance(error, ResourceNotFoundError):
        st.warning(f"Requested resource was not found: {error}")
    elif isinstance(error, APIClientError):
        st.error(f"Backend request failed: {error}")
    else:
        st.error("An unexpected frontend error occurred.")


def json_download(label: str, payload: Mapping[str, Any], filename: str, *, key: str) -> None:
    st.download_button(
        label,
        data=json.dumps(payload, ensure_ascii=False, indent=2),
        file_name=filename,
        mime="application/json",
        key=key,
        use_container_width=True,
    )
