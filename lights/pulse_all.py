import time
from PyGlow import PyGlow
import constants

b = constants.PIGLOW_B
s = constants.PIGLOW_S
pyglow = PyGlow(brightness = b, speed = s, pulse=True)

pyglow.all(0) #Set all LEDs to 0

pyglow.all(brightness=b)
time.sleep(s/1000)

pyglow.all(0) #Set all LEDs to 0
