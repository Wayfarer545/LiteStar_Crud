import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

from src.infrastructure.config import settings
from src.infrastructure.db.models import BigIntAuditBase, User

engine = create_async_engine(settings.POSTGRES_DSN, echo=False)

config = context.config
config.set_main_option("sqlalchemy.url", settings.POSTGRES_DSN)


if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = BigIntAuditBase.metadata


def run_migrations_offline():
    """Запуск миграций в оффлайн-режиме (без подключения к БД)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online_async():
    """Запуск миграций в онлайн-режиме для асинхронного движка."""
    async with engine.connect() as connection:
        await connection.run_sync(
            lambda conn: context.configure(connection=conn, target_metadata=target_metadata)
        )
        async with connection.begin():
            await connection.run_sync(lambda conn: context.run_migrations())

def run_migrations_online():
    """Синхронная обёртка для асинхронных миграций."""
    asyncio.run(run_migrations_online_async())

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
