import RPi.GPIO as gpio
import smbus
import time


PIN = 10
I2C_ADDR = 0x38
BITS = 8


class adc():
    def __init__(self, bus, pin, i2c_addr, bits):
        self.i2c_addr = i2c_addr
        self.bus = bus
        self.pin = pin
        self.bits = bits

        self.bus.write_byte(self.i2c_addr, 0)  # clear port

        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        gpio.setup(self.pin, gpio.IN, pull_up_down=gpio.PUD_UP)

    def _update(self, value):
        self.bus.write_byte(self.i2c_addr, value)

    def _get_comp(self):
        return gpio.input(self.pin)

    def ramp(self):
        count = 0
        for i in range((2**self.bits) - 1):
            self._update(i)
            if self._get_comp():
                count += 1
            else:
                break

        return count

    def approx(self):
        count = 0
        new = 0
        for i in range(self.bits):
            new = count | 2**((self.bits - 1) - i)
            self._update(new)
            time.sleep(0.1)
            if self._get_comp():
                count = new

        return count


# Main program block

def main():
    bus = smbus.SMBus(1)
    adc1 = adc(bus, PIN, I2C_ADDR, BITS)

    while True:
        # value = adc1.ramp()
        value = adc1.approx()
        print(value)

        time.sleep(0.1)


if __name__ == '__main__':
    main()
