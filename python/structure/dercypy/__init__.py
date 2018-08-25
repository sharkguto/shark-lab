from sanic import Sanic
from dercypy.controllers.quotes import bp_dercy
from dercypy.controllers.health import bp_health
from asyncpg import create_pool

# db connection config

DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "gustavo",
    "password": "test",
    "port": "5432",
    "database": "test",
    "max_size": 20,
    "max_inactive_connection_lifetime": 60.0,
}

# instance sanic app

app = Sanic(__name__)

# load blueprints

app.register_blueprint(bp_dercy)
app.register_blueprint(bp_health)

# load middlewares


@app.listener("before_server_start")
async def register_db(app, loop) -> None:
    """
        Create a database connection pool
        :param app: sanic instance
        :param loop: current event loop
    """
    app.config["pool"] = await create_pool(**DB_CONFIG, loop=loop)
