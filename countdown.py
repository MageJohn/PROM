import smbus
import time


class Countdown:
    def __init__(self, bus, addr, n_bits, lsb, speed):
        self.bus = smbus.SMBus(bus)
        self.addr = addr
        self.n_bits = n_bits
        self.lsb = lsb
        self.speed = speed

    def activate(self):
        for n in range(2**self.n_bits - 1, -1, -1):
            self.bus.write_byte(self.addr, n << self.lsb)
            time.sleep(self.speed)
