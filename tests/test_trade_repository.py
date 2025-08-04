import os
import sys

import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.database.models import Base
from src.database.repositories import TradeRepository
from src.database.schemas import TradeCreate


@pytest.mark.asyncio
async def test_create_and_get_active_trade():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async with AsyncSessionLocal() as session:
        repo = TradeRepository(session)
        trade_data = TradeCreate(
            id="t1",
            pair="BTC/USDT",
            direction="LONG",
            size=1.0,
            status="ACTIVE",
        )
        await repo.create_trade(trade_data)

        active_trades = await repo.get_active_trades()
        assert len(active_trades) == 1
        assert active_trades[0].id == "t1"
