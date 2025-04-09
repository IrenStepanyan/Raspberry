import spidev
import RPi.GPIO as GPIO
import time


VREF = 3.3  
#LED_PIN = 18

# Setup SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

# Setup PWM pin
GPIO.setmode(GPIO.BCM)
#GPIO.setup(LED_PIN, GPIO.OUT)
#pwm = GPIO.PWM(LED_PIN, 1000)
#pwm.start(0)

def read_channel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    result = ((adc[1] & 3) << 8) + adc[2]
    return result

try:
    while True:
        pwm_value = read_channel(0)
        ldr_value = read_channel(1)
        voltage = (pwm_value / 1023.0) * VREF
        voltage1 = (ldr_value / 1023.0) * VREF

        #pwm.ChangeDutyCycle((pwm_value / 1023.0) * 100)
        
        print(f"PWM: ADC Value: {pwm_value}, Voltage: {voltage:.2f} V")
        
        print(f"LRD: ADC Value: {ldr_value}, Voltage: {voltage1: .2f} V")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    #pwm.stop()
    GPIO.cleanup()
    spi.close()

