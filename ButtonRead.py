import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Press Ctrl+C to exit.")

try:
    while True:
        button_state = GPIO.input(4)
        if button_state == GPIO.LOW:
            print("Button Pressed")
        else:
            print("Button Not Pressed")
        time.sleep(0.2)

except KeyboardInterrupt:
    print("\nExiting :)")

finally:
    GPIO.cleanup()

