import asyncio
from dataclasses import dataclass
from typing import Any, Dict

import ujson as json
import os.path
import aiofiles


@dataclass(init=True, repr=True)
class ServerConfig:
    host: str
    port: int


@dataclass(init=True, repr=True)
class ClientConfig:
    token: str


async def read_client():
    async with aiofiles.open(os.path.abspath(path="config/client.json").replace("lib/", "")) as file:
        print(1)
        return await file.read()


async def read_server():
    async with aiofiles.open(os.path.abspath(path="config/server.json").replace("lib/", "")) as file:
        print(2)
        return await file.read()


async def set_config() -> (ServerConfig, ClientConfig):
    """
    build config server and client and  package in data class
    Returns: (ServerConfig,ClientConfig)
    """
    server_config: Dict[str, Any] = json.loads(await read_server())
    client_config: Dict[str, Any] = json.loads(await read_client())
    port: int = server_config.get("port")
    host: str = server_config.get("host")
    token: str = client_config.get("token")
    return ServerConfig(host=host, port=port), ClientConfig(token=token)
