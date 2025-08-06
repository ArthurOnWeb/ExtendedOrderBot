from __future__ import annotations

import logging
from typing import Callable, List, Optional


class AlertService:
    """Dispatch textual alerts to subscribed callbacks and the log."""

    def __init__(self, logger: Optional[logging.Logger] = None) -> None:
        self.logger = logger or logging.getLogger(__name__)
        self._subs: List[Callable[[str], None]] = []

    def subscribe(self, callback: Callable[[str], None]) -> None:
        self._subs.append(callback)

    async def send(self, message: str) -> None:
        self.logger.warning("ALERT: %s", message)
        for cb in list(self._subs):
            try:
                cb(message)
            except Exception:  # pragma: no cover - defensive logging
                self.logger.exception("Alert subscriber failed")
