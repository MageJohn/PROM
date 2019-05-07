import time

import RPi.GPIO as gpio

import constants

ACTIVE_LOW = gpio.PUD_UP
ACTIVE_HIGH = gpio.PUD_DOWN


class GPIO_Button:
    def __init__(self, pin, active_low, debounce):
        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)

        if active_low:
            active = ACTIVE_LOW
        else:
            active = ACTIVE_HIGH

        gpio.setup(pin, gpio.IN, pull_up_down=active)

        self.pin = pin
        self.active_low = active_low
        self.debounce = debounce

        self.last_pressed_time = time.perf_counter()

        self.value = False


    def update(self):
        if not self.debounce or time.perf_counter() - self.last_pressed_time >= constants.DEBOUNCE_TIME:
            self.value = bool(gpio.input(self.pin))
            if self.active_low:
                self.value = not self.value

if __name__ == "__main__":
    button = GPIO_Button(pin=9, active_low=True, debounce=True)
    try:
        while True:
            button.update()
            print("\rButton {}".format("pressed" if button.value else "not pressed"), end='')
    except KeyboardInterrupt:
        print()
