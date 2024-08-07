from machine import Pin
from time import sleep

redLEDPin=12
greenLEDPin=11
blueLEDPin=10

redLED=Pin(redLEDPin,Pin.OUT)
greenLED=Pin(greenLEDPin,Pin.OUT)
blueLED=Pin(blueLEDPin,Pin.OUT)


redButtonPin=13
greenButtonPin=14
blueButtonPin=15

redButton=Pin(redButtonPin,Pin.IN,Pin.PULL_UP)
greenButton=Pin(greenButtonPin,Pin.IN,Pin.PULL_UP)
blueButton=Pin(blueButtonPin,Pin.IN,Pin.PULL_UP)

redValOld=1
greenValOld=1
blueValOld=1

redLEDState=0
greenLEDState=0
blueLEDState=0

while True:
    #Red
    redValNew=redButton.value()
    if (redValOld==0 and redValNew==1):
        if (redLEDState==0):
            redLED.value(1)
            redLEDState=1
        else:
            redLED.value(0)
            redLEDState=0
    
    redValOld=redValNew
    
    #Green
    greenValNew=greenButton.value()
    if (greenValOld==0 and greenValNew==1):
        if (greenLEDState==0):
            greenLED.value(1)
            greenLEDState=1
        else:
            greenLED.value(0)
            greenLEDState=0
    
    greenValOld=greenValNew
    
    #Blue
    blueValNew=blueButton.value()
    if (blueValOld==0 and blueValNew==1):
        if (blueLEDState==0):
            blueLED.value(1)
            blueLEDState=1
        else:
            blueLED.value(0)
            blueLEDState=0
    
    blueValOld=blueValNew
    
    sleep(.1)


