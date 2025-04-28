from litestar import Controller, Router, get, post, put, delete


class MyController(Controller):
    path = "/users"
    dependencies = {}

    @post(path="/")
    async def create_user(self) -> None:
        ...

    @get(path="/{user_id: int}")
    async def read_user(self, user_id: int) -> None:
        ...

    @get(path="/list")
    async def read_users(self) -> None:
        ...

    @put(path="/{user_id: int}")
    async def update_user(self) -> None:
        ...

    @delete(path="/{user_id: int}")
    async def delete_user(self) -> None:
        ...


user = Router(
    path="/api",
    dependencies={},
    route_handlers=[MyController],
)
