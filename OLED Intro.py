import machine
#from machine import Pin, SoftI2C
import ssd1306
from time import sleep

i2c = machine.SoftI2C(scl=machine.Pin(15), sda=machine.Pin(14))

pin = machine.Pin(16, machine.Pin.OUT)
pin.value(0) #set GPIO16 low to reset OLED
pin.value(1) #while OLED is running, must set GPIO16 in high

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello world', 0, 0)
oled.text('welcome', 0, 16)

#Turning on a specific pixel
oled.pixel(64,32,0)

#Horizontal line. column 20, row 20 and 40 pixels long and turned on
oled.hline(20,40,40,1)

#Vertical line
oled.vline(20,40,20,1)

#Line between pixels (diagonal to  pixel 118,54)
oled.line(20,20,118,54,1)

#Rectangle
oled.rect(64,32,30,20,1)

#Solid filled rectangle
oled.fill_rect(70,40,15,10,1)

#Make the colours switch around (coloured background)
#oled.invert(1)

#Make the colours switch around (black background)
#oled.invert(0)

oled.show()
#sleep(5)
#Does not loose the image when you power off
#oled.poweroff()