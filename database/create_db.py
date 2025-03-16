import asyncio

from database import async_engine
from models import Base


async def create_db():
    async with async_engine.begin() as conn:
        from models import ShortenURL

        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    await async_engine.dispose()
