#Library is machine and the method being imported in Pin
from machine import Pin

#From time import the method sleep
from time import sleep

#Creating LED object, the pin we want to interact with is called 'LED'
myLED=Pin('LED',Pin.OUT)

while True:
    myLED.value(1) #1 is on and 0 is off, but you could also do myLED.on
    sleep(.05) #Wait one second
    myLED.value(0)
    sleep(.05)