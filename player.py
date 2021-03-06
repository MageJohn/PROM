import time
import random

import constants
import game_objects.score
import game_objects.bat


class Player:
    def __init__(self, cg, ball, side, interface):
        self.ball = ball
        self.bat = game_objects.bat.Bat(cg, side, constants.BAT_COL)
        self.score = game_objects.score.Score(cg, side, constants.SCORE_COL)
        self.interface = interface
        self.superbat_time = 0

    def update(self):
        inp = self.interface.get_input()
        self.bat.move(inp[0])
        if inp[1] and self.ball.server is self.bat and self.ball.serving:
            self.ball.serving = False
            self.ball.just_served = True
            self.ball.vector = [random.choice((-1, 0, 1)),
                                self.ball.server.side]
        if inp[2] and not self.bat.is_superbat():
            self.bat.enable_superbat()
            self.superbat_time = time.perf_counter()

        if time.perf_counter() - self.superbat_time > \
                constants.SUPERBAT_TIME:
            self.bat.disable_superbat()
            self.superbat_time = 0
