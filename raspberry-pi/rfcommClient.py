# Based on:
# https://github.com/pybluez/pybluez/blob/master/examples/simple/rfcomm-client.py

import bluetooth
from time import sleep


def receiveMessage(clientSocket, endCharacter):
    """Receives data stream from the socket and merges data into a message
    based on the endCharacter"""
    data = b''
    while True:
        try:
            data += clientSocket.recv(1024)
            #sleep(0.5) # Use sleep to wait for more packets
            if data.decode('utf-8').endswith(endCharacter):
                break
        except bluetooth.btcommon.BluetoothError:
            print("Connection timed out.")
            return False

    return data


def createSocket(bluetoothDeviceAddress, port):
    """Creates a rfcomm client. Returns False if the device is not responding.
    """
    try:
        clientSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        clientSocket.connect((bluetoothDeviceAddress, port))
        return clientSocket
    except bluetooth.btcommon.BluetoothError as bluetoothError:
        print(bluetoothError.args)
        return False


def closeSocket(clientSocket):
    closeSocket.close()


def getData(clientSocket, endCharacter):
    data = receiveMessage(clientSocket, '}')
    if data is not False:
        data = data.decode('utf-8')
    print("Received data: " + data)
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