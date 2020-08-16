import aiohttp
import uvloop
import asyncio
import srever_pyrogram_client.src.lib.config as config


async def main():
    server_config, client_config = await config.set_config()


if __name__ == '__main__':
    uvloop.install()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
