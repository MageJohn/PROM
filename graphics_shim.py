import sys

# The 3x5 digits
NUMS = ((1, 1, 1,
         1, 0, 1,
         1, 0, 1,
         1, 0, 1,
         1, 1, 1),
        (0, 0, 1,
         0, 0, 1,
         0, 0, 1,
         0, 0, 1,
         0, 0, 1),
        (1, 1, 1,
         0, 0, 1,
         1, 1, 1,
         1, 0, 0,
         1, 1, 1),
        (1, 1, 1,
         0, 0, 1,
         1, 1, 1,
         0, 0, 1,
         1, 1, 1),
        (1, 0, 1,
         1, 0, 1,
         1, 1, 1,
         0, 0, 1,
         0, 0, 1),
        (1, 1, 1,
         1, 0, 0, 
         1, 1, 1,
         0, 0, 1,
         1, 1, 1), 
        (1, 1, 1,
         1, 0, 0,
         1, 1, 1,
         1, 0, 1,
         1, 1, 1),
        (1, 1, 1,
         0, 0, 1,
         0, 0, 1,
         0, 0, 1, 
         0, 0, 1),
        (1, 1, 1,
         1, 0, 1, 
         1, 1, 1,
         1, 0, 1,
         1, 1, 1),
        (1, 1, 1,
         1, 0, 1,
         1, 1, 1,
         0, 0, 1,
         0, 0, 1)
        )


# Class to interact with the console
# Wraps ANSI escape sequences
class ConsoleGraphics:
    # Give the colors names
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37

    # The difference between the background and the forground colors
    LAYER_DIFF = 10

    # A flag for which layer to draw on
    FG = 'fg'
    BG = 'bg'

    def __init__(self, output=sys.stdout, bgcolor=BLACK):
        """
        output: the file-like object to print to
        bgcolor: the color to initialise the background to
        """
        self.out = output
        self.active = False
        self.bgcolor = bgcolor

    def _write(self, string):
        # internal function to write to the output
        print(string, file=self.out, end='')

    def init_screen(self):
        # save the cursor position
        self._write("\x1B7")
        # ?
        self._write("\x1B[?25l")
        # set background color
        self._write("\x1B[{}m".format(self.bgcolor + self.LAYER_DIFF))
        # clear screen, filling with bg color
        self._write("\x1B[2J")
        self.active = True

    def take_down_screen(self):
        self._write("\x1B[0m\x1B[2J\x1B8")

    def __enter__(self):
        self.init_screen()

    def __exit__(self, type, value, traceback):
        self.take_down_screen()

    def line(self, start, end=None, color=None, layer=FG):
        if not self.active:
            print("screen not initialised")

        if layer == self.BG:
            color += self.LAYER_DIFF
            char = ' '
        elif layer == self.FG:
            char = '█'

        if not end:
            end = start

        for y in range(start[0], end[0] + 1):
            for x in range(start[1], end[1] + 1):
                self._write("\x1B[{};{}H".format(y, x))
                if color:
                    self._write("\x1B[{}m".format(color))
                self._write(char)

    def num(self, num, pos, color, layer=BG):
        if not self.active:
            print("screen not initialised")

        if layer == self.BG:
            color += self.LAYER_DIFF
            char = ' '
        elif layer == self.FG:
            char = '█'

        self._write("\x1B[{0[0]};{0[1]}H".format(pos))
        self._write("\x1B[{}m".format(color))

        for i, p in enumerate(NUMS[num], start=1):
            if p:
                self._write(char)
            else:
                # move cursor 1 right
                self._write("\x1B[1C")

            if i % 3 == 0:
                # Move 1 line down and 3 left
                self._write("\x1B[1B\x1B[3D")

    def put_str(self, string, pos, color=None):
        if color:
            self._write("\x1B[{}m".format(color))
        self._write("\x1B[{0[0]};{0[1]}H".format(pos))
        self._write(string)
