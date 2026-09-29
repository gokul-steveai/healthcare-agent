"""Environment configuration for the boundary-testing platform."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = PROJECT_ROOT / ".env"


def load_project_environment() -> None:
    """Load local project settings without overriding process environment."""

    load_dotenv(dotenv_path=ENV_FILE, override=False)


def get_gemini_api_key() -> str | None:
    """Return the configured Gemini API key, excluding placeholder values."""

    load_project_environment()
    value = os.environ.get("GEMINI_API_KEY", "").strip()
    if not value or value.lower() in {
        "your_gemini_api_key_here",
        "paste_your_gemini_api_key_here",
    }:
        return None
    return value


load_project_environment()
