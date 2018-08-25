from sanic.response import json, text
from sanic import Blueprint
from dercypy.models.database import Database

bp_health = Blueprint("health")


@bp_health.route("/ping")
async def bp_ping(request):
    return text("pong", 200)


@bp_health.route("/ping/db")
async def bp_db(request):
    with Database() as db:
        alive = not db.is_dead()
        return json({"alive": alive}, 200 if alive else 410)
