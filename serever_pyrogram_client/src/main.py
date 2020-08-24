import asyncio
import aiohttp_jinja2
import jinja2
import uvloop

from aiohttp import web
from tortoise import Tortoise
from src.extend.config import ClientConfig, ServerConfig, set_config, DataBaseConfig
from src.extend.exception import DataBaseConnectionRefused
from src.telegram_client_settings.client import register
from src.server_settings.server import WebServer


class App:
    server_config: ServerConfig
    client_config: ClientConfig
    database_config: DataBaseConfig

    def __init__(self, asyncio_loop: asyncio.AbstractEventLoop):
        asyncio_loop.run_until_complete(self.read_config())

    async def read_config(self) -> None:
        self.server_config, self.client_config, self.database_config = await set_config()

    async def main(self) -> web.Application:
        # app_client: Client = client.register(config=client_config.token)
        # server = WebServer(app=app_client)
        db_url = f"postgres://{self.database_config.postgres_user}:{self.database_config.postgres_password}@{self.database_config.host}:{self.database_config.port}"
        print(db_url)
        try:
            await Tortoise.init(
                db_url=db_url,
                modules={'models': ['app.models']}

            )
            await Tortoise.generate_schemas()
        except ConnectionRefusedError as e:
            raise DataBaseConnectionRefused(f"field connect database:{db_url}  -> {e}")
        server = WebServer()
        web_app = web.Application()
        web_app.add_routes([web.get('/', server.start_hendler)])
        web_app.add_routes(
            [
                web.get("/api/start/", server.api_start_user_client),
                web.get("/api/stop/", server.api_stop_user_client),
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
    web.run_app(app.main(), host=app.server_config.host, port=app.server_config.port)
