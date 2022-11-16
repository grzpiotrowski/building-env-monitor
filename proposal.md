# Building Environment Monitoring System
#### Student Name: Grzegorz Piotrowski   Student ID: 20099926

Environment monitoring system for a building, focusing on temperature and humidity measured in different rooms.
Data to be accessed by a web server though a MQTT broker, where it is visualised for the user on charts and a 3D model (using threejs) or a plan view of the building.
User can set a target temperature and receive push notifications (using Google Assitant API) when it is reached for each room.
Using Raspberry Pi 4B as the main device and two Raspberry Pi Picos with Bluetooth modules and DHT11 sensors to collect data
and transmit it to the main device.
Integrate real weather forecast to aid when to turn on the heating.
Optional:
 - Main device will have an LCD display with a simple menu to view data from remote sensors.
 - Integration with Google Home Assistant to ask for temperature/humidity in any room.

## Tools, Technologies and Equipment

### Tools:
- Visual Studio Code
- WebStorm IDE

### Technologies
- Python
- MicroPython
- JavaScript
- ExpressJS framework
- Handlebars templating engine
- threejs
- MQTT Broker
- OpenWeather Map API
- Google Assistant API

### Equipment:
- Raspberry Pi 4B x1
- Raspberry Pi Pico H x2
- HC-05 6 Pin Wireless Bluetooth RF Transceiver x2
- DHT11 Temperature & humidity sensor x2
- Sense HAT x1

#### Optional equipment:
- LCD1602A display x1
- Push button x3

## Project Repository
https://github.com/grzpiotrowski/building-env-monitor


