from __future__ import annotations

from collections import defaultdict
from typing import Dict


class MetricsCollector:
    """Collect in-memory metrics for the bot.

    The implementation is intentionally lightweight. Metrics are stored in
    dictionaries and can be exported for display on the dashboard or sent to an
    external system if required.
    """

    def __init__(self) -> None:
        self.counters: Dict[str, int] = defaultdict(int)
        self.gauges: Dict[str, float] = {}

    def increment(self, name: str, value: int = 1) -> None:
        self.counters[name] += value

    def set_gauge(self, name: str, value: float) -> None:
        self.gauges[name] = value

    def snapshot(self) -> Dict[str, Dict[str, float]]:
        """Return a copy of all collected metrics."""
        return {"counters": dict(self.counters), "gauges": dict(self.gauges)}
