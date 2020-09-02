from dataclasses import dataclass


@dataclass(init=True, repr=True)
class ServerConfig:
    host: str
    port: int
    path_to_html: str
    support_ssl: bool
    path_to_ssl: str

