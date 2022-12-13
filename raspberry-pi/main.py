import mqttClient
import rfcommClient
import time
import json


if __name__ == "__main__":
    topicName = "sensor-temp-humidity"
    bluetoothMAC = '98:D3:71:F6:5F:5D' # MAC address of the HC–05 transceiver
    port = 1
    clientSocket = rfcommClient.createSocket(bluetoothMAC, port)

    mqttc = mqttClient.createMqttClient()

    while True:
        try:
            sensorDataJson = rfcommClient.getData(clientSocket, '}')
            sensorData = json.loads(sensorDataJson)
            sensorData["timestamp"] = int(time.time())
            mqttClient.publishMqtt(mqttc, topicName, json.dumps(sensorData))
            time.sleep(5)
        except KeyboardInterrupt:
            break

    clientSocket.close()
