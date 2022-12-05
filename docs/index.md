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
After assembling the circuit, Press the BOOTSEL button and hold it while you connect the other end of the micro USB cable to your computer (Raspberry Pi)

TBD...

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