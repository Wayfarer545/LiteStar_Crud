from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from application.uow.utit_of_work import SqlUnitOfWork
from src.infrastructure.config import settings


engine = create_async_engine(
    settings.POSTGRES_DSN,
    pool_pre_ping=True,
    echo=False,
    future=True,
)

async def get_uow() -> AsyncGenerator[SqlUnitOfWork, Any]:
    async with AsyncSession(engine) as session:
        yield SqlUnitOfWork(session)