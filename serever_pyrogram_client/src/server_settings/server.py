import subprocess
import aiohttp
import aiohttp_jinja2

from aiohttp import web
from aiologger import Logger
from aiologger.loggers.json import JsonLogger
from typing import Dict
from pyrogram import Client
from src.table.User import User


class WebServer:
    app: Client
    status_call_client: bool
    process_id: subprocess.Popen

    def __init__(self, app: Client = 1):
        self.app = app
        self.logger: Logger = JsonLogger.with_default_handlers(name="log/server.log")
        self.status_call_client = False

    @staticmethod
    @aiohttp_jinja2.template('main.html')
    async def start_hendler(request: aiohttp.web.Request) -> Dict:
        """
        main derectory ("/")
        """
        return {

        }

    @staticmethod
    @aiohttp_jinja2.template('doc_api.html')
    async def api_doc(request: aiohttp.web.Request) -> web.Response:
        """
        out html file with doc service
        """
        return web.Response(text="api doc get")

    async def api_start_user_client(self, request: aiohttp.web.Request) -> web.Response:
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
