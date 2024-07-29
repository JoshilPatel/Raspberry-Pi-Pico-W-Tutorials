"""while True:
    myInput=float(input('Input your number: '))
    if myInput==5:
        print('Your number is 5!')
    if myInput>5:
        print('Your number is greater than 5!')
    if myInput<5:
        print('Your number is less than 5!')"""

from machine import Pin
import time

led=Pin(15,Pin.OUT)

while True:
    CMD=input("Do you want to turn the LED on or off?: ")
    if CMD=='on':
        led.value(1)
    if CMD=='off':
        led.value(0)
    if CMD=='toggle':
        led.toggle()
            
    
    