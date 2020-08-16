from aiohttp import web
from pyrogram import Client



class WebServer:
    app: Client

    def __init__(self, app: Client = 1):
        self.app = app

    @staticmethod
    async def start_hendler(request):
        return web.Response(text="Hello, world")

    async def api_start_user_client(self, request):

        print(request.match_info.get("login")
              )
        return web.Response(text= str(await request.post()))

    async def api_stop_user_client(self, request):
        pass
