import sys

from consolegraphics import ConsoleGraphics as cg
import sound.pacman

# Flag used to easily switch between sets of constants designed
# for local testing or actual running
LOCAL = True

# Screen sizes
SCR_WIDTH = 80
SCR_HEIGHT = 24
SCR_MIN = 1

P1_AI = False
P2_AI = False

if LOCAL:
    import sound.dummy

    OUTPUT = sys.stdout
    DEBUG = False
    FLUSHING = True
    SOUND = sound.dummy.SoundPlayer

    PIGLOW = False
    BALL_LEDS = False
    COUNTDOWN = False

    P1_AI = True
    P2_AI = True
else:
    from textserial import TextSerial
    import sound.player

    OUTPUT = TextSerial("/dev/ttyAMA0", 115200)
    DEBUG = True
    FLUSHING = False
    SOUND = sound.player.SoundPlayer

    PIGLOW = True
    BALL_LEDS = False
    COUNTDOWN = True

I2C_BUS = 1

#
# Various constants used to interface with the controllers
#

AD799_ADDR = 0x21
AD799_MAX = 4090
AD799_MIN = 0
AD799_MOVING_AVERAGE_BUF_SIZE = 10
AD799_USE_MOVING_AVERAGE = True

DIY_ADC_MAX = 40
DIY_ADC_MIN = 0
DIY_ADC_ADDR = 0x38
DIY_ADC_N_BITS = 6
DIY_ADC_PIN = 9

BUTTONS_P1_ACTIVE_LOW = True
BUTTONS_P2_ACTIVE_LOW = False

BUTTON0_ADDR = 0x38
BUTTON0_BIT = 6
BUTTON0_ACTIVE_LOW = True
BUTTON1_ADDR = 0x38
BUTTON1_BIT = 7
BUTTON1_ACTIVE_LOW = True
BUTTON2_ADDR = 0x3A
BUTTON2_BIT = 6
BUTTON2_ACTIVE_LOW = False
BUTTON3_ADDR = 0x3A
BUTTON3_BIT = 7
BUTTON3_ACTIVE_LOW = False

# Delay between each decrement of the countdown
COUNTDOWN_SPEED = 0.5
COUNTDOWN_ADDR = 0x3A
COUNTDOWN_N_BITS = 2
COUNTDOWN_LSB = 0

# Sound settings
SOUND_PIN = 3
WALL_TONE = 131
BAT_TONE = 131
TONE_LENGTH = 30
INTRO_MUS = sound.pacman.notes

# Speed at which the AI moves
AI_SPEED = 3/SCR_HEIGHT

# How long to disable a button for when debouncing is enabled
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

# Default length of the bat in characters
BAT_LENGTH = 3
# Length as superbat
BAT_SUPERLENGTH = 6

# Number of superbats per game
SUPERBATS = 2
# How long the superbats last in seconds
SUPERBAT_TIME = 15

# Number of serves before switching sides
N_SERVES = 5

# Winning score
WIN_SCORE = 9

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
PIGLOW_B = 128  # Brightness from 0-255
PIGLOW_S = 500  # Speed in milliseconds

# The GPIO pins that the ball indicator LEDs are on
BALL_LED_PINS = (5, 6, 12, 13, 16, 19, 20, 26)
# The address of the I2C expander chip for the addition ball LEDs
BALL_LED_I2C_ADDR = 0x39

