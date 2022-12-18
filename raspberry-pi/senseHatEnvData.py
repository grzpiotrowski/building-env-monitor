from sense_hat import SenseHat
from gpiozero import CPUTemperature
from time import sleep, time
import json

# device id
deviceId = "senseHat01"

sense = SenseHat()
sense.clear()


def getCalibratedTemperature():
    # Calibration factor to account for RPi CPU temperature affecting SenseHat
    calibrationFactor = 1.10
    senseHatTemp = sense.get_temperature()
    cpuTemp = CPUTemperature().temperature
    tempCalibrated = senseHatTemp - ((cpuTemp - senseHatTemp)/calibrationFactor)
    return int(tempCalibrated)


def getHumidity():
    humidity = sense.get_humidity()
    return int(humidity)


def getEnvironmentalData():
    humidity = getHumidity()
    temperature = getCalibratedTemperature()
    envData = {
        "deviceId": deviceId,
        "temperature": temperature,
        "humidity": humidity
    }
    envData["timestamp"] = int(time())
    return envData


if __name__ == "__main__":
    while True:
        try:
            print(getEnvironmentalData())
            sleep(1)
        except KeyboardInterrupt:
            break

  