from litestar import Controller, Router, get, post, put, delete
from litestar.di import Provide
from litestar.dto import DataclassDTO, DTOConfig
from litestar.exceptions import NotFoundException

from application.uow.utit_of_work import AbstractUnitOfWork
from domain.entities.user import User
from domain.specifications.user_specs import UserByIdSpecification
from infrastructure.db.database import get_uow


class UserWriteDTO(DataclassDTO[User]): ...


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

    @get("/{user_id:int}")
    async def get_user(self, user_id: int, uow: AbstractUnitOfWork) -> User:
        id_spec = UserByIdSpecification(user_id)
        async with uow:
            user = await uow.users.get(id_spec)
            if user is None:
                raise NotFoundException
            return user


    @put("/{user_id:int}")
    async def update_user(self, data: User, uow: AbstractUnitOfWork) -> User:
        ...

    @delete("/{user_id:int}", return_dto=None)
    async def delete_user(self, user_id: int, uow: AbstractUnitOfWork) -> None:
        ...


users_router = Router(
    path="/users",
    dependencies={},
    route_handlers=[UserController],
)
