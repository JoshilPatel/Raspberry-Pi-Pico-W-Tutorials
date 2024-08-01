import machine
from machine import Pin
from time import sleep

potPin=27
greenLED=13
yellowLED=14
redLED=15

redLED=Pin(redLED,Pin.OUT)
yellowLED=Pin(yellowLED,Pin.OUT)
greenLED=Pin(greenLED,Pin.OUT)
myPot=machine.ADC(potPin)

while True:
    potVal=myPot.read_u16() #Reading a 16 bit number.
    dangerVal=(100/65327)*potVal-(20800/65327)
    print(dangerVal)
    
    if (dangerVal<=79):
        greenLED.value(1)
        redLED.value(0)
        yellowLED.value(0)
    
    if (dangerVal>=80 and dangerVal<=94):
        greenLED.value(0)
        redLED.value(0)
        yellowLED.value(1)     
    
    if (dangerVal>=95):
        greenLED.value(0)
        redLED.value(1)
        yellowLED.value(0)
        
    sleep(.5)
