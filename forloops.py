#Stops one value before
'''
for i in range(13):
    print(i)'''

#Counts to 10
'''
for i in range(1,11,1):
    print(i)'''

#Counts from 10 to 0 (because it stops before -1)
'''
for i in range(10,-1,-1):
    print(i)'''

#Steps through array
'''
x=[2,31,4,324,43]
for i in x:
    print(i)'''

#Steps through each fruit and each lettre in each fruit
'''
fruits=['apple','orange','banana']
for fruit in fruits:
    print(fruit)
    for lettre in fruit:
        print(lettre)'''

from machine import Pin
import time

redPin=15
redLED=Pin(redPin,Pin.OUT)

while True:
    numBlinks=int(input('How many blinks?: '))
    for i in range(0,numBlinks,1):
        redLED.value(1)
        time.sleep(.5)
        redLED.value(0)
        time.sleep(.5)