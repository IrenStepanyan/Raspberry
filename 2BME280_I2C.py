import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

i2c = busio.I2C(board.SCL, board.SDA)
bme1= adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)
bme2= adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x77)

bme1.sea_level_pressure = 1013.25 
bme2.sea_level_pressure = 1013.25

try:
    while True:
        print("Sensor1")
        print(f"Temperature: {bme1.temperature:.2f} °C")
        print(f"Humidity: {bme1.humidity:.2f} %")
        print(f"Pressure: {bme1.pressure:.2f} hPa")
        print(f"Altitude (estimated): {bme1.altitude:.2f} m")
        print("\n")

        print("Sensor2")
        print(f"Temperature: {bme2.temperature:.2f} °C")
        print(f"Humidity: {bme2.humidity:.2f} %")
        print(f"Pressure: {bme2.pressure:.2f} hPa")
        print(f"Altitude (estimated): {bme2.altitude:.2f} m")
        print("\n\n")
        time.sleep(3)
except KeyboardInterrupt:
    print("Exit")

