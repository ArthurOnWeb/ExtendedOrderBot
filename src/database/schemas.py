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
