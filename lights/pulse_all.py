import time
from .PyGlow import PyGlow
import constants

class PulseLights:
    def __init__(self):
        self.b = constants.PIGLOW_B
        self.s = constants.PIGLOW_S
        self.pyglow = PyGlow(brightness=self.b, speed=self.s, pulse=True)

    def activate(self):
        self.pyglow.all(0)  #Set all LEDs to 0

        self.pyglow.all(brightness=self.b)

        self.pyglow.all(0)  #Set all LEDs to 0
