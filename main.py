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

def init_screen():
    pass

def main():
    ball = Ball()
    p1 = Bat()
    p2 = Bat()

    cg = ConsoleGraphics(output = constants.OUTPUT)

    with cg:
        init_screen()
        playing = True
        while playing:
            # update ball
            cg.line(ball.pos, ball.pos, constants.BG_COL)
            ball.update()
            cg.line(ball.pos, ball.pos, constants.BALL_COL)

            # flush to screen
            sys.stdout.flush()
            time.sleep(0.1)



if __name__ == "__main__":
    main()
