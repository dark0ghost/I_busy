# project_x
# what does this project do?
this project allows you to assemble a system from a server and a client so that you can go away on business and enable the **"user is ofline"** (the system will answer everyone who wrote your **@username** anywhere)
# server(telegram-client)
the server is built on the __asynchronous frameworks__ [aiohttp](https://github.com/aio-libs/aiohttp) and [pyrogram](https://github.com/pyrogram/pyrogram). the api server accepts requests and executes the transmitted instructions (stop the client or start)
__the server has built-in authentication by passing the get requset parameter to the login, the server sends a request to the database (postgresql) and if this login is valid then it goes to execute the instructions__
# iot client
__coming soon__




