from machine import PWM,Pin
from time import sleep

redPin=15
greenPin=14
bluePin=13

redLED=PWM(Pin(redPin))
greenLED=PWM(Pin(greenPin))
blueLED=PWM(Pin(bluePin))

redLED.freq(1000)
redLED.duty_u16(0) #Off to begin with

greenLED.freq(1000)
greenLED.duty_u16(0) ##Off to begin with

blueLED.freq(1000)
blueLED.duty_u16(0)

while True:
    redBrightness=65550
    greenBrightness=65550
    blueBrightness=0
    
    redLED.duty_u16(redBrightness)
    greenLED.duty_u16(greenBrightness)
    blueLED.duty_u16(blueBrightness)
    sleep(.1)
    
    
    
