import machine
#from machine import Pin, SoftI2C
import ssd1306
from time import sleep
import math

i2c = machine.SoftI2C(scl=machine.Pin(15), sda=machine.Pin(14))

pin = machine.Pin(16, machine.Pin.OUT)
pin.value(0) #set GPIO16 low to reset OLED
pin.value(1) #while OLED is running, must set GPIO16 in high

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

r=35
xCentre=64
yCentre=40
phase=0

while True:
    for degree in range(0,360,1):
        rads=degree*(3.14/180)
        x=r*math.cos(2*rads+phase)+xCentre
        y=.65*r*math.sin(3*rads)+yCentre
        oled.pixel(int(x),int(y),1)
    oled.show()
    #Clear display
    oled.fill(0)
    #Keep adding one radian (degree conversion included)
    phase=phase+1*(3.14/180)