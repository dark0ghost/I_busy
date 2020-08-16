from pyrogram import Client, Filters

from serever_pyrogram_client.src.extend.config import ClientConfig


def register(config: ClientConfig) -> Client:
    app = Client(config.token)

    @app.on_message()
    def hello(client, message):
        message.reply_text("Hello {}".format(message.from_user.first_name))

    return app
