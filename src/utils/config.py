from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    """Application configuration loaded from a file or environment variables."""

    api_url: str = "https://extended.exchange/api"
    max_position: float = 10.0
    log_level: str = "INFO"
    kill_switch: bool = False


def _parse_bool(value: str) -> bool:
    return value.lower() in {"1", "true", "yes", "on"}


def load_config(path: Optional[str] = None) -> Config:
    """Load configuration from ``path`` overriding values with environment variables."""

    data: dict[str, object] = {}
    if path and os.path.exists(path):
        with open(path) as f:
            data.update(json.load(f))

    api_url = os.getenv("API_URL", data.get("api_url", Config.api_url))
    max_position = float(
        os.getenv("MAX_POSITION", data.get("max_position", Config.max_position))
    )
    log_level = os.getenv("LOG_LEVEL", data.get("log_level", Config.log_level))
    kill_switch = os.getenv(
        "KILL_SWITCH", str(data.get("kill_switch", Config.kill_switch))
    )

    return Config(
        api_url=api_url,
        max_position=max_position,
        log_level=log_level,
        kill_switch=_parse_bool(str(kill_switch)),
    )
