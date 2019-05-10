class HardwareInputs:
    def __init__(self, knob, serve, superbat):
        self.knob = knob
        self.serve_button = serve
        self.superbat_button = superbat

        self.get_input()

    def get_input(self):
        self.knob.update()
        self.serve_button.update()
        self.superbat_button.update()

        return (self.knob.bat_y,
                self.serve_button.value,
                self.superbat_button.value)
