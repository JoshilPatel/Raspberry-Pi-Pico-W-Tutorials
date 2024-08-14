import socket
#Address of the raspbery pi pico w
serverAddress=('192.168.0.126',2222)
bufferSize=1024
#Setting up the client
UDPClient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    cmd=input('Which colour do you want the LED to be?: ')
    #Encode the command
    cmdEncoded=cmd.encode('utf-8')
    #Send command to the server
    UDPClient.sendto(cmdEncoded,serverAddress)
    
    #Waiting for received confirmation from server
    data,address=UDPClient.recvfrom(bufferSize)
    dataDecoded=data.decode('utf-8')
    print('MESSAGE FROM SERVER:',dataDecoded)