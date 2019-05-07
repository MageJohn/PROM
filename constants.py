import sys

from .consolegraphics import ConsoleGraphics as cg
from . import sound

LOCAL = True

# Screen sizes
SCR_WIDTH = 80
SCR_HEIGHT = 24
SCR_MIN = 1

I2C_BUS = 1

AD799_ADDR = 0x21
DIY_ADC_ADDR = 0x38

DIY_ADC_N_BITS = 6

PIN0 = 10
PIN1 = 9
PIN2 = 11
PIN3 = 14
PIN4 = 15

BUTTONS_ACTIVE_LOW = True

I2C_BUTTON0_ADDR = 0x38
I2C_BUTTON0_BIT = 6
I2C_BUTTON1_ADDR = 0x38
I2C_BUTTON1_BIT = 7

P1_AI = False
P2_AI = False

if LOCAL:
    from .inputs import ai
    from .sound import dummy_sound

    OUTPUT = sys.stdout
    DEBUG = False
    P1_INTERFACE = ai.AI()
    P2_INTERFACE = ai.AI()
    FLUSHING = True
    SOUND = dummy_sound.SoundPlayer
else:
    from . import inputs
    from .serial_wrapper import TextSerial
    from .sound import sound_player

    OUTPUT = TextSerial("/dev/ttyAMA0", 115200)
    DEBUG = True

    if not P1_AI:
        p1_knob = inputs.ad799_knob.AD799(AD799_ADDR)
        p1_serve = inputs.gpio_button.GPIO_Button(PIN1, BUTTONS_ACTIVE_LOW, debounce=True)
        p1_superbat = inputs.gpio_button.GPIO_Button(PIN2, BUTTONS_ACTIVE_LOW, debounce=True)
        P1_INTERFACE = inputs.interface.HardwareInputs(p1_knob, p1_serve, p1_superbat)

    if not P2_AI:
        p2_knob = inputs.diy_knob.DIY_ADC(I2C_BUS, PIN0, DIY_ADC_ADDR, DIY_ADC_N_BITS)
        p2_serve = inputs.i2c_button.I2C_Button(I2C_BUTTON0_ADDR, I2C_BUTTON0_BIT, BUTTONS_ACTIVE_LOW, debounce=False)
        p2_superbat = inputs.i2c_button.I2C_Button(I2C_BUTTON1_ADDR, I2C_BUTTON1_BIT, BUTTONS_ACTIVE_LOW, debounce=False)
        P2_INTERFACE = inputs.interface.HardwareInputs(p2_knob, p2_serve, p2_superbat)

    SOUND = sound_player.SoundPlayer

    FLUSHING = False


SOUND_PIN = PIN3
WALL_TONE = 131
BAT_TONE = 131
TONE_LENGTH = 30
INTRO_MUS = sound.pacman.notes

# Speed at which the AI moves
AI_SPEED = 3/SCR_HEIGHT

INPUT_AD799_MAX = 4092
INPUT_AD799_MIN = 0

INPUT_DIY_ADC_MAX = 45
INPUT_DIY_ADC_MAX = 0

DEBOUNCE_TIME = 0.2

# Speeds the ball can go at
# Expressed as time per refresh
# n/SCR_WIDTH means the ball will cross the screen in n seconds.
BALL_SPEEDS = [2/SCR_WIDTH, 3/SCR_WIDTH, 4/SCR_WIDTH]
# Probability weighting for the different speeds
# The wieghts are cumulative
BALL_SPEED_WEIGHTS = [2.5, 7.5, 10]

# Speed at which to refresh the bat position
# Expressed as time per refresh
BAT_SPEED = 1/60

BAT_LENGTH = 3
BAT_SUPERLENGTH = 6

# Number of superbats per game
SUPERBATS = 2
# How long the superbats last in seconds
SUPERBAT_TIME = 15

# The colors for different game objects
BALL_COL = cg.RED
BG_COL = cg.BLACK
NET_COL = cg.GREEN
SCORE_COL = cg.CYAN
BAT_COL = cg.MAGENTA

# Constants to help distinguish between which side of the field a thing is on
# Used differently by different classes
LEFT = 'left'
RIGHT = 'right'

# PiGlow brightness and speed
PIGLOW_B = 255 #Brightness from 0-255
PIGLOW_S = 1000 #Speed in milliseconds
