import sys
import asyncio
from pyrogram import Client
from pyrogram.client.filters import filters


def register(api_hash: str, api_id: str, trigger_name: str) -> Client:
    app = Client("project", api_id=api_id, api_hash=api_hash)

    @app.on_message(filters=filters.Filters.regex(pattern=f'^@{trigger_name}'))
    async def anser(client, message):
        await message.reply_text("wait user busy")

    return app


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    app_api_hash: str = sys.argv[1]
    app_api_id: str = sys.argv[2]
    app_trigger: str = sys.argv[3]
    app = register(api_id=app_api_id, api_hash=app_api_hash, trigger_name=app_trigger)
    loop.run_until_complete(app.run())
