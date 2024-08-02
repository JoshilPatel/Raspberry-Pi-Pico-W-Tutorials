#PWM stands for pulse width modulation
from machine import PWM,Pin
from time import sleep

#Physical pin 21 but GP16
outPin=16
#Creating object
analogOut=PWM(Pin(outPin))
#1000Hz
analogOut.freq(1000)
#Off all the time
analogOut.duty_u16(0)

while True:
    myVoltage=float(input('What voltage would you like? '))
    pwmVal=(65550/3.3)*myVoltage
    analogOut.duty_u16(int(pwmVal))
    sleep(.1)
    