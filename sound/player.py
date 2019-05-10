import time

import RPi.GPIO as gpio


class SoundPlayer:
    def __init__(self, pin, dc=30, note_gap=2):
        self._buffer = []
        self._cur_note = None
        self._note_started = 0
        self._duration = 0

        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        gpio.setup(pin, gpio.OUT)
        self._pwm = gpio.PWM(pin, 100)

        self.dc = dc
        self.note_gap = note_gap

    def note(self, note):
        if not self._buffer:
            self._buffer.append(note)

    def notes(self, notes):
        self._buffer = notes

    def update(self):
        # time playing in milliseconds
        time_playing = (time.perf_counter() - self._note_started) * 1000
        if (self._cur_note or self._buffer) and time_playing >= self._duration:
            if self._buffer and not (self.note_gap and self._cur_note):
                self._cur_note = self._buffer.pop(0)
                if self._cur_note.frequency:
                    self._pwm.ChangeFrequency(self._cur_note.frequency)
                    self._pwm.start(self.dc)
                else:
                    self._pwm.stop()
                self._duration = self._cur_note.duration
            else:
                self._pwm.stop()
                self._cur_note = None
                self._duration = self.note_gap
            self._note_started = time.perf_counter()
