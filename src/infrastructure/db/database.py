from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.infrastructure.config import settings

engine = create_async_engine(settings.POSTGRES_DSN, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)