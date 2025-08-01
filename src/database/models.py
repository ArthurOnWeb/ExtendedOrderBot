# src/database/models.py
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Trade(Base):
    __tablename__ = 'trades'
    id = Column(String, primary_key=True)
    pair = Column(String, nullable=False)
    direction = Column(String, nullable=False)
    size = Column(Float, nullable=False)
    entry_price = Column(Float)
    tp_price = Column(Float)
    sl_price = Column(Float)
    status = Column(String, nullable=False)
    pnl = Column(Float, default=0)
    fees = Column(Float, default=0)
    created_at = Column(DateTime)
    closed_at = Column(DateTime)

    orders = relationship("Order", back_populates="trade")

class Order(Base):
    __tablename__ = 'orders'
    id = Column(String, primary_key=True)
    trade_id = Column(String, ForeignKey('trades.id', ondelete='CASCADE'))
    type = Column(String, nullable=False)
    side = Column(String, nullable=False)
    size = Column(Float, nullable=False)
    price = Column(Float)
    status = Column(String, nullable=False)
    exchange_id = Column(String)
    timestamp = Column(DateTime)

    trade = relationship("Trade", back_populates="orders")
