import time
import smbus

import constants


class I2C_Button:
    def __init__(self, addr, bit, active_low, debounce):
        self.bus = smbus.SMBus(1)
        self.addr = addr
        self.mask = 2**bit
        self.active_low = active_low
        self.debounce = debounce
        self.last_pressed_time = time.perf_counter()
        self.value = False

        self.update()

    def update(self):
        if not self.debounce or time.perf_counter() - self.last_pressed_time >= constants.DEBOUNCE_TIME:
            self.bus.write_byte(self.addr, 0xFF)
            self.value = bool(self.bus.read_byte(self.addr) & self.mask)
            if self.active_low:
                self.value = not self.value

if __name__ == "__main__":
    buttons = (I2C_Button(addr=constants.I2C_BUTTON0_ADDR, 
                          bit=constants.I2C_BUTTON0_BIT,
                          active_low=constants.BUTTONS_P1_ACTIVE_LOW,
                          debounce=False),
               I2C_Button(addr=constants.I2C_BUTTON1_ADDR,
                          bit=constants.I2C_BUTTON1_BIT,
                          active_low=constants.BUTTONS_P1_ACTIVE_LOW,
                          debounce=False),
               I2C_Button(addr=constants.I2C_BUTTON2_ADDR,
                          bit=constants.I2C_BUTTON2_BIT,
                          active_low=constants.BUTTONS_P2_ACTIVE_LOW,
                          debounce=False),
               I2C_Button(addr=constants.I2C_BUTTON3_ADDR,
                          bit=constants.I2C_BUTTON3_BIT,
                          active_low=constants.BUTTONS_P2_ACTIVE_LOW,
                          debounce=False))
    try:
        while True:
            out = "\r"
            for i, button in enumerate(buttons):
                button.update()
                out += "Button {} = {} ".format(i, button.value)
            print(out, end='')
    except KeyboardInterrupt:
        print()

