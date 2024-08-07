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
    choice=input("What colour do you want the LED to light? (red,green,blue,orange,cyan,magenta,yellow): ")
    
    if choice=='red':
        redLED.duty_u16(65550)
        greenLED.duty_u16(0)
        blueLED.duty_u16(0)
            
    if choice=='green':
        redLED.duty_u16(0)
        greenLED.duty_u16(65550)
        blueLED.duty_u16(0)
    
    if choice=='red':
        redLED.duty_u16(65550)
        greenLED.duty_u16(0)
        blueLED.duty_u16(0)
        
    if choice=='orange':
        redLED.duty_u16(65550)
        greenLED.duty_u16(32775)
        blueLED.duty_u16(0)

    if choice=='cyan':
        redLED.duty_u16(0)
        greenLED.duty_u16(65550)
        blueLED.duty_u16(65550)
    
    if choice=='magenta':
        redLED.duty_u16(65550)
        greenLED.duty_u16(15720)
        blueLED.duty_u16(47160)
        
    if choice=='yellow':
        redLED.duty_u16(65550)
        greenLED.duty_u16(65550)
        blueLED.duty_u16(0)   
        
    
    
    