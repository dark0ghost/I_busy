from aiohttp import web


async def hello(request):
    return web.Response(text="Hello, world")


