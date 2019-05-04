from .. import constants
import smbus

CH1 = 0x10
CH2 = 0x20
CH3 = 0x40
CH4 = 0x80


class AD799:
    def __init__(self, addr, channel=CH1):
        self.addr
        self.bus = smbus.SMBus(1)
        self.code = channel

    def update(self):
        self.bus.write_byte(self.addr, self.code)
        little_endian = self.bus.read_word_data(self.addr, 0x00)

        # the bytes come in the wrong order
        big_endian = ((little_endian << 8) & 0xFF00) | (little_endian >> 8)

        # the first for bits aren't useful
        value = big_endian & 0x0FFF

        percentage = (value - constants.INPUT_AD799_MIN) / \
                     (constants.INPUT_AD799_MAX - constants.INPUT_AD799_MIN)

        y = int((percentage * (constants.SCR_HEIGHT - constants.SCR_MIN)) + 1)

        self.value = value
        self.bat_y = y


if __name__ == '__main__':
    adc = AD799(addr=0x21)

    try:
        while True:
            adc.update()
            print("\rvalue = {}, y = {}".format(adc.value, adc.bat_y), end='')
    except KeyboardInterrupt:
        print()
