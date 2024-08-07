from machine import Pin
import time #microtime
from dht import DHT11

buttonPin=15
toggleButton=Pin(buttonPin,Pin.IN,Pin.PULL_UP)

dataPin=16
myPin=Pin(dataPin,Pin.IN,Pin.PULL_DOWN)
sensor=DHT11(myPin)
print('Sensor data:')

buttonValOld=1
tempUnitC=True

while True:
    buttonValNew=toggleButton.value()
    
    if (buttonValOld==0 and buttonValNew==1):
        tempUnitC = not tempUnitC
    
    sensor.measure()
    tempC=sensor.temperature()
    tempF=tempC*(9/5)+32
    humidity=sensor.humidity()
    
    if tempUnitC==True:
        print('\r','Temperature:',float(tempC),chr(176)+'C','Humidity:',humidity,'%', end='')
    
    if tempUnitC==False:
        print('\r','Temperature:',tempF,chr(176)+'F','Humidity:',humidity,'%', end='')
    
    time.sleep(.25)
    buttonValOld=buttonValNew