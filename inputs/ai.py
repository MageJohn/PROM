import sys
import time
import random

from .. import constants

MISS_GAP = 2


class AIError(Exception):
    pass


class AI:
    def __init__(self):
        self.prev_ball_state = (None, None, None)
        self.inputs_given = False
        self.refresh_time = time.perf_counter()

    def give_inputs(self, ball, bat):
        self.ball = ball
        self.bat = bat
        self.inputs_given = True

    def get_input(self):
        if not self.inputs_given:
            raise AIError

        if not time.perf_counter() - self.refresh_time >= constants.AI_SPEED:
            return (self.bat.y, False, False)

        self.refresh_time = time.perf_counter()

        ball_state = (self.ball.vector[1], self.ball.serving, self.bat.is_superbat())
        if ball_state != self.prev_ball_state:
            self.calc_ball_target()
            self.prev_ball_state = ball_state

        delta_y = self.target - self.bat.y
        if delta_y:
            use_superbat = delta_y >= constants.SCR_HEIGHT / 2 and not self.ball.serving
            step = delta_y // abs(delta_y)
            return (self.bat.y + step, False, use_superbat)
        elif self.ball.serving and self.ball.server is self.bat:
            return (self.bat.y, True, False)
        else:
            return (self.bat.y, False, False)

    def calc_ball_target(self):
        if self.ball.serving and self.ball.server is self.bat:
            self.target = random.randrange(1, constants.SCR_HEIGHT - self.bat.length + 1)
        elif self.ball.vector[1] == -self.bat.side:
            zero_based_y = self.ball.pos[0] - 1
            zero_based_height = constants.SCR_HEIGHT - 1
            distance = abs((self.bat.col + self.bat.side) - self.ball.pos[1])
            unbounded_y = zero_based_y + distance * self.ball.vector[0]
            wrapped_y = unbounded_y % zero_based_height
            bounced_y = int(wrapped_y * (-1)**(unbounded_y // zero_based_height))
            target_y = (bounced_y % zero_based_height) + 1
            target_y += random.randrange(-(self.bat.length + MISS_GAP),
                                         2 + MISS_GAP)
            self.target = target_y
        else:
            self.target = self.bat.y

        try:
            assert type(self.target) is int
        except AssertionError:
            raise AIError
