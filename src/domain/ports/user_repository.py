from abc import ABC, abstractmethod

from domain.specifications.user_specs import UserSpecification
from domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    async def add(self, user: User) -> User:
        ...

    @abstractmethod
    async def get(self, spec: UserSpecification) -> User | None:
        ...

    @abstractmethod
    async def get_list(self, ) -> list[User] | None:
        ...

    @abstractmethod
    async def update(self, user: User) -> User:
        ...

    @abstractmethod
    async def delete(self, user_id: int) -> None:
        ...