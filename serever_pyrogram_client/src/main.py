import asyncio
import aiohttp_jinja2
import jinja2
import uvloop
from aiohttp import web
from pyrogram import Client


from src.extend.config import ClientConfig, ServerConfig, set_config
from src.telegram_client_settings.client import register
from src.server_settings.server import WebServer


class App:
    server_config: ServerConfig
    client_config: ClientConfig

    def __init__(self, loop: asyncio.AbstractEventLoop):
        loop.run_until_complete(self.read_config())

    async def read_config(self):
        self.server_config, self.client_config = await set_config()

    async def main(self) -> web.Application:
        # app_client: Client = client.register(config=client_config.token)
        # server = WebServer(app=app_client)
        server = WebServer()
        web_app = web.Application()
        web_app.add_routes([web.get('/', server.start_hendler)])
        web_app.add_routes(
            [
                web.get("/api/start", server.api_start_user_client),
                web.get("/api/stop", server.api_stop_user_client),
                web.get("/api", server.api_doc_get),
                web.post("/api", server.api_doc_post)
            ]
        )
        aiohttp_jinja2.setup(web_app,
                             loader=jinja2.FileSystemLoader('server_settings/html/'))
        return web_app


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    uvloop.install()
    app = App(loop=loop)
    web.run_app(app.main(), host=app.server_config.host, port=app.server_config.port)
