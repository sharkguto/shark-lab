import dercypy
from dercypy.models.config import QUERIES
import asyncpg


class Database(object):
    """
    Default class for all databases connections
    """

    pool = None

    def __init__(self, database=None):
        self.pool = dercypy.app.config["pool"]
        self.database = database or "test"

    def is_dead(self):
        return self.pool._closed

    @staticmethod
    def res2json(records: list) -> list:
        list_return = []
        for r in records:
            itens = r.items()
            list_return.append(
                {
                    i[0]: i[1].rstrip() if type(i[1]) == str else i[1]
                    for i in itens
                }
            )
        return list_return

    async def execute_query(self, proc: str, **kwargs) -> list:
        query = QUERIES[proc]["query"].format(database=self.database, **kwargs)

        async with self.pool.acquire() as conn:
            results = await conn.fetch(query)

        return Database.res2json(results)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(exc_val)

