import mqttClient
import rfcommClient
import time


if __name__ == "__main__":
    bluetoothMAC = '98:D3:71:F6:5F:5D' # MAC address of the HC–05 transceiver
    port = 1
    clientSocket = rfcommClient.createSocket(bluetoothMAC, port)

    mqttc = mqttClient.createMqttClient()

    while True:
        try:
            sensorData = rfcommClient.getData(clientSocket, '}')
            mqttClient.publishMqtt(mqttc, 'temperature', sensorData)
            time.sleep(5)
        except KeyboardInterrupt:
            break

    clientSocket.close()
