import dht
from machine import Pin, UART
from time import sleep


# device id
deviceId = "pico01"

# setup the UART
id = 0
rx = Pin(1)
tx = Pin(0)
baudrate=9600
# create the UART
uart = UART(0, baudrate=baudrate,tx=tx, rx=rx)

# create dht sensor instance
dhtSensor = dht.DHT11(Pin(22))

i = 0
while True:
    dhtSensor.measure()
    temperature = dhtSensor.temperature()
    humidity = dhtSensor.humidity()
    i += 1
    sensorMessage = '{ deviceid: "%s", temp: %.0f, humidity: %.0f }' % (
        deviceId, temperature, humidity)
    print(sensorMessage)
    uart.write(sensorMessage)
    sleep(5)










