# Based off code written by Mike Freeman:
# https://www-users.cs.york.ac.uk/~mjf/pi_time/index.html#LS
import time
import smbus

import RPi.GPIO as gpio

import constants


class DIY_ADC():
    def __init__(self, bus, pin, i2c_addr, bits):
        self.i2c_addr = i2c_addr
        self.bus = smbus.SMBus(bus)
        self.pin = pin
        self.bits = bits

        self.bus.write_byte(self.i2c_addr, 0)  # clear port

        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        gpio.setup(self.pin, gpio.IN, pull_up_down=gpio.PUD_UP)

    def _write(self, value):
        self.bus.write_byte(self.i2c_addr, value)

    def _get_comp(self):
        return gpio.input(self.pin)

    def ramp(self):
        count = 0
        for i in range((2**self.bits) - 1):
            self._write(i)
            if self._get_comp():
                count += 1
            else:
                break

        self.value = count

    def approx(self):
        count = 0
        new = 0
        for i in range(self.bits):
            new = count | 2**((self.bits - 1) - i)
            self._write(new)
            time.sleep(0.001)
            if not self._get_comp():
                count = new

        self.value = count

    def update(self):
        # could also use the ramp function
        self.approx()
        percentage = (self.value - constants.INPUT_DIY_ADC_MIN) / \
                     (constants.INPUT_DIY_ADC_MAX - constants.INPUT_DIY_ADC_MIN)

        self.bat_y = int((percentage * (constants.SCR_HEIGHT - constants.SCR_MIN)) + constants.SCR_MIN)


if __name__ == '__main__':
    BUS = constants.I2C_BUS
    PIN = constants.DIY_ADC_PIN
    I2C_ADDR = constants.DIY_ADC_ADDR
    BITS = constants.DIY_ADC_N_BITS

    adc = DIY_ADC(BUS, PIN, I2C_ADDR, BITS)

    try:
        while True:
            adc.update()
            print("\rvalue = {:<4}, y = {:<2}".format(adc.value, adc.bat_y), end='')
    except KeyboardInterrupt:
        print()
