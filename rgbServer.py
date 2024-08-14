#When we communicate over Wi-Fi /Ethernet in python we talk over a socket. Client and server connect over socket
import socket
import time
import network

import machine
from machine import PWM,Pin
import ssd1306

time.sleep(5)

#RGB LED SETUP
redPin=13
greenPin=12
bluePin=11

redLED=PWM(Pin(redPin))
greenLED=PWM(Pin(greenPin))
blueLED=PWM(Pin(bluePin))

redLED.freq(1000)
redLED.duty_u16(0) #Off to begin with

greenLED.freq(1000)
greenLED.duty_u16(0) ##Off to begin with

blueLED.freq(1000)
blueLED.duty_u16(0)


#OLED DISPLAY SETUP

i2c = machine.SoftI2C(scl=machine.Pin(15), sda=machine.Pin(14))

pin = machine.Pin(16, machine.Pin.OUT)
pin.value(0) #set GPIO16 low to reset OLED
pin.value(1) #while OLED is running, must set GPIO16 in high

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


#WIFI SETUP

#Creating a wi-fi network with this command
wifi=network.WLAN(network.STA_IF)
#Activating wifi network
wifi.active(True)

#Telling wifi object to connect to wifi network
wifi.connect('SKYTNSH7','AdSV8hu1reAb')

while wifi.isconnected()==False:
    print('Waiting for connection...')
    time.sleep(1)
    
#Requesting IP address from server
wifiInfo=wifi.ifconfig()

#The first IP address printed is the IP address of the server
print(wifiInfo)

#The IP address we want is the first one in the wifiInfo array
ServerIP=wifiInfo[0]
oledMessage1='IP: '+ServerIP


#Need to agree on a port for that IP address to talk on
ServerPort=2222
oledMessage2='Port: '+ str(ServerPort)


#How big of a packet we are sending back and fourth (1024 bytes)
bufferSize=1024
#Need to create a socket with UDP protocol which will talk over
UDPServer=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#Need to connect UDP server with specific IP address
UDPServer.bind((ServerIP,ServerPort))
print('UDP Server Up and Waiting...')

#The server has now been created, it now needs to wait for someone to request something
while True:
    oled.text(oledMessage1,0,0)
    oled.text(oledMessage2,0,16)

    message,address=UDPServer.recvfrom(bufferSize) #The message is what it is asking for and the address is who is asking
    messageDecoded=message.decode('utf-8') #utf-8 format
    print('MESSAGED RECEIVED:',messageDecoded,'FROM:',address[0])
    
    oled.text('MESSAGE RECEIVED',0,32)
    oled.text(messageDecoded,0,40)
    oled.text('FROM:',0,50)
    oled.text(SererIP)
    oled.show()
    
    if messageDecoded=='red':
        redLED.duty_u16(65550)
        greenLED.duty_u16(0)
        blueLED.duty_u16(0)
        
    if messageDecoded=='green':
        redLED.duty_u16(0)
        greenLED.duty_u16(65550)
        blueLED.duty_u16(0)

    if messageDecoded=='orange':
        redLED.duty_u16(65550)
        greenLED.duty_u16(32775)
        blueLED.duty_u16(0)
    
    if messageDecoded=='cyan':
        redLED.duty_u16(0)
        greenLED.duty_u16(65550)
        blueLED.duty_u16(65550)

    if messageDecoded=='magenta':
        redLED.duty_u16(65550)
        greenLED.duty_u16(15720)
        blueLED.duty_u16(47160)

    if messageDecoded=='yellow':
        redLED.duty_u16(65550)
        greenLED.duty_u16(65550)
        blueLED.duty_u16(0)

    if messageDecoded=='off':
        redLED.duty_u16(0)
        greenLED.duty_u16(0)
        blueLED.duty_u16(0)
    
    
    #Sending back confirmation to the client
    dataString='Received  your command: '+messageDecoded
    dataStringEncoded=dataString.encode('utf-8')
    UDPServer.sendto(dataStringEncoded,address)
    
    