from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from litestar import Litestar
from sqlalchemy.ext.asyncio import create_async_engine

from infrastructure.config import settings


@asynccontextmanager
async def db_connection(app: Litestar) -> AsyncGenerator[None, None]:
    engine = getattr(app.state, "engine", None)
    if engine is None:
        engine = create_async_engine(settings.POSTGRES_DSN)
        app.state.engine = engine
    try:
        yield
    finally:
        await engine.dispose()