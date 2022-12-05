import paho.mqtt.client as mqtt
import sys
from config.configFiles import APIkeys

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("Connection Result: " + str(rc))

def on_message(client, obj, msg):
    print("Topic:"+msg.topic + ",Payload:" + str(msg.payload))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed,  QOS granted: "+ str(granted_qos))

def main():
    mqttc = mqtt.Client()

    # Assign event callbacks
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_subscribe = on_subscribe

    # mqtt cloud broker details, username and password
    mqttBrokerURL = APIkeys.mqttBrokerURL
    mqttBrokerPort = APIkeys.mqttBrokerPort
    mqttUser = APIkeys.mqttUser
    mqttPassword = APIkeys.mqttPassword

    # Connect
    mqttc.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
    mqttc.username_pw_set(mqttUser, mqttPassword)
        
    mqttc.connect(mqttBrokerURL, mqttBrokerPort)

    # Start subscribe, with QoS
    mqttc.subscribe("temperature/#")
    mqttc.loop_forever()

    # Continue the network loop, exit when an error occurs
    rc = 0
    while rc == 0:
        rc = mqttc.loop()

    print("rc: " + str(rc))

if __name__ == "__main__":
    main()