from sanic.response import json
from sanic import Blueprint
from dercypy.models.database import Database

bp_dercy = Blueprint("quotes")


@bp_dercy.route("/companies")
async def bp_companies(request):
    with Database() as db:
        result = await db.execute_query("company")
        return json({"results": result})


@bp_dercy.route("/quotes/dercy")
async def bp_companies(request):
    with Database(database="dercypy") as db:
        result = await db.execute_query("all_quotes")
        return json({"results": result})


@bp_dercy.route("/")
async def bp_root(request):
    return json({"my": "blueprint"})


@bp_dercy.route("/sync")
def bp_root2(request):
    return json({"my": "blueprintsync"})
