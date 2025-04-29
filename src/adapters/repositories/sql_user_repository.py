from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.domain.specifications.user_specs import UserSpecification
from src.domain.entities.user import User as UserEntity
from src.domain.ports.user_repository import UserRepository
from src.infrastructure.db.models import User as UserModel


class SqlUserRepository(UserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, user: UserEntity) -> UserEntity:
        db_user = UserModel(
            name=user.name,
            surname=user.surname,
            password=user.password,
        )
        self.session.add(db_user)
        await self.session.flush()
        user.id = db_user.id
        user.created_at = db_user.created_at
        user.updated_at = db_user.updated_at
        return user

    async def get(self, spec: UserSpecification) -> UserEntity | None:
        statement = spec.to_query(select(UserModel))
        result = await self.session.execute(statement)
        if user := result.scalars().first():
            return UserEntity(
                id=user.id,
                name=user.name,
                surname=user.surname,
                password=user.password,
                created_at=user.created_at,
                updated_at=user.updated_at
            )
        return None

    async def get_list(self) -> list[UserEntity] | None:
        statement = select(UserModel)
        result = await self.session.execute(statement)
        return [
            UserEntity(
                id=user.id,
                name=user.name,
                surname=user.surname,
                password=user.password,
                created_at=user.created_at,
                updated_at=user.updated_at
            ) for user in result.scalars().all()]

    async def update(self, user_id: int, user: UserEntity) -> UserEntity | None:
        db_user = await self.session.get(UserModel, user_id)
        if db_user is None:
            return None
        db_user.name = user.name
        db_user.surname = user.surname
        db_user.password = user.password
        await self.session.flush()
        await self.session.refresh(db_user)
        updated_user_dict = db_user.__dict__
        user.id = updated_user_dict["id"]
        user.created_at = updated_user_dict["created_at"]
        user.updated_at = updated_user_dict["updated_at"]
        return user

    async def delete(self, user_id: int) -> bool:
        db_user = await self.session.get(UserModel, user_id)
        if db_user:
            await self.session.delete(db_user)
            await self.session.flush()
            return True
        return False


