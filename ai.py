import constants
import random

MISS_GAP = 2

class AI:
    def __init__(self, ball, bat):
        self.ball = ball
        self.bat = bat

    def get_input(self):
        if self.ball.serving:
            return (self.bat.y, True, False)
        else:
            return (self.bat.y + (1 if self.target - self.bat.y > 0 else (-1 if self.target - self.bat.y < 0 else 0)),
                    False, False)

    @property
    def target(self):
        if self.ball.vector[1] != self.bat.side:
            unbounded_y = (self.ball.pos[0] - 1) + abs((self.bat.col + self.bat.side) - self.ball.pos[1]) * self.ball.vector[0]
            target = (((unbounded_y % (constants.SCR_HEIGHT - 1)) * (-1)**(unbounded_y // (constants.SCR_HEIGHT - 1))) % (constants.SCR_HEIGHT - 1)) + 1
            target += random.randrange(-(self.bat.length + MISS_GAP), 2 + MISS_GAP)
            return target
        else:
            return self.bat.y
