from __future__ import annotations

from typing import Dict


class RiskManager:
    """Basic risk control features including a kill switch."""

    def __init__(self, max_position: float = float("inf")) -> None:
        self.max_position = max_position
        self.kill_switch = False
        self._positions: Dict[str, float] = {}

    def check_order(self, pair: str, size: float) -> bool:
        """Return ``True`` if placing an order of ``size`` is allowed."""
        if self.kill_switch:
            return False
        current = self._positions.get(pair, 0.0)
        return current + size <= self.max_position

    def register_order(self, pair: str, size: float) -> None:
        self._positions[pair] = self._positions.get(pair, 0.0) + size

    def unregister_order(self, pair: str, size: float) -> None:
        self._positions[pair] = self._positions.get(pair, 0.0) - size

    def activate_kill_switch(self) -> None:
        self.kill_switch = True

    def deactivate_kill_switch(self) -> None:
        self.kill_switch = False

    def check_stop(self, price: float, stop_price: float) -> bool:
        """Return ``True`` when the stop should trigger."""
        return price <= stop_price
