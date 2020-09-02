from dataclasses import dataclass


@dataclass(init=True, repr=True)
class DataBaseConfig:
    host: str
    port: int
    postgres_user: str
    postgres_password: str
    need_update: bool