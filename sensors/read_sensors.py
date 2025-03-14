import time
import Adafruit_DHT
import RPi.GPIO as GPIO

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
SOIL_SENSOR_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(SOIL_SENSOR_PIN, GPIO.IN)

def read_sensors():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    soil_moisture = GPIO.input(SOIL_SENSOR_PIN)
    return {"temperature": temperature, "humidity": humidity, "soil_moisture": soil_moisture}

if __name__ == "__main__":
    while True:
        data = read_sensors()
        print(f"Temp: {data['temperature']}°C, Humidity: {data['humidity']}%, Soil: {data['soil_moisture']}")
        time.sleep(5)
