import sys
from graphics_shim import ConsoleGraphics as cg

LOCAL = True

# Screen sizes
SCR_WIDTH = 80
SCR_HEIGHT = 24
SCR_MIN = 1

# A file-like object for output
if LOCAL:
    OUTPUT = sys.stdout

    # Whether or not to flush the output. May not be necessary over serial
    FLUSHING = True
else:
    from serial_wrapper import TextSerial
    OUTPUT = TextSerial("/dev/ttyAMA0", 115200)

    FLUSHING = False

# Speed at which the AI responds
AI_SPEED = 5/SCR_HEIGHT
AI_P1 = True
AI_P2 = True

INPUT_AD799_MAX = 4092
INPUT_AD799_MIN = 0

# Speeds the ball can go at
# Expressed as time per refresh
# n/80 means the ball will cross the screen (80 columns) in n seconds.
BALL_SPEEDS = [2/SCR_WIDTH, 3/SCR_WIDTH, 4/SCR_WIDTH]
# Probability weighting for the different speeds
# The wieghts are cumulative
BALL_SPEED_WEIGHTS = [2.5, 7.5, 10]

# Speed at which to refresh the bat position
# Expressed as time per refresh
BAT_SPEED = 1/60

# The colors for different game objects
BALL_COL = cg.RED
BG_COL = cg.BLACK
NET_COL = cg.GREEN
SCOR_COL = cg.CYAN
BAT_COL = cg.MAGENTA
