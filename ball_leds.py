import RPi.GPIO as gpio
import smbus

import constants


class BallLEDs:
    def __init__(self):
        self.init_onboard()
        self.init_i2c()

    def init_onboard(self):
        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        for pin in constants.BALL_LED_PINS:
            gpio.setup(pin, gpio.OUT)

    def init_i2c(self):
        self.bus = smbus.SMBus(1)

    def update_onboard(self, led):
        for i, pin in enumerate(constants.BALL_LED_PINS):
            if i == led:
                gpio.output(pin, True)
            else:
                gpio.output(pin, False)

    def update_i2c(self, led):
        self.bus.write_byte(constants.BALL_LED_I2C_ADDR, ~(2**led) & 0xFF)

    def update(self, pos):
        percentage = (pos - constants.SCR_MIN) / (constants.SCR_WIDTH - constants.SCR_MIN)
        led_number = int(round(7 * percentage))
        self.update_onboard(led_number)
        self.update_i2c(led_number)
