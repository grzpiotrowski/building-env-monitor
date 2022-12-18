# building-env-monitor

This is the Raspberry Pi Pico and Raspberry Pi 4B part of the Building Environmental Monitoring System IoT project. \
\
Link to the repo with the Web App part of this project: \
https://github.com/grzpiotrowski/building-env-webapp

## Documentation

[building-env-monitor docs](/docs/index.md)

## System architecture
![BEMS System architecture](/images/IoT_BEMS_ProjectGraphic_v1.png)


## Hardware
### RPi Pico: Temperature and Humidity Unit
![Pico Temperature and Humidity Unit](/images/circuits/pico-temp-humidity-unit_bb.png)

# Resources
* Fritzing - for designing circuits \
https://fritzing.org/

* How to Safely Store API keys in Python \
https://python.plainenglish.io/how-to-safely-store-your-api-keys-in-python-1dc5aadf93f9

* Paho Python - MQTT Client Library Encyclopedia \
https://www.hivemq.com/blog/mqtt-client-library-paho-python/

## Raspberry Pi Pico
* Getting started with Raspberry Pi Pico \
https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/0

* Raspberry Pi Pico Pinout \
https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf

* MicroPython - DHT11 \
https://docs.micropython.org/en/latest/index.html \
https://docs.micropython.org/en/latest/esp8266/tutorial/dht.html?highlight=dht11

* Bluetooth Programming with Python 3 \
https://blog.kevindoran.co/bluetooth-programming-with-python-3/

* Sockets \
https://docs.python.org/3/library/socket.html

## Raspberry Pi 4B
* How to Manage Bluetooth Devices on Linux Using bluetoothctl \
https://www.makeuseof.com/manage-bluetooth-linux-with-bluetoothctl/

* PyBluez BluetoothSocket \
https://pybluez.readthedocs.io/en/latest/api/bluetooth_socket.html


# Known errors
In [/raspberrypi/main.py](/raspberrypi/main.py): Error after one of the devices times out and the data builds up on the serial connection and there is more than one JSON in the sensorData.