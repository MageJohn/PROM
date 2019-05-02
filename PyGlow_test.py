
#####
#
# PyGlow
#
#####
#
# Python module to control Pimoronis PiGlow
# [http://shop.pimoroni.com/products/piglow]
#
# * pulsetest.py - test the pulsing light feature
#
#####

import time
from PyGlow import PyGlow


b = input("Maximum brightness: ")
s = int(input("Speed in milliseconds (try 1000 as a default): "))

pyglow = PyGlow(brightness=int(b), speed=s, pulse=True)

pyglow.all(0)

for colour in ['white', 'blue', 'green', 'yellow', 'orange', 'red']:
    pyglow.color(colour, 255)
    time.sleep(s / 1000)
    pyglow.color(colour, 0)
