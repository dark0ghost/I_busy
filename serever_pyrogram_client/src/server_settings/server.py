from aiohttp import web
from pyrogram import Client


class WebServer:
    app: Client

    def __init__(self, app: Client):
        self.app = app

    async def start_hendler(self, request):
        return web.Response(text="Hello, world")
