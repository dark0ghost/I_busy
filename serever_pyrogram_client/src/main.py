import asyncio

import uvloop
from aiohttp import web
from pyrogram import Client

import serever_pyrogram_client.src.extend.config as config
import serever_pyrogram_client.src.telegram_client_settings.client as client
from serever_pyrogram_client.src.server_settings.server import WebServer


async def main():
    server_config, client_config = await config.set_config()
    app_client: Client = client.register(config=client_config.token)
    server = WebServer(app=app_client)
    app = web.Application()
    app.add_routes([web.get('/', server.start_hendler)])


if __name__ == '__main__':
    uvloop.install()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
