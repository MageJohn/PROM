import RPi.GPIO as gpio

import constants


class BallLEDs:
    def __init__(self):
        self.init_onboard()

    def init_onboard(self):
        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        for pin in constants.BALL_LED_PINS:
            gpio.setup(pin, gpio.OUT)

    def update_onboard(self, led):
        for i, pin in enumerate(constants.BALL_LED_PINS):
            if i == led:
                gpio.output(pin, True)
            else:
                gpio.output(pin, False)

    def update(self, pos):
        percentage = (pos - constants.SCR_MIN) / (constants.SCR_WIDTH - constants.SCR_MIN)
        led_number = int(round(7 * percentage))
        self.update_onboard(led_number)
