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
    path_to_html: str


@dataclass(init=True, repr=True)
class ClientConfig:
    app_api_id: str
    app_api_hash: str
    name: str
    test_configuration: str
    product_configuration: str


async def read_client() -> str:
    """
    read client config
    Returns: str
    """
    async with aiofiles.open(os.path.abspath(path="config/client.json").replace("lib/", "")) as file:
        return await file.read()


async def read_server() -> str:
    """
    read server config
    """
    async with aiofiles.open(os.path.abspath(path="config/server.json").replace("lib/", "")) as file:
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
    path_to_html: str = server_config.get("path to html")
    name: str = client_config.get("name")
    app_api_id: str = client_config.get("App api_id")
    app_api_hash: str = client_config.get("App api_hash")
    test_configuration: str = client_config.get("Test configuration")
    product_configuration: str = client_config.get("Production configuration")
    return ServerConfig(host=host, port=port, path_to_html=path_to_html), ClientConfig(name=name, app_api_id=app_api_id,
                                                                                       app_api_hash=app_api_hash,
                                                                                       test_configuration=test_configuration,
                                                                                       product_configuration=product_configuration)
