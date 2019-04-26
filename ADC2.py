import RPi.GPIO as GPIO
import smbus
import time

class adc():
    def __init__( self, bus, pin, dac ):
        self.I2C_DATA_ADDR   = 0x38	
        self.I2C_ENABLE_ADDR = 0x39	
        self.DAC_EN = [0xBF, 0x7F]

        self.bus = bus
        self.dac = dac

        try:class adc():
    def __init__( self, bus, pin, dac ):
        self.I2C_DATA_ADDR   = 0x38	
        self.I2C_ENABLE_ADDR = 0x39	
        self.DAC_EN = [0xBF, 0x7F]

        self.bus = bus
        self.dac = dac

        try:
            self.bus.write_byte( self.I2C_DATA_ADDR, 0 )    	# clear port
        except IOError:
            print("clock: I2C comms error")

        try:
            self.bus.write_byte( self.I2C_ENABLE_ADDR, 255 )    # clear port
        except IOError:
            print("clock: I2C comms error")

        self.COMP_PIN = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(self.COMP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def update( self, value ):
        try:
            self.bus.write_byte( self.I2C_DATA_ADDR, value )    	  
            self.bus.write_byte( self.I2C_ENABLE_ADDR, self.DAC_EN[self.dac] )  
            #time.sleep(0.001)
            self.bus.write_byte( self.I2C_ENABLE_ADDR, 255 ) 
        except IOError:
            print("clock: I2C comms error")

    def getComp( self ):
        return GPIO.input( self.COMP_PIN )

    def ramp( self ):
        count = 0   
        self.update( 0 ) 
        for i in range(0,255):
            if self.getComp() == False:              
                count = count + 1
                self.update( i ) 
            else:
                break

        return count

    def approx( self ):
        count = 0   
        new = 0
        self.update( 0 ) 
        for i in range(0, 8):
            new = count | 2**(7-i)
	    #print i, count, new

            self.update( new )
            if self.getComp() == False:
                count = new

        return count

		
# Main program block

def main():
    print "main start"
   
    bus = smbus.SMBus(1)
    adc1 = adc( bus, 25, 1 )

    while True:    
        #value = adc1.ramp()
        value = adc1.approx()
        if value > 160:
            print value

        time.sleep( 0.001 )
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        pass
            self.bus.write_byte( self.I2C_DATA_ADDR, 0 )    	# clear port
        except IOError:
            print("clock: I2C comms error")

        try:
            self.bus.write_byte( self.I2C_ENABLE_ADDR, 255 )    # clear port
        except IOError:
            print("clock: I2C comms error")

        self.COMP_PIN = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(self.COMP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def update( self, value ):
        try:
            self.bus.write_byte( self.I2C_DATA_ADDR, value )    	  
            selfclass adc():
    def __init__( self, bus, pin, dac ):
        self.I2C_DATA_ADDR   = 0x38	
        self.I2C_ENABLE_ADDR = 0x39	
        self.DAC_EN = [0xBF, 0x7F]

        self.bus = bus
        self.dac = dac

        try:
            self.bus.write_byte( self.I2C_DATA_ADDR, 0 )    	# clear port
        except IOError:
            print("clock: I2C comms error")

        try:
            self.bus.write_byte( self.I2C_ENABLE_ADDR, 255 )    # clear port
        except IOError:
            print("clock: I2C comms error")

        self.COMP_PIN = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(self.COMP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def update( self, value ):
        try:
            self.bus.write_byte( self.I2C_DATA_ADDR, value )    	  
            self.bus.write_byte( self.I2C_ENABLE_ADDR, self.DAC_EN[self.dac] )  
            #time.sleep(0.001)
            self.bus.write_byte( self.I2C_ENABLE_ADDR, 255 ) 
        except IOError:
            print("clock: I2C comms error")

    def getComp( self ):
        return GPIO.input( self.COMP_PIN )

    def ramp( self ):
        count = 0   
        self.update( 0 ) 
        for i in range(0,255):
            if self.getComp() == False:              
                count = count + 1
                self.update( i ) 
            else:
                break

        return count

    def approx( self ):
        count = 0   
        new = 0
        self.update( 0 ) 
        for i in range(0, 8):
            new = count | 2**(7-i)
	    #print i, count, new

            self.update( new )
            if self.getComp() == False:
                count = new

        return count

		
# Main program block

def main():
    print "main start"
   
    bus = smbus.SMBus(1)
    adc1 = adc( bus, 25, 1 )

    while True:    
        #value = adc1.ramp()
        value = adc1.approx()
        if value > 160:
            print value

        time.sleep( 0.001 )
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        pass.bus.write_byte( self.I2C_ENABLE_ADDR, self.DAC_EN[self.dac] )  
            #time.sleep(0.001)
            self.bus.write_byte( self.I2C_ENABLE_ADDR, 255 ) 
        except IOError:
            print("clock: I2C comms error")

    def getComp( self ):
        return GPIO.input( self.COMP_PIN )

    def ramp( self ):
        count = 0   
        self.update( 0 ) 
        for i in range(0,255):
            if self.getComp() == False:              
                count = count + 1
                self.update( i ) 
            else:
                break

        return count

    def approx( self ):
        count = 0   
        new = 0
        self.update( 0 ) 
        for i in range(0, 8):
            new = count | 2**(7-i)
	    #print i, count, new

            self.update( new )
            if self.getComp() == False:
                count = new

        return count

		
# Main program block

def main():
    print "main start"
   
    bus = smbus.SMBus(1)
    adc1 = adc( bus, 25, 1 )

    while True:    
        #value = adc1.ramp()
        value = adc1.approx()
        if value > 160:
            print value

        time.sleep( 0.001 )
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        pass
