import RPi.GPIO as GPIO
import time
from sensors.read_sensors import read_sensors

PUMP_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP_PIN, GPIO.OUT)

def control_pump():
    data = read_sensors()
    if data["soil_moisture"] == 0:
        print("Tanah kering, menyalakan pompa...")
        GPIO.output(PUMP_PIN, GPIO.HIGH)
        time.sleep(10)
        GPIO.output(PUMP_PIN, GPIO.LOW)
        print("Pompa dimatikan.")
    else:
        print("Tanah cukup lembab.")

if __name__ == "__main__":
    try:
        while True:
            control_pump()
            time.sleep(30)
    except KeyboardInterrupt:
        GPIO.cleanup()
