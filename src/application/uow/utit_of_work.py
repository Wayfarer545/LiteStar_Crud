from abc import abstractmethod, ABC

from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.repositories.sql_user_repository import SqlUserRepository
from src.domain.ports.user_repository import UserRepository


class AbstractUnitOfWork(ABC):
    users: UserRepository

    @abstractmethod
    async def commit(self) -> None:
        pass

    @abstractmethod
    async def rollback(self) -> None:
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            await self.rollback()
        else:
            await self.commit()


class SqlUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: AsyncSession):
        self.session = session
        self.users = SqlUserRepository(session)

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()