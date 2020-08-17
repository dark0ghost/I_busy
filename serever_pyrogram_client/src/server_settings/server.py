import aiohttp_jinja2
from aiohttp import web
from pyrogram import Client


class WebServer:
    app: Client

    def __init__(self, app: Client = 1):
        self.app = app

    @aiohttp_jinja2.template('main.html')
    async def start_hendler(self, request):
        return

    async def api_doc_get(self):
        return web.Response(text="api doc get")

    async def api_doc_post(self):
        return web.Response(text="api doc post")

    async def api_start_user_client(self, request):
        print(dir(request))
        return web.Response(text="api/")

    async def api_stop_user_client(self, request):
        pass
