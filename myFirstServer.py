#When we communicate over Wi-Fi /Ethernet in python we talk over a socket. Client and server connect over socket
import socket
import time
import network

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
#Need to agree on a port for that IP address to talk on
ServerPort=2222
#How big of a packet we are sending back and fourth (1024 bytes)
bufferSize=1024
#Need to create a socket with UDP protocol which will talk over
UDPServer=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#Need to connect UDP server with specific IP address
UDPServer.bind((ServerIP,ServerPort))
print('UDP Server Up and Waiting...')

#The server has now been created, it now needs to wait for someone to request something
while True:
    message,address=UDPServer.recvfrom(bufferSize) #The message is what it is asking for and the address is who is asking
    messageDecoded=message.decode('utf-8') #utf-8 format
    print('MESSAGED RECEIVED:',messageDecoded,'FROM:',address[0])
    #Sending back confirmation to the client
    dataString='Received  your command: '+messageDecoded
    dataStringEncoded=dataString.encode('utf-8')
    UDPServer.sendto(dataStringEncoded,address)