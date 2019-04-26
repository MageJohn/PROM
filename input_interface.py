import constants
import smbus

I2C_ADDR = 0x21


class AD799:
    CH1 = 0x10
    CH2 = 0x20
    CH3 = 0x40
    CH4 = 0x80

    def __init__(self, channel=CH1):
        self.bus = smbus.SMBus(1)
        self.code = channel

    def get_input(self):
        self.bus.write_byte(I2C_ADDR, self.code)
        little_endian = self.bus.read_word_data(I2C_ADDR, 0x00)

        big_endian = ((little_endian << 8) & 0xFF00) | (little_endian >> 8)

        value = big_endian & 0x0FFF

        percentage = (value - constants.INPUT_AD799_MIN) / \
                     (constants.INPUT_AD799_MAX - constants.INPUT_AD799_MIN)

        y = int((percentage * (constants.SCR_HEIGHT - constants.SCR_MIN)) + 1)
        return (y, True, False)
