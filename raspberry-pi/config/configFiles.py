import os
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass

load_dotenv(find_dotenv())
@dataclass(frozen=True)
class APIkeys:
    mqttBrokerURL: str = os.getenv('mqttBrokerURL')
    mqttBrokerPort: int = int(os.getenv('mqttBrokerPort'))
    mqttUser: str = os.getenv('mqttUser')
    mqttPassword: str = os.getenv('mqttPassword')
    mqttClientId: str = os.getenv('mqttClientId')