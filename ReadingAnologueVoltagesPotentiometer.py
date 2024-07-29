import machine
from time import sleep

#pot pin is connected to GPIO pin 28
potPin=28
#Creating potentiometer object
myPot=machine.ADC(potPin)

while True:
    potVal=myPot.read_u16() #u16 means we are reading a 16 bit number
    voltage=(3.3/66327)*potVal-(208*3.3/66327)
    print(voltage)
    sleep(.5)