# src/database/repositories.py
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

# src/database/schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TradeCreate(BaseModel):
    pair: str
    direction: str
    size: float
    entry_price: Optional[float] = None
    tp_price: Optional[float] = None
    sl_price: Optional[float] = None

class TradeResponse(BaseModel):
    id: str
    pair: str
    direction: str
    size: float
    status: str
    pnl: float
    fees: float
    created_at: datetime
    
    class Config:
        from_attributes = True