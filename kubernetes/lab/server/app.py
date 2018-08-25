#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# app.py
# @Author : Gustavo F (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto
# @Date   : 2018-6-29 15:19:46
from sanic import Sanic, response
from sanic.config import Config
from sanic.log import LOGGING_CONFIG_DEFAULTS


Config.REQUEST_TIMEOUT = 20

app = Sanic(__name__)


def jsonify(records):
    """
    Parse asyncpg record response into JSON format
    """
    # print(records)
    list_return = []

    for r in records:
        itens = r.items()
        list_return.append({i[0]: i[1].rstrip() if type(
            i[1]) == str else i[1] for i in itens})
    return list_return


@app.route('/', strict_slashes=True)
async def hello(request):
    return response.json({'posts': True})

LOGGING_CONFIG_DEFAULTS['loggers']['sanic.access']['level'] = 'ERROR'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, workers=1,
            debug=False, access_log=False)
