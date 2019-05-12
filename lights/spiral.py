import time
from .PyGlow import PyGlow
import constants


class Spiral:
    def __init__(self):
        self.b = constants.PIGLOW_B
        self.s = constants.PIGLOW_S
        self.pyglow = PyGlow(brightness=self.b, speed=self.s, pulse=False)

        self.pyglow.all(0)  # Set all LEDs to 0

    def activate(self):
        for i in range(1, 18):
            if(i > 2):
                self.pyglow.led(i-2, int(0))

            if(i > 1):
                self.pyglow.led(i-1, int(self.b/2))

            self.pyglow.led(i, self.b)

            if(i < 18):
                self.pyglow.led(i+1, int(self.b/2))

            time.sleep(self.s/10000)

        self.pyglow.all(0)  # Set all LEDs to 0
