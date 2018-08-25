import asyncio
import asyncpg
import ujson

DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "gustavo",
    "password": "test",
    "port": "5432",
    "database": "test",
}


async def main():
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    conn = await asyncpg.connect(**DB_CONFIG)
    # Execute a statement to create a new table.

    await conn.execute(
        """
        CREATE schema IF NOT EXISTS dercypy
        """
    )
    await conn.execute(
        """
        CREATE TABLE IF NOT EXISTS dercypy.QUOTES(
            ID INT PRIMARY KEY     NOT NULL,
            QUOTE          TEXT    NOT NULL
        )
    """
    )

    await conn.execute(
        """
        truncate dercypy.QUOTES
        """
    )
    # Insert a record into the created table.
    count = 0
    with open("dercypy/static/dercy.json") as data:
        for i in ujson.loads(data.read()):
            count += 1
            await conn.execute(
                """
                INSERT INTO dercypy.QUOTES(ID,QUOTE) VALUES($1,$2)
            """,
                count,
                i["text"],
            )

    # Close the connection.
    await conn.close()


asyncio.get_event_loop().run_until_complete(main())
