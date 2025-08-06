from __future__ import annotations

from typing import Dict, Optional

from ..core.order_manager import OrderManager
from ..core.risk_manager import RiskManager
from .trailing_stop import TrailingStop


class SemiAutoStrategy:
    """Simple semi-automatic trading strategy.

    Orders are created manually through method calls but the strategy maintains
    optional trailing stops and respects the global kill switch exposed by the
    :class:`~src.core.risk_manager.RiskManager`.
    """

    def __init__(self, order_manager: OrderManager, risk_manager: RiskManager) -> None:
        self.order_manager = order_manager
        self.risk_manager = risk_manager
        self._trailing: Dict[str, TrailingStop] = {}

    async def open_trade(
        self, pair: str, direction: str, size: float, trail: Optional[float] = None
    ) -> str:
        if self.risk_manager.kill_switch:
            raise RuntimeError("Kill switch active")
        order_id = await self.order_manager.create_order(pair, direction, size)
        if trail is not None:
            self._trailing[order_id] = TrailingStop(trail)
        return order_id

    async def on_price(self, order_id: str, price: float) -> bool:
        """Update trailing stop with the latest ``price``.

        Returns ``True`` if the trailing stop triggers and the order is cancelled.
        """
        ts = self._trailing.get(order_id)
        if not ts:
            return False
        stop = ts.update(price)
        if ts.hit(price) and self.risk_manager.check_stop(price, stop):
            await self.order_manager.cancel_order(order_id)
            self._trailing.pop(order_id, None)
            return True
        return False

    async def close_trade(self, order_id: str) -> None:
        await self.order_manager.cancel_order(order_id)
        self._trailing.pop(order_id, None)
