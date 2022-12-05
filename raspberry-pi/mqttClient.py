import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import sys
import time
import json
import random
from config.configFiles import APIkeys

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("Connection Result: " + str(rc))

def on_publish(client, obj, mid):
    print("Message ID: " + str(mid))

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

mqttBrokerURL = APIkeys.mqttBrokerURL
mqttBrokerPort = APIkeys.mqttBrokerPort
print(mqttBrokerURL)

# enable TLS for secure connection
mqttc.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
mqttc.username_pw_set(APIkeys.mqttUser, APIkeys.mqttPassword)
# connect to MQTT Cloud on specified port
mqttc.connect(mqttBrokerURL, mqttBrokerPort)
mqttc.loop_start()

# Publish a message to temp every 15 seconds
while True:
    temp=round(random.uniform(15, 21), 1)
    temp_json=json.dumps({'temperature':temp, 'timestamp':time.time()})
    print(str(temp_json))
    print(mqttc.publish('temperature', temp_json))
    time.sleep(5)