from lcd1602 import LCD
import utime as time

lcd=LCD()#No need to specify pins because the library already hard codes certain pins for LCD display

while True:
    myName=input('What is your name? ')
    lcd.clear()
    greeting1='Hello '+myName
    greeting2='Welcome to my Pi'
    lcd.write(0,0,greeting1)#Column 0 row
    lcd.write(0,1,greeting2)#Column 0 row 0