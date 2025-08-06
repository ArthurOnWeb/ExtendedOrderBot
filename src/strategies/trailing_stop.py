from __future__ import annotations

from typing import Optional


class TrailingStop:
    """Maintain a trailing stop price for an open position."""

    def __init__(self, distance: float) -> None:
        self.distance = distance
        self._peak: float = float("-inf")
        self._stop: Optional[float] = None

    def update(self, price: float) -> float:
        """Update internal state with the latest ``price`` and return the stop."""
        if price > self._peak:
            self._peak = price
            self._stop = price - self.distance
        elif self._stop is None:
            self._stop = price - self.distance
        return self._stop

    def hit(self, price: float) -> bool:
        """Return ``True`` if the trailing stop would trigger at ``price``."""
        return self._stop is not None and price <= self._stop
