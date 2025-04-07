import spidev
import time
import RPi.GPIO as GPIO

# GPIO setup
LED_PIN = 18  # Use PWM-capable pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
pwm = GPIO.PWM(LED_PIN, 1000)  # PWM at 1kHz
pwm.start(0)

# SPI setup
spi = spidev.SpiDev()
spi.open(0, 0)  # Open bus 0, device 0 (CE0)
spi.max_speed_hz = 1350000

# Read MCP3008 channel (0-7)
def read_adc(channel):
    if channel < 0 or channel > 7:
        return -1
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

try:
    while True:
        value = read_adc(0)  # Read from channel 0
        duty_cycle = (value / 1023.0) * 100  # Scale to 0-100%
        pwm.ChangeDutyCycle(duty_cycle)
        print(f"Potentiometer value: {value}, Duty Cycle: {duty_cycle:.1f}%")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
    pwm.stop()
    GPIO.cleanup()
    spi.close()

