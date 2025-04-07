import spidev
import RPi.GPIO as GPIO
import time

# Constants
VREF = 3.3  # Voltage reference (usually 3.3V on Raspberry Pi)
LED_PIN = 18

# Setup SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

# Setup PWM pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
pwm = GPIO.PWM(LED_PIN, 1000)
pwm.start(0)

def read_channel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    result = ((adc[1] & 3) << 8) + adc[2]
    return result

try:
    while True:
        adc_value = read_channel(0)
        voltage = (adc_value / 1023.0) * VREF
        pwm.ChangeDutyCycle((adc_value / 1023.0) * 100)
        
        print(f"ADC Value: {adc_value}, Voltage: {voltage:.2f} V")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    pwm.stop()
    GPIO.cleanup()
    spi.close()

