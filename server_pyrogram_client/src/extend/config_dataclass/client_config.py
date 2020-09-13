from dataclasses import dataclass


@dataclass(init=True, repr=True)
class ClientConfig:
    app_api_id: str
    app_api_hash: str
    name: str
    test_configuration: str
    product_configuration: str
    trigger_username: str
    message_on_trigger: str
