from litestar import Controller, Router, get, post, put, delete
from litestar.di import Provide
from litestar.dto import DataclassDTO, DTOConfig

from domain.entities.user import User


class UserWriteDTO(DataclassDTO[User]):
    config = DTOConfig(exclude={"id"})


class UserReadDTO(DataclassDTO[User]): ...


class UserController(Controller):
    dto = UserWriteDTO
    return_dto = UserReadDTO

    @post("/", sync_to_thread=False)
    def create_user(self, data: User) -> User:
        ...

    @get("/", sync_to_thread=False)
    def get_users(self) -> list[User]:
        ...

    @get("/{user_id:uuid}", sync_to_thread=False)
    def get_user(self, user_id: int) -> User:
        ...

    @put("/{user_id:uuid}", sync_to_thread=False)
    def update_user(self, data: User) -> User:
        ...

    @delete("/{user_id:uuid}", return_dto=None, sync_to_thread=False)
    def delete_user(self, user_id: int) -> None:
        ...


users_router = Router(
    path="/users",
    dependencies={},
    route_handlers=[UserController],
)
