import sys


class ConsoleGraphics:
    """
    A context manager for writing to the terminal. When entered the screen
    is prepared to show graphics, and when exited it always returns the screen
    to a usable state
    """
    # Give the colors names
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    WHITE = 47
    DEFAULT = 49

    # A flag for which layer to draw on
    FG = '█'
    BG = ' '

    def __init__(self, output=sys.stdout, bgcolor=DEFAULT,
                 hide_cursor=True, alt_buf=True):
        """
        output: the file-like object to print to
        bgcolor: the color to initialise the background to
        hide_cursor: whether or not to hide the cursor. Can be useful for 
                     debugging
        alt_buf: whether or not to switch to the alternate buffer. Useful for
                 debugging
        """
        self.out = output
        self.active = False
        self.bgcolor = bgcolor
        self.bg = {}
        self.hide_cursor = hide_cursor
        self.alt_buf = alt_buf

    def write(self, string):
        """Write string to stdout"""
        if not self.active:
            print("screen not initialised")
            sys.exit()
        print(string, file=self.out, end='')

    def __enter__(self):
        """Set up screen for showing graphics"""
        self.active = True

        if self.alt_buf:
            # save the cursor position and use alternate buffer
            self.write("\x1B[?1049h")
        if self.hide_cursor:
            # Hide cursor
            self.write("\x1B[?25l")
        # set background color
        self.write("\x1B[{}m".format(self.bgcolor))
        # clear screen, filling with bg color
        self.write("\x1B[2J")

    def __exit__(self, type, value, traceback):
        """Return the screen to a usable terminal"""
        # Remove all text attributes
        self.write("\x1B[0m")
        if self.hide_cursor:
            # Set normal cursor
            self.write("\x1B[?25h")
        # Clear screen
        self.write("\x1B[2J")
        if self.alt_buf:
            # Restore cursor position and use normal buffer
            self.write("\x1B[?1049l")

        self.active = False
