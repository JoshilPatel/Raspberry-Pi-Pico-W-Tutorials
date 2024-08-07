from machine import Pin
from time import sleep

buttonPin=14
#Creating my button object, setting it to an input and acitivating pull up resistor
myButton=Pin(buttonPin,Pin.IN,Pin.PULL_UP)

LEDPin=15
redLED=Pin(LEDPin,Pin.OUT)
LEDState=0

buttonValOld=1

while True:
    buttonValNew=myButton.value()
    #When I let go of the button I want it to switch...old value has to be 0 and the new value 1.
    if (buttonValOld==1 and buttonValNew==0):
        if (LEDState==0):
            redLED.value(1)
            LEDState=1
        else:
            redLED.value(0)
            LEDState=0
    
    buttonValOld=buttonValNew
    sleep(.1)
    
    
    

    
    

