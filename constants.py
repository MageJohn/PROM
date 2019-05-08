import sys

from consolegraphics import ConsoleGraphics as cg
import sound_pacman

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

P1_AI = True
P2_AI = True

if LOCAL:
    from input_ai import AI
    import sound_dummy

    OUTPUT = sys.stdout
    DEBUG = False
    FLUSHING = True
    SOUND = sound_dummy.SoundPlayer

    P1_AI = True
    P2_AI = True
else:
    from textserial import TextSerial
    import sound_player

    OUTPUT = TextSerial("/dev/ttyAMA0", 115200)
    DEBUG = True

    SOUND = sound_player.SoundPlayer

    FLUSHING = False


SOUND_PIN = PIN3
WALL_TONE = 131
BAT_TONE = 131
TONE_LENGTH = 30
INTRO_MUS = sound_pacman.notes

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

BALL_LED_PINS = (5, 6, 12, 13, 16, 19, 20, 26)
