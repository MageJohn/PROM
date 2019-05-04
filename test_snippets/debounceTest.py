import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

PIN = 10

GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #uses pin 17
count = 0
while True:
    GPIO.wait_for_edge(PIN, GPIO.FALLING)
    count += 1
    print("Button pressed {} times".format(count))
    time.sleep(0.2)
