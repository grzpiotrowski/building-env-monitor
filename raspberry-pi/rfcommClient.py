# using PyBluez library: https://github.com/pybluez/pybluez
# Based on:              https://github.com/pybluez/pybluez/blob/master/examples/simple/rfcomm-client.py

import bluetooth

bluetoothDeviceAddress = '98:D3:71:F6:5F:5D' #The MAC address from the HC–05 sensor
port = 1
socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
socket.connect((bluetoothDeviceAddress, port))
data = ''
while True:
    try:
        data = socket.recv(1024)
        print(str(data))
    except KeyboardInterrupt:
        break

socket.close()
    