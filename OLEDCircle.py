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

oled.text('My Circle:', 0, 0)

#r=20
xCentre=64
yCentre=40

rStart=4
rStop=25

for r in range(rStart,rStop):
    for degree in range(0,360,1):
        rads=degree*(3.14/180)
        x=r*math.cos(rads)+xCentre
        y=r*math.sin(rads)+yCentre
        oled.pixel(int(x),int(y),1)
    oled.show()