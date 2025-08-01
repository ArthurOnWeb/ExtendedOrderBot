-- src/database/migrations/002_add_indexes.sql
CREATE INDEX idx_trades_status ON trades(status);
CREATE INDEX idx_trades_pair ON trades(pair);
CREATE INDEX idx_trades_created_at ON trades(created_at);
CREATE INDEX idx_orders_trade_id ON orders(trade_id);
CREATE INDEX idx_orders_status ON orders(status);