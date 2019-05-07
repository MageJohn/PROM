import time
from PyGlow import PyGlow
from .. import constants

b = constants.PIGLOW_B
s = constants.PIGLOW_S
pyglow = PyGlow(brightness = b, speed = s, pulse=False)

pyglow.all(0) #Set all LEDs to 0

for i in range(1,18):
    if(i>2):
        pyglow.led(i-2, int(0))
        
    if(i>1):
        pyglow.led(i-1, int(b/2))
        
    pyglow.led(i, b)
    
    if(i<18):
        pyglow.led(i+1, int(b/2))

    time.sleep(s/10000)


pyglow.all(0) #Set all LEDs to 0
