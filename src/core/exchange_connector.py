from __future__ import annotations

import asyncio
import logging
import random
import uuid
from typing import Dict, Optional


class ExchangeConnector:
    """Tiny wrapper simulating connectivity with an exchange API.

    The implementation does not perform real HTTP requests.  Instead it keeps an
    in-memory representation of orders which is sufficient for unit tests and
    development without network access.
    """

    def __init__(self, api_url: str, logger: Optional[logging.Logger] = None) -> None:
        self.api_url = api_url
        self.logger = logger or logging.getLogger(__name__)
        self._orders: Dict[str, Dict[str, object]] = {}

    async def fetch_ticker(self, pair: str) -> float:
        """Return a pseudo random price for ``pair``.

        In a production ready bot this method would request the latest ticker
        from the exchange.  Here we simply return a deterministic pseudo-random
        value to keep the module functional offline.
        """
        await asyncio.sleep(0)
        price = random.uniform(10, 100)
        self.logger.debug("Fetched ticker for %s: %.2f", pair, price)
        return price

    async def send_order(
        self, pair: str, direction: str, size: float, price: Optional[float] = None
    ) -> str:
        """Send an order to the (simulated) exchange and return its id."""
        await asyncio.sleep(0)
        order_id = str(uuid.uuid4())
        self._orders[order_id] = {
            "pair": pair,
            "direction": direction,
            "size": size,
            "price": price,
            "status": "OPEN",
        }
        self.logger.info(
            "Order %s created: %s %.4f %s", order_id, direction, size, pair
        )
        return order_id

    async def cancel_order(self, order_id: str) -> bool:
        """Cancel an order by id."""
        await asyncio.sleep(0)
        order = self._orders.get(order_id)
        if not order or order["status"] != "OPEN":
            return False
        order["status"] = "CANCELLED"
        self.logger.info("Order %s cancelled", order_id)
        return True

    async def get_order(self, order_id: str) -> Optional[Dict[str, object]]:
        await asyncio.sleep(0)
        return self._orders.get(order_id)
