from serial_wrapper import TextSerial

port = TextSerial("/dev/ttyAMA0", 9600)

print("Hello world!", file=port, end='\n\r')
port.close()
