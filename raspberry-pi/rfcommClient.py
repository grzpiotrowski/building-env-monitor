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


bluetoothDeviceAddress = '98:D3:71:F6:5F:5D' #The MAC address from the HC–05 sensor
port = 1
clientSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
clientSocket.connect((bluetoothDeviceAddress, port))

while True:
    try:
        data = receiveMessage(clientSocket, '}').decode('utf-8')
        print(data)
    except KeyboardInterrupt:
        break

clientSocket.close()