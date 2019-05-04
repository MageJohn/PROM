from .. import constants

NUM_WIDTH = 3
NUM_HEIGHT = 5

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

SIDES = {constants.LEFT: -(8 + 3), constants.RIGHT: 8}
ROW = 2


class Score:

    def __init__(self, cg, side, color):
        self.cg = cg
        mid = constants.SCR_WIDTH // 2
        self.side = mid + SIDES[side]
        self._score = 0
        self.color = color

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if type(value) is int and value in range(10):
            self._score = value

    def draw(self):
        for i in range(2):
            color = self.cg.bgcolor if i else self.color
            # Set the background color
            self.cg.write("\x1B[{}m".format(color))

            # Move cursor to position
            self.cg.write("\x1B[{0};{1}H".format(ROW, self.side))

            for row in range(NUM_HEIGHT):
                for col in range(NUM_WIDTH):
                    cursor = ROW+row, self.side+col
                    if NUMS[self.score][row*3 + col] != i:
                        self.cg.bg[cursor] = color
                        self.cg.write(self.cg.BG)
                    else:
                        self.cg.write("\x1B[C")

                # Move back to beginning of the line and down one line
                self.cg.write("\x1B[{}D\x1B[B".format(NUM_WIDTH))
