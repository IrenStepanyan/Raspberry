import RPi.GPIO as GPIO
import time

LED_PIN = 18
POT_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(POT_PIN, GPIO.OUT)

led_pwm= GPIO.PWM(LED_PIN, 10000)
led_pwm.start(0)

def read(pot):
    count = 0

    GPIO.setup(pot, GPIO.OUT)
    GPIO.output(pot, False)
    time.sleep(0.01)

    GPIO.setup(pot, GPIO.IN)

    while GPIO.input(pot) == GPIO.LOW:
        count +=1

    return count

try:
    while True:
        a = read(POT_PIN)

        bright = max(0, min(100, int(a/100)))

        led_pwm.ChangeDutyCycle(bright)

        print(f"{bright}\n")

        time.sleep(0.1)
except:
    print("Exit")

finally:
    led_pwm.stop()
    GPIO.cleanup()
