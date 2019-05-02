
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

#Pulse colour outward
for colour in ['white', 'blue', 'green', 'yellow', 'orange', 'red']:
    pyglow.color(colour, b)
    time.sleep(s / 1000)
    pyglow.color(colour, 0)

#Ring pulse (1 LED at a time)
for i in range(1,18):
    if(i>2):
        pyglow.led(i-2, int(0))
        
    if(i>1):
        pyglow.led(i-1, int(b/2))
        
    pyglow.led(i, b)
    
    if(i<18):
        pyglow.led(i+1, int(b/2))

    time.sleep(s/2000)
    
    
    
