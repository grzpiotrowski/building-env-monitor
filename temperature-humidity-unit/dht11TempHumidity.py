import dht
from machine import Pin, UART
from time import sleep
import ujson

# device id
deviceId = "pico01"

# Interval between measurements in seconds
dataInterval = 5

LED = Pin(25, Pin.OUT)
ledBlinkTime = 1

# setup the UART
id = 0
rx = Pin(1)
tx = Pin(0)
baudrate=9600
# create the UART
uart = UART(0, baudrate=baudrate,tx=tx, rx=rx)

# create dht sensor instance
dhtSensor = dht.DHT11(Pin(22))

LED.value(1)
sleep(5) # Sleep to let DHT11 initialise after powering up

while True:
    try:
        dhtSensor.measure()
        temperature = dhtSensor.temperature()
        humidity = dhtSensor.humidity()
        sensorData = {
            "deviceId": deviceId,
            "temperature": temperature,
            "humidity": humidity
        }
        jsonData = ujson.dumps(sensorData)
        #print(jsonData)
        uart.write(jsonData)
        LED.value(1)
        sleep(ledBlinkTime)
        LED.value(0)
        sleep(dataInterval - ledBlinkTime)
    except KeyboardInterrupt:
        LED.value(0)
        break

