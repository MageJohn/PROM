from serial import Serial

class TextSerial(Serial):
    def read(self, size=1):
        response = super().read(size)
        return response.decode(utf-8)

    def write(self, string):
        return super().write(string.encode('utf-8'))
