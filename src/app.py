import uvicorn
from litestar import Controller, Router, Litestar, get, post, put, delete
from litestar.di import Provide


async def bool_fn() -> bool: ...


async def dict_fn() -> dict: ...


async def list_fn() -> list: ...


async def int_fn() -> int: ...


class MyController(Controller):
    path = "/user"
    dependencies = {"controller_dependency": Provide(list_fn)}

    # on the route handler
    @post(path="/", dependencies={"local_dependency": Provide(int_fn)})
    async def my_route_handler(
        self,
        app_dependency: bool,
        router_dependency: dict,
        controller_dependency: list,
        local_dependency: int,
    ) -> None: ...


# on the router
user = Router(
    path="/api",
    dependencies={"router_dependency": Provide(dict_fn)},
    route_handlers=[MyController],
)

# on the app
app = Litestar(
    route_handlers=[user], dependencies={"app_dependency": Provide(bool_fn)}
)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)