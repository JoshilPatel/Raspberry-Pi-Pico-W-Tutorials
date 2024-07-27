from machine import Pin
from time import sleep

aLED=Pin(15,Pin.OUT)
bLED=Pin(12,Pin.OUT)
cLED=Pin(13,Pin.OUT)
dLED=Pin(6,Pin.OUT)

while True:
    aLED.value(0)
    bLED.value(0)
    cLED.value(0)
    dLED.value(0)
    
    sleep(0.5)
    
    aLED.value(1)
    bLED.value(0)
    cLED.value(0)
    dLED.value(0)

    sleep(0.5)
    
    aLED.value(0)
    bLED.value(1)
    cLED.value(0)
    dLED.value(0)

    sleep(0.5)
    
    aLED.value(1)
    bLED.value(1)
    cLED.value(0)
    dLED.value(0)

    sleep(0.5)

    aLED.value(0)
    bLED.value(0)
    cLED.value(1)
    dLED.value(0)
    
    sleep(0.5)
    
    aLED.value(1)
    bLED.value(0)
    cLED.value(1)
    dLED.value(0)

    sleep(0.5)
    
    aLED.value(0)
    bLED.value(1)
    cLED.value(1)
    dLED.value(0)
    
    sleep(0.5)
    
    aLED.value(1)
    bLED.value(1)
    cLED.value(1)
    dLED.value(0)
    
    sleep(0.5)

    aLED.value(0)
    bLED.value(0)
    cLED.value(0)
    dLED.value(1)

    sleep(0.5)
    
    aLED.value(1)
    bLED.value(0)
    cLED.value(0)
    dLED.value(1)
    
    sleep(0.5)
    
    aLED.value(0)
    bLED.value(1)
    cLED.value(0)
    dLED.value(1)
    
    sleep(0.5)
    
    aLED.value(1)
    bLED.value(1)
    cLED.value(0)
    dLED.value(1)
    
    sleep(0.5)

    aLED.value(0)
    bLED.value(0)
    cLED.value(1)
    dLED.value(1)
    
    sleep(0.5)
    
    aLED.value(1)
    bLED.value(0)
    cLED.value(1)
    dLED.value(1)
    
    sleep(0.5)
    
    aLED.value(0)
    bLED.value(1)
    cLED.value(1)
    dLED.value(1)
    
    sleep(0.5)
    
    aLED.value(1)
    bLED.value(1)
    cLED.value(1)
    dLED.value(1)
    
    sleep(0.5)

    