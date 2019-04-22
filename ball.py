import random

import constants


class Ball:
    def __init__(self, cg, server, color):
        self.pos = [10, 40]
        self.oldpos = tuple(self.pos)
        self.vector = [1, 1]
        self.serving = False
        self.randomise_speed()

        self.server = server
        self.cg = cg
        self.color = color - 10

    def move(self):
        self.oldpos = tuple(self.pos)
        if not self.serving:
            self.pos[0] += self.vector[0]
            self.pos[1] += self.vector[1]
        else:
            self.pos[0] = self.server.y + self.server.length // 2
            self.pos[1] = self.server.col + self.server.side

    def randomise_speed(self):
        rand = random.uniform(0, 10)
        for i, w in enumerate(constants.BALL_SPEED_WEIGHTS):
            if rand < w:
                self.speed = constants.BALL_SPEEDS[i]
                break


    def draw(self):
        # Set fg and bg colors. 8 bytes
        self.cg.write("\x1B[{};{}m".format(
            self.cg.bg.get(self.oldpos, self.cg.bgcolor),
            self.color))

        # Move to old position. Max 8 bytes
        self.cg.write("\x1B[{0[0]};{0[1]}H".format(self.oldpos))
        # Write background character. 1 byte
        self.cg.write(self.cg.BG)

        # Move to current position. Max 8 bytes
        self.cg.write("\x1B[{0[0]};{0[1]}H".format(self.pos))
        # Write foreground character. 3 bytes.
        self.cg.write(self.cg.FG)

    def collide(self):
        vec = list(self.vector)
        if self.pos[0] <= 1 or self.pos[0] >= constants.SCR_HEIGHT:
            vec[0] = -vec[0]
            return vec
