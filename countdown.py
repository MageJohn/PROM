import smbus
import time

I2C_ADDR = 0x24
CONF_REG = 0x03
WRITE_ENABLE = 0x01
OUT_REG = 0x01

class Countdown:
    def __init__(self, bus, n_bits, lsb, speed):
        self.bus = smbus.SMBus(bus)
        self.n_bits = n_bits
        self.lsb = lsb
        self.speed = speed

        self.bus.write_byte_data(I2C_ADDR, CONF_REG, WRITE_ENABLE)

    def activate(self):
        for n in range(2**self.n_bits - 1, -1, -1):
            self.bus.write_byte_data(I2C_ADDR, OUT_REG, n << self.lsb)
            time.sleep(self.speed)
