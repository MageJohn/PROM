import constants

SIDES = {constants.LEFT: 1, constants.RIGHT: -1}


class Bat:
    def __init__(self, cg, side, color):
        self.cg = cg
        self.side = SIDES[side]
        self.col = (self.side * 3) % constants.SCR_WIDTH
        self.color = color
        self.y = 9
        self.old_y = 0
        self.length = constants.BAT_LENGTH
        self.old_length = 0
        self._superbats = constants.SUPERBATS
        self._superbat = False

    def move(self, y):
        if y in range(1, constants.SCR_HEIGHT - self.length + 2):
            self.old_y = self.y
            self.y = y

    def is_superbat(self):
        return self._superbat

    def enable_superbat(self):
        if self._superbats:
            self._superbat = True
            self.old_length = self.length
            self.length = constants.BAT_SUPERLENGTH
            self._superbats -= 1

    def disable_superbat(self):
        self._superbat = False
        self.old_length = self.length
        self.length = constants.BAT_LENGTH

    def draw(self):
        if self.old_y == self.y and self.old_length == self.length:
            return
        # Set the bacground color
        self.cg.write("\x1B[{}m".format(self.cg.bgcolor))

        # Move cursor to old y start
        self.cg.write("\x1B[{};{}H".format(self.old_y, self.col))

        # Color first block
        self.cg.write(self.cg.BG)
        for point in range(self.old_length - 1):
            # Move down one, then color next block
            self.cg.write("\x1B[B\x1B[D")
            self.cg.write(self.cg.BG)
        self.old_length = self.length

        # Set bat color
        self.cg.write("\x1B[{}m".format(self.color))

        # Move to current y
        self.cg.write("\x1B[{}d".format(self.y))

        self.cg.write("\x1B[D")

        # Color first block
        self.cg.write(self.cg.BG)
        for point in range(self.length - 1):
            # Move down one, then color next block
            self.cg.write("\x1B[B\x1B[D")
            self.cg.write(self.cg.BG)

    def collide(self, ball):
        collision = True
        if not (ball.pos[1] == self.col + self.side):
            collision = False
        elif ball.pos[0] in range(self.y - 1, self.y + self.length // 3):
            ball.vector = [-1, self.side]
        elif ball.pos[0] in range(self.y + self.length // 3,
                                  self.y + 2 * self.length // 3):
            ball.vector = [0, self.side]
        elif ball.pos[0] in range(self.y + 2 * self.length // 3,
                                  self.y + self.length + 1):
            ball.vector = [1, self.side]
        else:
            collision = False
        return collision
