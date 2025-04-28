from litestar import Litestar

from infrastructure.db.database import db_connection
from presentation.routers.user import user


# on the app
app = Litestar(
    route_handlers=[user],
    dependencies={},
    lifespan=[db_connection]
)
