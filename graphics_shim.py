import sys

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



class ConsoleGraphics:
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    LAYER_DIFF = 10
    FG = 'fg'
    BG = 'bg'

    def __init__(self, output=sys.stdout, bgcolor=BLACK, fgcolor=WHITE):
        self.out = output
        self.active = False
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor

    def write(self, string):
        print(string, file=self.out, end='')

    def init_screen(self):
        self.write("\x1B7")
        self.write("\x1B[?25l\x1B[{};{}m\x1B[2J".format(self.fgcolor, self.bgcolor + self.LAYER_DIFF))
        self.active = True

    def take_down_screen(self):
        self.write("\x1B[0m\x1B[2J\x1B8")

    def __enter__(self):
        self.init_screen()
    
    def __exit__(self, type, value, traceback):
        self.take_down_screen()

    def line(self, start, end, color, layer=FG):
        if not self.active:
            print("screen not initialised")
        if layer == self.BG:
            color += self.LAYER_DIFF
            char = ' '
        elif layer == self.FG:
            char = '█'
        for y in range(start[0], end[0] + 1):
            for x in range(start[1], end[1] + 1):
                self.write("\x1B[{};{}H\x1B[{}m{}".format(y, x, color, char))

    def num(self, num, pos, color, layer=FG):
        if not self.active:
            print("screen not initialised")
        if layer == self.BG:
            color +=  self.LAYER_DIFF
            char = ' '
        elif layer == self.FG:
            char = '█'
        self.write("\x1B[{};{}H\x1B[{}m".format(pos[0], pos[1], color))
        point = 0
        for p in NUMS[num]:
            if p:
                self.write(char)
            else:
                self.write("\x1B[1C")
            point += 1
            if point % 3 == 0:
                self.write("\x1B[1B\x1B[3D")

