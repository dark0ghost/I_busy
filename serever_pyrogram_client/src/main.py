import asyncio

import aiohttp_jinja2
import jinja2
import uvloop
from aiohttp import web
from tortoise import Tortoise

from src.extend.config import ClientConfig, ServerConfig, set_config, DataBaseConfig
from src.extend.exception import DataBaseConnectionRefused
from src.server_settings.server import WebServer


class App:
    server_config: ServerConfig
    client_config: ClientConfig
    database_config: DataBaseConfig
    asyncio_loop:  asyncio.AbstractEventLoop

    def __init__(self, asyncio_loop: asyncio.AbstractEventLoop):
        asyncio_loop.run_until_complete(self.read_config())
        self.asyncio_loop = asyncio_loop

    async def read_config(self) -> None:
        self.server_config, self.client_config, self.database_config = await set_config()

    async def set_server(self) -> web.Application:
        """
        set server
        """
        server = WebServer(database_config=self.database_config)
        web_app = web.Application()
        web_app.add_routes([web.get('/', server.start_hendler)])
        web_app.add_routes(
            [
                web.get("/api/command/", server.api_start_user_client),
                web.route("*", "/api/", server.api_doc),
            ]
        )
        aiohttp_jinja2.setup(web_app,
                             loader=jinja2.FileSystemLoader('server_settings/html/'))
        return web_app


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    uvloop.install()
    app = App(asyncio_loop=loop)
    try:
        web.run_app(app=app.set_server(), host=app.server_config.host, port=app.server_config.port)
    finally:
        loop.run_until_complete(Tortoise.close_connections())
