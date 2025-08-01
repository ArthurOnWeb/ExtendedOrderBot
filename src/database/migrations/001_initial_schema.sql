-- src/database/migrations/001_initial_schema.sql
CREATE TABLE trades (
    id TEXT PRIMARY KEY,
    pair TEXT NOT NULL,
    direction TEXT NOT NULL,
    size REAL NOT NULL,
    entry_price REAL,
    tp_price REAL,
    sl_price REAL,
    status TEXT NOT NULL,
    pnl REAL DEFAULT 0,
    fees REAL DEFAULT 0,
    created_at TIMESTAMP,
    closed_at TIMESTAMP
);

CREATE TABLE orders (
    id TEXT PRIMARY KEY,
    trade_id TEXT,
    type TEXT NOT NULL,
    side TEXT NOT NULL,
    size REAL NOT NULL,
    price REAL,
    status TEXT NOT NULL,
    exchange_id TEXT,
    timestamp TIMESTAMP,
    FOREIGN KEY (trade_id) REFERENCES trades(id) ON DELETE CASCADE
);
