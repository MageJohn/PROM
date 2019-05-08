import constants


class Net:
    def __init__(self, cg, color):
        self.cg = cg
        self.color = color

    def draw(self):
        mid = constants.SCR_WIDTH // 2

        # Set colors
        self.cg.write("\x1B[{}m".format(self.color))

        # Move to position
        self.cg.write("\x1B[{};{}H".format(1, mid))

        pen_down = True
        for i in range(1, constants.SCR_HEIGHT+1):
            if i % 2 == 1:
                pen_down = not pen_down
            if pen_down:
                self.cg.write(self.cg.BG + "\x1B[D")
                self.cg.bg[(i, mid)] = self.color
            self.cg.write("\x1B[B")
