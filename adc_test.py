import RPi.GPIO as gpio
import smbus
import time


class adc():
    def __init__(self, bus, pin):
        self.I2C_DATA_ADDR = 0x38

        self.bus = bus

        self.bus.write_byte(self.I2C_DATA_ADDR, 0)    	# clear port

        self.pin = pin
        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        gpio.setup(self.pin, gpio.IN, pull_up_down=gpio.PUD_UP)

    def update(self, value):
        self.bus.write_byte(self.I2C_DATA_ADDR, value)

    def get_comp(self):
        return gpio.input(self.pin)

    def ramp(self):
        count = 0
        self.update(0)
        for i in range(0, 255):
            if self.get_comp() == False:
                count = count + 1
                self.update(i)
            else:
                break

        return count

    def approx(self):
        count = 0
        new = 0
        self.update(0)
        for i in range(0, 8):
            new = count | 2**(7-i)
            # print(i, count, new)

            self.update(new)
            if not self.get_comp():
                count = new

        return count


# Main program block

def main():
    print("main start")

    bus = smbus.SMBus(1)
    adc1 = adc(bus, 25)

    while True:
        # value = adc1.ramp()
        value = adc1.approx()
        print(value)

        time.sleep(0.001)


if __name__ == '__main__':
    main()
