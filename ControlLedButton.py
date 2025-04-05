import RPi.GPIO as GPIO
import time

BUTTON_PIN = 17
LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

print("Ctrl C for exiting")

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            GPIO.output(LED_PIN, GPIO.LOW)
        else:
            GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.2)
except KeyboardInterrupt:
    print("Exiting")
finally:
    GPIO.cleanup()
