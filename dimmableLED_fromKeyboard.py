from machine import PWM,Pin
from time import sleep

outPin=16
analogOut=PWM(Pin(outPin))

#Fast enough so that you do not see the LED flicker and the voltage remains more steady.
analogOut.freq(1000)

#65550 would be on all the time and 0 is off.
analogOut.duty_u16(0)

while True:
    LEDVoltage=float(input('What voltage would you like to send to the LED? '))
    pwmVal=(65550/3.3)*LEDVoltage
    analogOut.duty_u16(int(pwmVal)) #needs to be an int not a float
    
    
    


