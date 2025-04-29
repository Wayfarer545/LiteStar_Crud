from click import Group
from litestar import Litestar
from litestar.plugins import CLIPluginProtocol
from litestar_granian import GranianPlugin

from src.presentation.routers.users import users_router


class CLIPlugin(CLIPluginProtocol):
    def on_cli_init(self, cli: Group) -> None:
        @cli.command()
        def is_debug_mode(app: Litestar):
            print(app.debug)

app = Litestar(
    route_handlers=[users_router],
    dependencies={},
    plugins=[CLIPlugin(), GranianPlugin()],
)
