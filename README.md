# project_x
# what does this project do?
this project allows you to assemble a system from a server and a client so that you can go away on business and enable the **"user is ofline"** (the system will answer everyone who wrote your **@username** anywhere)
# server(telegram-client)
the server is built on the __asynchronous frameworks__ [aiohttp](https://github.com/aio-libs/aiohttp) and [pyrogram](https://github.com/pyrogram/pyrogram). the api server accepts requests and executes the transmitted instructions (stop the client or start)
__the server has built-in authentication by passing the get requset parameter to the login, the server sends a request to the database (postgresql) and if this login is valid then it goes to execute the instructions__
# iot client
__this repository presents one of the implementations of a smart device using the example of arduino uno and esp8266. In this case, arduino reads the value of the button and sends the command to the esp if the condition is met, the esp collects the link and makes a request to the specified host__

## expanding examples of smart device
**if you want to add your example of a smart device, then you need to add documentation in addition to the software, which says what devices are needed and a description of how the installation works**

