import asyncio

import uvloop
from aiohttp import web
from pyrogram import Client

import serever_pyrogram_client.src.extend.config as config
import serever_pyrogram_client.src.telegram_client_settings.client as client
from serever_pyrogram_client.src.server_settings.server import WebServer


class App:
    server_config: config.ServerConfig
    client_config: config.ClientConfig

    def __init__(self, loop: asyncio.AbstractEventLoop):
        loop.run_until_complete(self.read_config())

    async def read_config(self):
        self.server_config, self.client_config = await config.set_config()

    async def main(self) -> web.Application:
        # app_client: Client = client.register(config=client_config.token)
        # server = WebServer(app=app_client)
        server = WebServer()
        app = web.Application()
        app.add_routes([web.get('/', server.start_hendler)])
        app.add_routes(
            [
                web.get("/api/start", server.api_start_user_client),
                web.get("/api/stop", server.api_stop_user_client)
            ]
        )
        # , host=server_config.host, port=server_config.port)
        return app


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    uvloop.install()
    app = App(loop=loop)
    web.run_app(app.main(),host=app.server_config.host,port=app.server_config.port)
