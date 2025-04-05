import RPi.GPIO as GPIO
import time

BUTTON_PIN = 17
LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

led_state = False
last_button_state = GPIO.input(BUTTON_PIN)

print("Ctrl+ C to stop")

try:
    while True:
        button_state = GPIO.input(BUTTON_PIN)

        if last_button_state == GPIO.HIGH and button_state == GPIO.LOW:
            led_state = not led_state
            GPIO.output(LED_PIN, led_state)
            print("LED ON" if led_state else "LED OFF")
            time.sleep(0.2)

        last_button_state = button_state
        time.sleep(0.05)

except:
    print("\nExiting")

finally:
    GPIO.cleanup()
