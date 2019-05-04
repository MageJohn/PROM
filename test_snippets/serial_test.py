from serial import Serial
import time

# open pi serial port, speed 9600 baud
serial_port = Serial("/dev/ttyAMA0", 9600)

# wait for character to be RX. Print ASCII value to pi screen
# TX back RX character to remote terminal. If RX character is
# CR exit loop and close port.
go = True
while go:
    input_byte = serial_port.read()
    print("ASCII Value: {}".format(str(ord(input_string))))
    serial_port.write(input_byte)
    time.sleep(0.1)
    if ord(input_string) == 13:
        go = False

serial_port.close()
