# src/database/repositories.py
from typing import List

from .models import Trade
from .schemas import TradeCreate, TradeResponse

class TradeRepository:
    def __init__(self, session):
        self.session = session
    
    async def create_trade(self, trade_data: dict) -> Trade:
        trade = Trade(**trade_data)
        self.session.add(trade)
        await self.session.commit()
        return trade
    
    async def get_active_trades(self) -> List[Trade]:
        return await self.session.query(Trade).filter(
            Trade.status == 'ACTIVE'
        ).all()
