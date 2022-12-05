# Temperature and Humidity Unit
## Assembly
![Pico Temperature and Humidity Unit](/docs/images/pico-temp-humidity-unit.jpg)

### Components:
    * Raspberry Pi Pico
    * DHT11
    * HC-05 Bluetooth Module
    * 10k Ohm Resistor
    * 8x Jumper Wire


## Setup
The next step after assembling the circuit is to put the code ([dht11TempHumidity.py](/temperature-humidity-unit/dht11TempHumidity.py)) onto Raspberry Pi Pico.
1. Press the BOOTSEL button and hold it while you connect the other end of the micro USB cable to your Raspberry Pi 4.
2. Run Thonny IDE.
3. The current version of Python used is displayed in the bottom right corner of Thonny window.
4. Click on the Python version and choose "MicroPython (Raspberry Pi Pico)".
5. Click the Install button in the popup dialog to copy the MicroPython firmware to Raspberry Pi Pico.
6. Open dht11TempHumidity.py file in Thonny.
7. Save this file as main.py and select Raspberry Pi Pico as the target device.

Pico will now automatically run the code in main.py file when powered.

After disconnecting the Pico from power and reconnecting it again you should notice the onboard LED being on for a few seconds and then blinking at regular intervals. \
![Pico blinking LED](/docs/images/pico-temp-humidity-blinking-led.gif) \
This means the Python program is running and temperature and humidity data is being sent to the HC-05 transceiver.

# Raspberry Pi


## Dependencies
```bat
sudo apt-get install bluetooth
sudo apt-get install libbluetooth-dev
pip install PyBluez
pip install paho-mqtt
```

## Pairing with HC05 Bluetooth module
Run bluetoothctl:
```bat
sudo bluetoothctl
```
Scan for other devices:
```bat
bluetoothctl scan on
```
Note the MAC address of the Bluetooth module and pair and connect devices:
```bat
bluetoothctl pair MAC_ADDRESS
bluetoothctl connect MAC_ADDRESS
```
Paired Bluetooth devices can be check with:
```bat
bluetoothctl paired-devices
```

# HiveMQ
This section will explain how to create free HiveMQ cluster. \
https://www.hivemq.com/

# InfluxDB
This section will explain how to create and setup free InfluxDB database. \
https://cloud2.influxdata.com/signup