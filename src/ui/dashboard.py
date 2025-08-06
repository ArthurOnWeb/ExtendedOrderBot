from __future__ import annotations

from typing import Optional

from ..core.order_manager import OrderManager
from ..core.portfolio_tracker import PortfolioTracker
from .alerts import AlertService


class Dashboard:
    """Very small textual dashboard for the trading bot."""

    def __init__(
        self,
        portfolio: PortfolioTracker,
        orders: OrderManager,
        alerts: Optional[AlertService] = None,
    ) -> None:
        self.portfolio = portfolio
        self.orders = orders
        self.alerts = alerts

    async def render(self) -> str:
        balances = ", ".join(
            f"{asset}: {amount:.2f}" for asset, amount in self.portfolio.balances.items()
        ) or "no balances"
        open_orders = [o for o in self.orders.orders.values() if o.get("status") == "OPEN"]
        dashboard = f"Balances: {balances} | Open orders: {len(open_orders)}"
        if self.alerts:
            await self.alerts.send("Dashboard refreshed")
        return dashboard
