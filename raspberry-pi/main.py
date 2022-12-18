import mqttClient
import rfcommClient
import time
import json
import senseHatEnvData


if __name__ == "__main__":
    topicName = "sensor-temp-humidity"

    # Bluetooth details of temperature-humidity devices
    bluetoothDetails = {
        'pico01': {
            'macAddress': '98:D3:71:F6:5F:5D',
            'port': 1
        },
        'pico02': {
            'macAddress': '98:D3:31:F6:43:D1',
            'port': 1
        }
    }

    # Creating serial client connections
    clientSockets = {}
    for device in bluetoothDetails:
        print('Creating a client socket for: ' + device)
        clientSockets[device] = (rfcommClient.createSocket(
            bluetoothDetails[device]['macAddress'],
            bluetoothDetails[device]['port']
        ))

    # Creating MQTT Client
    mqttc = mqttClient.createMqttClient()

    # Reading data from temperature-humidity devices and publishing to MQTT
    while True:
        try:
            for device in clientSockets:
                if clientSockets[device] is not False:
                    clientSocket = clientSockets[device]
                    sensorDataJson = rfcommClient.getData(clientSocket, '}')
                    if sensorDataJson is not False:
                        try:
                            sensorData = json.loads(sensorDataJson)
                            sensorData["timestamp"] = int(time.time())
                            mqttClient.publishMqtt(mqttc, topicName, json.dumps(sensorData))
                        except json.decoder.JSONDecodeError:
                            # Error after one of the devices times out and the data builds up
                            # on the serial connection and there is more than one JSON in the sensorData
                            # TO BE FIXED.
                            continue
            sensorData = senseHatEnvData.getEnvironmentalData()
            mqttClient.publishMqtt(mqttc, topicName, json.dumps(sensorData))
            time.sleep(5)
        except KeyboardInterrupt:
            break


    clientSocket.close()
