import constants


class Bat:
    LEFT = 1
    RIGHT = -1
    LENGTH = 3
    SUPERLENGTH = 6

    def __init__(self, cg, side, color):
        self.cg = cg
        self.side = side
        self.col = (side * 3) % constants.SCR_WIDTH
        self.color = color
        self.y = 9
        self.old_y = self.y
        self.length = self.LENGTH

    def move(self, y):
        if y in range(1, constants.SCR_HEIGHT - self.length + 2):
            self.old_y = self.y
            self.y = y

    def draw(self):
        # Set the bacground color
        self.cg.write("\x1B[{}m".format(self.cg.bgcolor))

        # Move cursor to old y start
        self.cg.write("\x1B[{};{}H".format(self.old_y, self.col))

        # Color first block
        self.cg.write(self.cg.BG)
        for point in range(self.length - 1):
            # Move down one, then color next block
            self.cg.write("\x1B[B\x1B[D")
            self.cg.write(self.cg.BG)

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
        if not (ball.pos[1] == self.col + self.side):
            return
        if ball.pos[0] in range(self.y - 1, self.y + self.length // 3):
            return [-1, self.side]
        elif ball.pos[0] in range(self.y + self.length // 3,
                                  self.y + 2 * self.length // 3):
            return [0, self.side]
        elif ball.pos[0] in range(self.y + 2 * self.length // 3, 
                                  self.y + self.length + 1):
            return [1, self.side]

