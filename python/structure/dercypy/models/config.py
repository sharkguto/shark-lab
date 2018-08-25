import configparser

SQLFILE = "dercypy/secrets/queries.ini"
DBCREDENTIALS = "dercypy/secrets/database.ini"
QUERIES = dict()


def load_queries():
    config = configparser.ConfigParser()
    config.read(SQLFILE)
    global QUERIES
    QUERIES = {i: dict(config._sections[i]) for i in config._sections}

