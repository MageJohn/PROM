import time
import random

import constants

MISS_GAP = 2


class AIError(Exception):
    pass


class AI:
    def __init__(self, ball=None, bat=None):
        self.prev_ball_state = (None, None, None)
        self.refresh_time = time.perf_counter()
        self.knob = Knob()
        self.serve_button = Button()
        self.superbat_button = Button()
        self.ball = None
        self.bat = None
        self.give_inputs(ball=ball, bat=bat)

    def give_inputs(self, ball=None, bat=None):
        if ball:
            self.ball = ball
        if bat:
            self.bat = bat
        self.inputs_given = self.ball and self.bat

    def get_input(self):
        if not self.inputs_given:
            raise AIError

        if not time.perf_counter() - self.refresh_time >= constants.AI_SPEED:
            self.knob.bat_y = self.bat.y
            self.knob.value = self.bat.y
            self.serve_button.value = False
            self.superbat_button.value = False
        else:
            self.refresh_time = time.perf_counter()

            ball_state = (self.ball.vector[1], self.ball.serving, self.bat.is_superbat())
            if ball_state != self.prev_ball_state:
                self.calc_ball_target()
                self.prev_ball_state = ball_state

            delta_y = self.target - self.bat.y
            if delta_y:
                use_superbat = delta_y >= constants.SCR_HEIGHT / 2 and not self.ball.serving
                step = delta_y // abs(delta_y)
                self.knob.bat_y = self.bat.y + step
                self.knob.value = self.knob.bat_y
                self.serve_button.value = False
                self.superbat_button.value = use_superbat
            elif self.ball.serving and self.ball.server is self.bat:
                self.knob.bat_y = self.bat.y
                self.knob.value = self.knob.bat_y
                self.serve_button.value = True
                self.superbat_button.value = False
            else:
                self.knob.bat_y = self.bat.y
                self.knob.value = self.knob.bat_y
                self.serve_button.value = False
                self.superbat_button.value = False
        return (self.knob.bat_y, self.serve_button.value, self.superbat_button.value)

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

class Knob:
    def __init__(self):
        self.value = 0
        self.bat_y = 0

class Button:
    def __init__(self):
        self.value = 0
