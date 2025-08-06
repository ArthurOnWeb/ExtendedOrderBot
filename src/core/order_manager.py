from __future__ import annotations

from typing import Dict, Optional

from .exchange_connector import ExchangeConnector
from .risk_manager import RiskManager


class OrderManager:
    """High level order management including optional risk checks."""

    def __init__(
        self, connector: ExchangeConnector, risk_manager: Optional[RiskManager] = None
    ) -> None:
        self.connector = connector
        self.risk_manager = risk_manager
        self.orders: Dict[str, Dict[str, object]] = {}

    async def create_order(
        self, pair: str, direction: str, size: float, price: Optional[float] = None
    ) -> str:
        """Create an order after verifying risk limits."""
        if self.risk_manager and not self.risk_manager.check_order(pair, size):
            raise ValueError("Risk check failed")
        order_id = await self.connector.send_order(pair, direction, size, price)
        self.orders[order_id] = {
            "pair": pair,
            "direction": direction,
            "size": size,
            "price": price,
            "status": "OPEN",
        }
        if self.risk_manager:
            self.risk_manager.register_order(pair, size)
        return order_id

    async def cancel_order(self, order_id: str) -> bool:
        success = await self.connector.cancel_order(order_id)
        if success and order_id in self.orders:
            self.orders[order_id]["status"] = "CANCELLED"
            if self.risk_manager:
                self.risk_manager.unregister_order(
                    self.orders[order_id]["pair"],
                    self.orders[order_id]["size"],
                )
        return success

    def get_order(self, order_id: str) -> Optional[Dict[str, object]]:
        return self.orders.get(order_id)
