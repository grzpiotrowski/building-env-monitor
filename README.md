# building-env-monitor

This is the Raspberry Pi Pico and Raspberry Pi 4B part of the Building Environmental Monitoring System IoT project. \
The project has been scoped out in the [proposal document](/proposal.md). \
\
Link to the repo with the Web App part of this project: \
https://github.com/grzpiotrowski/building-env-webapp

## Video presentation
https://youtu.be/r7cTduhuFsI

## Documentation

[building-env-monitor docs](/docs/index.md)

## System architecture
![BEMS System architecture](/docs/images/IoT_BEMS_ProjectGraphic_v3.jpg)


## Hardware
### RPi Pico: Temperature and Humidity Unit
![Pico Temperature and Humidity Unit](/docs/images/pico-temp-humidity-unit.jpg)

Here are some photos of built prototypes:
![Pico Temperature and Humidity Unit Photo](/docs/images/temp-humidity-unit-photo.jpg)
![Pico Temperature and Humidity Unit Battery Powered Photo](/docs/images/temp-humidity-unit-battery-powered-photo.jpg)

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

### SenseHat
* SenseHat temperature correction \
https://github.com/initialstate/wunderground-sensehat/wiki/Part-3.-Sense-HAT-Temperature-Correction


## Known errors
In [/raspberrypi/main.py](/raspberrypi/main.py): Error after one of the devices times out and the data builds up on the serial connection and there is more than one JSON in the sensorData.