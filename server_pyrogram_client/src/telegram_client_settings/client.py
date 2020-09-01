import sys

from pyrogram import Client


def register(api_hash: str, api_id: str) -> Client:
    """

    """
    app = Client("project", api_id=api_id, api_hash=api_hash)

    @app.on_message()
    async def hello(client, message):
        await message.reply_text("Hello {}".format(message.from_user.first_name))

    return app


if __name__ == "__main__":
    while True:
        app_api_hash: str = sys.argv[1]
        app_api_id: str = sys.argv[2]
        print(f"{app_api_id}={app_api_hash}")
