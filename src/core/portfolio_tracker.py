from __future__ import annotations

from typing import Dict


class PortfolioTracker:
    """Track account balances and positions in memory."""

    def __init__(self) -> None:
        self.balances: Dict[str, float] = {}
        self.positions: Dict[str, float] = {}

    def update_balance(self, asset: str, amount: float) -> None:
        self.balances[asset] = self.balances.get(asset, 0.0) + amount

    def get_balance(self, asset: str) -> float:
        return self.balances.get(asset, 0.0)

    def update_position(self, pair: str, size: float) -> None:
        self.positions[pair] = self.positions.get(pair, 0.0) + size

    def get_position(self, pair: str) -> float:
        return self.positions.get(pair, 0.0)
