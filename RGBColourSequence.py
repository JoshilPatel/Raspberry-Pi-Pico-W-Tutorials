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
    colours=[]
    numColours=int(input('How many colours do you want to see?: '))
    for i in range(0,numColours,1):
        colour=input(f'Enter colour {i+1} (red,green,blue,orange,cyan,magenta,yellow,off): ')
        colour=colour.lower()
        colours.append(colour)
    
    for colour in colours:
        if colour=='red':
            redLED.duty_u16(65550)
            greenLED.duty_u16(0)
            blueLED.duty_u16(0)
            
        if colour=='green':
            redLED.duty_u16(0)
            greenLED.duty_u16(65550)
            blueLED.duty_u16(0)
    
        if colour=='red':
            redLED.duty_u16(65550)
            greenLED.duty_u16(0)
            blueLED.duty_u16(0)
        
        if colour=='orange':
            redLED.duty_u16(65550)
            greenLED.duty_u16(32775)
            blueLED.duty_u16(0)

        if colour=='cyan':
            redLED.duty_u16(0)
            greenLED.duty_u16(65550)
            blueLED.duty_u16(65550)
    
        if colour=='magenta':
            redLED.duty_u16(65550)
            greenLED.duty_u16(15720)
            blueLED.duty_u16(47160)
        
        if colour=='yellow':
            redLED.duty_u16(65550)
            greenLED.duty_u16(65550)
            blueLED.duty_u16(0)
            
        if colour=='off':
            redLED.duty_u16(0)
            greenLED.duty_u16(0)
            blueLED.duty_u16(0)
        
        sleep(1)
        redLED.duty_u16(0)
        greenLED.duty_u16(0)
        blueLED.duty_u16(0)

    print('')
        
        
        