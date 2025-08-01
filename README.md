# ExtendedOrderBot

Ce projet fournit un bot simple permettant de lancer des ordres de trading de
manière semi-automatique sur [extended.exchange](https://extended.exchange).

## Installation

Clonez le dépôt et installez les dépendances dans un environnement virtuel:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Les scripts SQL situés dans `src/database/migrations` permettent de créer la base
SQLite par défaut:

```bash
sqlite3 trading_bot.db < src/database/migrations/001_initial_schema.sql
```

## Exemple rapide

Le code suivant crée un trade dans la base en utilisant `TradeRepository`:

```python
import asyncio
from src.database.connection import get_session
from src.database.repositories import TradeRepository

async def main():
    async for session in get_session():
        repo = TradeRepository(session)
        await repo.create_trade({
            "id": "demo",
            "pair": "BTC/USDT",
            "direction": "BUY",
            "size": 1.0,
            "status": "ACTIVE"
        })

asyncio.run(main())
```
