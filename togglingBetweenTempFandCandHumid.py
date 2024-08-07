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
toggle=0

while True:
    buttonValNew=toggleButton.value()
    
    if (buttonValOld==0 and buttonValNew==1):
        toggle=toggle+1
        if (toggle==3):
            toggle=0
    
    sensor.measure()
    tempC=sensor.temperature()
    tempF=tempC*(9/5)+32
    humidity=sensor.humidity()
    
    if toggle==0:
        print('\r','Temperature:',float(tempC),chr(176)+'C',end='')
        
    if toggle==1:
        print('\r','Temperature:',tempF,chr(176)+'F',end='     ')
    
    if toggle==2:
        print('\r','Humidity:',humidity,'%', end='         ')
    
    time.sleep(.25)
    buttonValOld=buttonValNew