from collectionts import deque


class MovingAverage:
    def __init__(self, buf_size):
        self.buf = deque(maxlen=buf_size)

    def add_value(self, value):
        self.buf.appendleft(value)

    def get_average(self):
        return round(sum(self.buf) / len(self.buf))
