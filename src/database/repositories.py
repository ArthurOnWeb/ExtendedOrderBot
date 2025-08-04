# src/database/repositories.py
from typing import List

from sqlalchemy import select

from .models import Trade
from .schemas import TradeCreate

class TradeRepository:
    def __init__(self, session):
        self.session = session
    
    async def create_trade(self, trade_data: TradeCreate) -> Trade:
        trade_dict = trade_data.model_dump()
        trade = Trade(**trade_dict)
        self.session.add(trade)
        await self.session.commit()
        await self.session.refresh(trade)
        return trade
    
    async def get_active_trades(self) -> List[Trade]:
        result = await self.session.execute(
            select(Trade).where(Trade.status == 'ACTIVE')
        )
        return result.scalars().all()
