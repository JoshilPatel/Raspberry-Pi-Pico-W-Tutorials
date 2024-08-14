import network
import time
import urequests #u is for micro, this library allows us to pull the data

wlan=network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SKYTNSH7','AdSV8hu1reAb')

while wlan.isconnected==False:
    print('...Connecting')
print('Your are connected!')
print()
print('Greetings Earthlings! These are the humans in space:')

astronauts=urequests.get('http://api.open-notify.org/astros.json').json()

print()
for person in range(len(astronauts['people'])):
    print (astronauts['people'][person]['name']+' is riding the '+astronauts['people'][person]['craft'])