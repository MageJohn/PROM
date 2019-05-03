## Credit:
## Midi to Raspberry Pi Converter
##     - Andy Tran (extramaster), 2015
## https://www.extramaster.net/tools/midiToArduino/
##
## Process:
## Midi -> Midi tracks -> Note mappings -> Frequency
##
## CC0

import RPi.GPIO as GPIO
import time

# Set this to be the pin that your buzzer resides in. (Note that you can only have one buzzer actively using the PWM signal at a time).

# GD = GND = Ground
 
# RPI v1 GPIO Layout BCM
# 5V 5V GD 14 15 18 GD 23 24 GD 25 08 07
# 3V 02 03 04 GD 17 27 22 3V 10 09 11 GD

# RPI v2 GPIO Layout BCM
# 5V 5V GD 14 15 18 GD 23 24 GD 25 08 07 SC GD 12 GD 16 20 21
# 3V 02 03 04 GD 17 27 22 3V 10 09 11 GD SD 05 06 13 19 26 GD 

# Note: Raspberry Pi 2 seems to handle software-PWM a lot better then the original Raspberry Pis.
tonePin = 21

GPIO.setmode(GPIO.BCM)  
GPIO.setup(tonePin, GPIO.IN)
GPIO.setup(tonePin, GPIO.OUT)
p = GPIO.PWM(tonePin, 100)

# High-level abstraction of the Arduino's Delay function
def delay(times):
    time.sleep(times/1000.0)
    
# High-level abstraction of the Arduino's Tone function, though this version is blocking
def tone(pin, pitch, duration):
    if pitch == 0:
        delay(duration)
        return
    p = GPIO.PWM(tonePin, pitch)
    
    # Change the duty-cycle to 50 if you wish
    p.start(30)
    delay(duration)
    p.stop()
    
    # Delay used to discourage overlap of PWM cycles
    delay(2)
    
def midi():
    tone(tonePin, 987, 129.292929293)
    tone(tonePin, 739, 129.292929293)
    tone(tonePin, 622, 129.292929293)
    tone(tonePin, 987, 64.6464646465)
    tone(tonePin, 739, 193.939393939)
    tone(tonePin, 123, 129.292929293)
    tone(tonePin, 123, 129.292929293)
    delay(143.658810325)
    tone(tonePin, 523, 129.292929293)
    tone(tonePin, 783, 129.292929293)
    tone(tonePin, 1046, 129.292929293)
    tone(tonePin, 659, 64.6464646465)
    tone(tonePin, 783, 193.939393939)
    tone(tonePin, 130, 129.292929293)
    tone(tonePin, 61, 129.292929293)
    tone(tonePin, 659, 129.292929293)
    tone(tonePin, 987, 129.292929293)
    tone(tonePin, 739, 129.292929293)
    tone(tonePin, 622, 129.292929293)
    tone(tonePin, 987, 64.6464646465)
    tone(tonePin, 739, 193.939393939)
    tone(tonePin, 123, 129.292929293)
    tone(tonePin, 622, 129.292929293)
    tone(tonePin, 622, 64.6464646465)
    tone(tonePin, 659, 64.6464646465)
    tone(tonePin, 92, 129.292929293)
    tone(tonePin, 698, 64.6464646465)
    tone(tonePin, 739, 64.6464646465)
    tone(tonePin, 103, 129.292929293)
    tone(tonePin, 783, 64.6464646465)
    tone(tonePin, 830, 64.6464646465)
    tone(tonePin, 880, 129.292929293)
    tone(tonePin, 1046, 4072.72727273)
    tone(tonePin, 130, 387.878787879)
    tone(tonePin, 493, 129.292929293)
    tone(tonePin, 61, 517.171717172)
    tone(tonePin, 123, 1292.92929293)


while 1:
    midi()
    GPIO.cleanup()