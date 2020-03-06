from umqtt.robust import MQTTClient
from machine import Pin, reset
from time import sleep
import network
import urequests as requests
import json
import sys

button1=Pin(34,Pin.IN)
ledAlarm=Pin(25,Pin.OUT)
ledOn=Pin(33,Pin.OUT)
ledOff=Pin(26,Pin.OUT)
button2=Pin(32,Pin.IN)

urlAlarm = "https://maker.ifttt.com/trigger/motion/with/key/iwncIvHbA08r56HRonCjbeXZzkUJ4GgROuclbADsljg"
urlsong = "https://maker.ifttt.com/trigger/thief!/with/key/iwncIvHbA08r56HRonCjbeXZzkUJ4GgROuclbADsljg"

wlan=network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('best.in.iot','Secret.Password')
    while not wlan.isconnected():
        pass
print('network config: ',wlan.ifconfig())

def on_message(topic, message):
    print('Message "{}" received in topic "{}"'.format(message, topic))
    if topic==b'best/state':
        if message == b"True" :
            ledOn.on()
            ledOff.off()
        else :
            ledOn.off()
            ledOff.on()
    if topic == b'best/alarm' :
        ledAlarm.on()
        sleep(3)

    if topic ==b'best/alarm':
        try:
            r = requests.post(urlAlarm)
            q = requests.post(urlsong)
        except Exception:#catch all exceptions
            print('Exception')
            #reset()
        #e=sys.exc_info()[0]
        #print("<p>Error:%s</p>"%e)
    #results = r.json()
    #print (results)

client = MQTTClient('lights', 'mqtt.kpi.fei.tuke.sk', 80)
client.set_callback(on_message)
client.connect()
client.subscribe('best/alarm')
client.subscribe('best/state')

print("ready")

while True:
    client.check_msg()
    if button1.value()==1:
        print('reset')
        client.publish('best/reset', 'True')
        ledAlarm.off()
        sleep(0.5)
    if button2.value()==1 and ledAlarm.value()==0:
        print('changeStateAlarm')
        client.publish('best/set', 'True')
        sleep(0.5)
    sleep(0.1)
