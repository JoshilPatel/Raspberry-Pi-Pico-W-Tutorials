from machine import PWM,Pin,ADC
from time import sleep

potPin=26
myPot=machine.ADC(potPin)

LEDPin=16
redLED=PWM(Pin(LEDPin))

redLED.freq(1000)
redLED.duty_u16(0)


while True:
    potVal=myPot.read_u16()
    print(potVal)
    redLED.duty_u16(int(potVal))
    sleep(.5)