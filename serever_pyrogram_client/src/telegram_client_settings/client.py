from pyrogram import Client, Filters

from src.extend.config import ClientConfig


def register(config: ClientConfig) -> Client:
    app = Client(config.name, api_id=config.app_api_id, api_hash=config.app_api_hash)

    @app.on_message()
    def hello(client, message):
        message.reply_text("Hello {}".format(message.from_user.first_name))

    return app
