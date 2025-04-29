from litestar import Controller, Router, get, post, put, delete
from litestar.di import Provide
from litestar.dto import DataclassDTO, DTOConfig

from src.application.uow.utit_of_work import AbstractUnitOfWork
from src.domain.entities.user import User
from src.domain.specifications.user_specs import UserByIdSpecification
from src.infrastructure.db.database import get_uow
from src.presentation.exceptions import UserNotFoundError


class UserWriteDTO(DataclassDTO[User]):
    config = DTOConfig(exclude={"id", "created_at", "updated_at"})


class UserReadDTO(DataclassDTO[User]):
    config = DTOConfig(exclude={"password"})


class UserController(Controller):
    dependencies = {"uow": Provide(get_uow)}
    dto = UserWriteDTO
    return_dto = UserReadDTO

    @post("/")
    async def create_user(self, data: User, uow: AbstractUnitOfWork) -> User:
        async with uow:
            return await uow.users.add(data)

    @get("/list")
    async def get_users(self, uow: AbstractUnitOfWork) -> list[User]:
        async with uow:
            return await uow.users.get_list()

    @get("/{user_id:int}", raises=[UserNotFoundError])
    async def get_user(self, user_id: int, uow: AbstractUnitOfWork) -> User:
        id_spec = UserByIdSpecification(user_id)
        async with uow:
            user = await uow.users.get(id_spec)
            if user is None:
                raise UserNotFoundError
            return user

    @put("/{user_id:int}", raises=[UserNotFoundError])
    async def update_user(self, user_id: int, data: User, uow: AbstractUnitOfWork) -> User:
        async with uow:
            updated_user = await uow.users.update(user_id, data)
            if updated_user is None:
                raise UserNotFoundError
            return updated_user

    @delete("/{user_id:int}",return_dto=None)
    async def delete_user(self, user_id: int, uow: AbstractUnitOfWork) -> None:
        async with uow:
            if not await uow.users.delete(user_id):
                raise UserNotFoundError


users_router = Router(
    path="/users",
    dependencies={},
    route_handlers=[UserController],
)
