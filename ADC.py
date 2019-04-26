import smbus
import time 

I2CADDR = 0x21
CMD_CODE = 0x10
for i in range(0,100):
    bus = smbus.SMBus(1)
    bus.write_byte( I2CADDR, CMD_CODE ) 
    tmp = bus.read_word_data( I2CADDR, 0x00)
    tmp = (((tmp << 8) & 0x00FFFF) | (tmp >> 8)) & 0x0FFF
    #print("{:04x}".format(tmp))
    print(tmp)
#get rid of first 4 bits
    tmp = tmp & 0000111111111111
    print(tmp)
    time.sleep(1)
    	


