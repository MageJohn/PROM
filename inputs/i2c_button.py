import time
import smbus

from .. import constants


class I2C_Button:
    def __init__(self, addr, bit, active_low, debounce):
        self.bus = smbus.SMBus(1)
        self.addr = addr
        self.mask = 2**bit
        self.active_low = active_low
        self.debounce = debounce
        self.last_pressed_time = time.perf_counter()

        self.update()

    def update(self):
        if not self.debounce or time.perf_counter() - self.last_pressed_time >= constants.DEBOUNCE_TIME:
            self.bus.write(self.addr, 0xFF)
            self.value = bool(self.bus.read_byte(self.addr) & self.mask)
            if self.active_low:
                self.value = not self.value

if __name__ == "__main__":
    button = I2C_Button(addr=0x38, bit=6, active_low=True, debounce=False)
    try:
        while True:
            button.update()
            print("\rButton {}".format("pressed" if button.value else "not pressed"), end='')
    except KeyboardInterrupt:
        print()

