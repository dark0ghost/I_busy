from pyrogram import Client, Filters

from srever_pyrogram_client.src.lib.config import ClientConfig


def register(config: ClientConfig) -> Client:
    app = Client(config.token)

    @app.on_message()
    def hello(client, message):
        message.reply_text("Hello {}".format(message.from_user.first_name))

    return app
