import asyncio
from dataclasses import dataclass
from typing import Any, Dict, Optional

import ujson as json
import os.path
import aiofiles


@dataclass(init=True, repr=True)
class ServerConfig:
    host: str
    port: int
    path_to_html: str
    support_ssl: bool
    path_to_ssl: str


@dataclass(init=True, repr=True)
class ClientConfig:
    app_api_id: str
    app_api_hash: str
    name: str
    test_configuration: str
    product_configuration: str


@dataclass(init=True, repr=True)
class DataBaseConfig:
    host: str
    port: int
    postgres_user: str
    postgres_password: str


async def read_client_config() -> str:
    """
    read client config
    Returns: str
    """
    async with aiofiles.open(os.path.abspath(path="config/client.json").replace("lib/", "")) as file:
        return await file.read()


async def read_server_config() -> str:
    """
    read server config
    """
    async with aiofiles.open(os.path.abspath(path="config/server.json").replace("lib/", "")) as file:
        return await file.read()


async def read_database_config() -> str:
    """
    read database config
    """
    async with aiofiles.open(os.path.abspath(path="config/database.json").replace("lib/", "")) as file:
        return await file.read()


async def set_config() -> (ServerConfig, ClientConfig, DataBaseConfig):
    """
    build config server and client and  package in data class
    Returns: (ServerConfig,ClientConfig)
    """
    server_config: Dict[str, Any] = json.loads(await read_server_config())
    client_config: Dict[str, Any] = json.loads(await read_client_config())
    database_config: Dict[str, Any] = json.loads(await read_database_config())
    port: Optional[int] = server_config.get("port")
    host: Optional[str] = server_config.get("host")
    support_ssl: Optional[bool] = server_config.get("support ssl")
    path_to_html: Optional[str] = server_config.get("path to html")
    path_to_ssl: Optional[str] = server_config.get("path to ssl")
    name: Optional[str] = client_config.get("name")
    app_api_id: Optional[str] = client_config.get("App api_id")
    app_api_hash: Optional[str] = client_config.get("App api_hash")
    test_configuration: Optional[str] = client_config.get("Test configuration")
    product_configuration: Optional[str] = client_config.get("Production configuration")
    port_database: Optional[int] = database_config.get("port")
    host_database: Optional[str] = database_config.get("host")
    postgres_user: Optional[str] = database_config.get("POSTGRES_USER")
    postgres_password: Optional[str] = database_config.get("POSTGRES_PASSWORD")
    return ServerConfig(host=host, port=port, path_to_html=path_to_html, support_ssl=support_ssl,
                        path_to_ssl=path_to_ssl), \
           ClientConfig(name=name, app_api_id=app_api_id,
                        app_api_hash=app_api_hash,
                        test_configuration=test_configuration,
                        product_configuration=product_configuration), \
           DataBaseConfig(port=port_database, host=host_database, postgres_user=postgres_user,
                          postgres_password=postgres_password)
