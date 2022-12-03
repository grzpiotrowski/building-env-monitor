import dht
import machine
from time import sleep

dhtSensor = dht.DHT11(machine.Pin(22))
i = 0
while True:
  dhtSensor.measure()
  temperature = dhtSensor.temperature()
  humidity = dhtSensor.humidity()
  i += 1
  print("Measurement: " + str(i))
  print("temperature: " + str(temperature))
  print("humidity: " + str(humidity))
  sleep(5)