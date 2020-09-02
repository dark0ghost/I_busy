import asyncio
import os
import aiohttp
import aiohttp_jinja2

from typing import Dict
from aiohttp import web
from aiologger import Logger
from aiologger.loggers.json import JsonLogger
from tortoise import Tortoise
from asyncio.subprocess import Process
from src.extend.config import DataBaseConfig, ClientConfig
from src.extend.exception import DataBaseConnectionRefused
from src.table.User import User


class WebServer:
    status_call_client: bool
    process_id: Process
    database_config: DataBaseConfig
    client_config: ClientConfig

    def __init__(self, database_config: DataBaseConfig, client_config: ClientConfig) -> None:
        self.database_config = database_config
        self.client_config = client_config
        self.logger: Logger = JsonLogger.with_default_handlers(name="log/server.log")
        self.status_call_client = False

    async def create_connect_db(self) -> None:
        db_url = f"postgres://{self.database_config.postgres_user}:{self.database_config.postgres_password}@{self.database_config.host}:{self.database_config.port} "
        try:
            await Tortoise.init(
                db_url=db_url,
                modules={
                    'models': [
                        'src.table.User'
                    ]
                }
            )
        except ConnectionRefusedError as e:
            raise DataBaseConnectionRefused(f"field connect database:{db_url}  -> {e}")

    @staticmethod
    async def generate_schemas() -> None:
        await Tortoise.generate_schemas()

    @staticmethod
    @aiohttp_jinja2.template('doc_api.html')
    async def api_doc(request: aiohttp.web.Request) -> web.Response:
        """
        out html file with doc service
        """
        return web.Response(text="api doc get")

    async def api_start_user_client(self, request: aiohttp.web.Request) -> web.Response:
        if ((login := request.query.get("login")) is not None) and (
                (command := request.query.get("command")) is not None):
            await self.create_connect_db()
            if await User.filter(login_key=login).all():
                if command == "start" and not self.status_call_client:
                    self.status_call_client = True
                    self.process_id = await asyncio.create_subprocess_shell(
                        "$(which python)" + f" {os.path.abspath(path='telegram_client_settings/client.py')}  {self.client_config.app_api_hash}  {self.client_config.app_api_id}",
                    )
                    return web.json_response(data={
                        "status": "ok",
                        "cause": "script start work"
                    })
                elif command == "stop":
                    if self.status_call_client:
                        print("kill process")
                        self.process_id.kill()
                        self.status_call_client = False
                        return web.json_response(data={
                            "status": "ok",
                            "cause": f"process stop  {self.process_id.communicate()}"
                        })
                    return web.json_response({
                        "status": "bad",
                        "cause": "process is not active"
                    })

                elif self.status_call_client:
                    return web.json_response({
                        "status": "bad",
                        "cause": "process is active"
                    })
                else:
                    return web.json_response({
                        "status": "bad",
                        "cause": "command not valid"
                    })
        await self.logger.warning(msg=f"user {request.transport.get_extra_info('peername')[0]} connect without param "
                                      "login")
        return web.json_response({
            "status": "bad",
            "cause": "parameter not specified"
        })
