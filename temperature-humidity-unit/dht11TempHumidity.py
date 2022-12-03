import dht
import machine
dhtSensor = dht.DHT11(machine.Pin(22))

dhtSensor.measure()

temperature = dhtSensor.temperature()
humidity = dhtSensor.humidity()

print("temperature: " + str(temperature))
print("humidity: " + str(humidity))