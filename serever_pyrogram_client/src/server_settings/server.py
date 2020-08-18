from typing import Dict

import aiohttp
import aiohttp_jinja2

from aiohttp import web
from aiologger import Logger
from aiologger.loggers.json import JsonLogger
from pyrogram import Client



class WebServer:
    app: Client

    def __init__(self, app: Client = 1):
        self.app = app
        self.logger: Logger = JsonLogger.with_default_handlers(name="log/server.log")

    @staticmethod
    @aiohttp_jinja2.template('main.html')
    async def start_hendler(request) -> Dict:
        """
        main derectory ("/")
        """
        return {

        }

    @staticmethod
    @aiohttp_jinja2.template('doc_api.html')
    async def api_doc(request) -> web.Response:
        return web.Response(text="api doc get")

    async def api_start_user_client(self, request: aiohttp.web.Request) -> web.Response:
        print(await request.text())
        if login := request.query.get("login") is not None:

            return web.json_response(data={
                "status": "ok"
            })
        await self.logger.warning(msg=f"user {request.transport.get_extra_info('peername')[0]} connect without param "
                                      "login")
        return web.json_response({
            "status": "bad",
            "cause": "parameter not specified"
        })

    async def api_stop_user_client(self, request):
        pass
