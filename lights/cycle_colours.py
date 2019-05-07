import time
from PyGlow import PyGlow
from .. import constants

b = constants.PIGLOW_B
s = constants.PIGLOW_S
pyglow = PyGlow(brightness = b, speed = s, pulse=False)

pyglow.all(0) #Set all LEDs to 0

for colour in ['white', 'blue', 'green', 'yellow', 'orange', 'red']:
    pyglow.color(colour, b)
    time.sleep(s / 2000)
    pyglow.color(colour, 0)


pyglow.all(0) #Set all LEDs to 0
