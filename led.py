import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setwarnings(False)  # Ignore warning for now

button1 = 18
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)  # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:  # Run forever
    GPIO.output(15, GPIO.HIGH)  # Turn on
    print("Led On")
    sleep(1)  # Sleep for 1 second
    GPIO.output(15, GPIO.LOW)  # Turn off
    if GPIO.input(button1) == 1:
        print("Button pressed")
        break
    print("Led Off")
    sleep(1)  # Sleep for 1 second