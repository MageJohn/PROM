import RPi.GPIO as GPIO 	#IO library
import time 			    #Time library
import re
import sys

BEEP = r":beep frequency=(\d*) length=(\d*)ms;"
DELAY = r":delay (\d*)ms;"


class MikrotikPlayer:
    def __init__(self, filename):
        GPIO.setwarnings(False)  #disable runtime warnings
        GPIO.setmode(GPIO.BCM)  #use Broadcom GPIO names

        GPIO.setup(9, GPIO.OUT)  #set pin 10 as output

        self.filename = filename
        self.pwm = GPIO.PWM(9, 1000)  #set freq 100Hz

    def play(self):
        with open(self.filename) as sndfile:
            for line in sndfile:
                beep = re.match(BEEP, line)
                delay = re.match(DELAY, line)
                if beep:
                    self.pwm.ChangeFrequency(int(beep.group(1)))
                    self.pwm.start(50)
                    time.sleep(int(beep.group(2))/1000)
                elif delay:
                    self.pwm.stop()
                    time.sleep(int(delay.group(1))/1000)

if __name__ == "__main__":
    player = MikrotikPlayer(sys.argv[1])
    player.play()
