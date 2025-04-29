from click import Group
from litestar import Litestar
from litestar.exceptions import HTTPException
from litestar.plugins import CLIPluginProtocol

from presentation.exceptions import app_exception_handler
from presentation.routers.users import users_router


class CLIPlugin(CLIPluginProtocol):
    def on_cli_init(self, cli: Group) -> None:
        @cli.command()
        def is_debug_mode(app: Litestar):
            print(app.debug)


app = Litestar(
    route_handlers=[users_router],
    exception_handlers={HTTPException: app_exception_handler},
    dependencies={},
    plugins=[CLIPlugin()],
)
