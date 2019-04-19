import time
import sys

from graphics_shim import ConsoleGraphics
import constants


class Ball:
    def __init__(self):
        self.pos = [10, 40]
        self.vector = [1, 1]

    def update(self):
        self.pos[0] += self.vector[0]
        self.pos[1] += self.vector[1]
        if self.pos[0] >= constants.SCR_HEIGHT or\
                self.pos[0] <= 1:
            self.vector[0] = -self.vector[0]
        if self.pos[1] >= constants.SCR_WIDTH or\
                self.pos[1] <= 1:
            self.vector[1] = -self.vector[1]


class Bat:
    pass


class Net:
    def __init__(self, cg):
        self.cg = cg

    def update(self):
        mid = constants.SCR_WIDTH // 2
        pen_down = True
        for i in range(1, constants.SCR_HEIGHT+1):
            if i % 2 == 1:
                pen_down = not pen_down
            if pen_down:
                self.cg.line((i, mid), color=constants.NET_COL,
                             layer=self.cg.BG)


class Score:
    LEFT = -(8 + 3)
    RIGHT = 8

    def __init__(self, cg, side):
        self.cg = cg
        self.side = side

    def update(self):
        mid = constants.SCR_WIDTH // 2
        self.cg.num(0, (2, mid + self.side), constants.SCOR_COL)


def main():
    ball = Ball()

    cg = ConsoleGraphics(output=constants.OUTPUT)

    with cg:
        net = Net(cg)
        p1 = Score(cg, Score.LEFT)
        p2 = Score(cg, Score.RIGHT)

        playing = True
        while playing:
            cg.line(ball.pos, color=constants.BG_COL)

            net.update()
            p1.update()
            p2.update()

            ball.update()
            cg.line(ball.pos, color=constants.BALL_COL)

            # flush updates to screen
            constants.OUTPUT.flush()

            time.sleep(0.1)



if __name__ == "__main__":
    main()
