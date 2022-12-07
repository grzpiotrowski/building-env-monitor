# Based on:
# https://github.com/pybluez/pybluez/blob/master/examples/simple/rfcomm-client.py

import bluetooth
from time import sleep


def receiveMessage(clientSocket, endCharacter):
    """Receives data stream from the socket and merges data into a message
    based on the endCharacter"""
    data = b''
    while True:
        data += clientSocket.recv(1024)
        #sleep(0.5) # Use sleep to wait for more packets
        if data.decode('utf-8').endswith(endCharacter):
            break
    return data


def createSocket(bluetoothDeviceAddress, port):
    clientSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    clientSocket.connect((bluetoothDeviceAddress, port))
    return clientSocket


def closeSocket(clientSocket):
    closeSocket.close()


def getData(clientSocket, endCharacter):
    data = receiveMessage(clientSocket, '}').decode('utf-8')
    print(data)
    return data


if __name__ == "__main__":
    bluetoothMAC = '98:D3:71:F6:5F:5D' # MAC address of the HC–05 transceiver
    port = 1
    clientSocket = createSocket(bluetoothMAC, port)

    while True:
        try:
            getData(clientSocket, '}')
        except KeyboardInterrupt:
            break

    clientSocket.close()