# Tutaj pisz swój kod, młody padawanie ;-)
from machine import Pin
from time import sleep
from umqtt.robust import MQTTClient


def do_connect(ssid, password):
    import network

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("connecting to network...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print("network config:", wlan.ifconfig())


x = False
y = True

def on_message(topic, message):
    global x, y
    print('Message "{}" received in topic "{}"'.format(message, topic))
    if topic == b'best/reset':
        print('reset')
        x = False
    if topic == b'best/set':
        print('set')
        y = not y
        client.publish("best/state", str(y))

do_connect("best.in.iot", "Secret.Password")

sensor = Pin(35, Pin.IN)
led = Pin(32, Pin.OUT)
speaker = Pin(33, Pin.OUT)

client = MQTTClient("alarm-system", "mqtt.kpi.fei.tuke.sk", 80)
client.set_callback(on_message)
client.connect()
client.subscribe("best/reset")
client.subscribe("best/set")



while True:
    client.check_msg()
    input = sensor.value()
    if y == True:
        if input == 1:
            if x == False:
                client.publish("best/alarm", "on")
                x = True
        if x is True:
            led.on()
            for i in range(1, 50):
                speaker.on()
                sleep(0.005)
                speaker.off()
                sleep(0.005)
            for j in range(1, 50):
                speaker.on()
                sleep(0.003)
                speaker.off()
                sleep(0.003)
            for j in range(1, 50):
                speaker.on()
                sleep(0.001)
                speaker.off()
                sleep(0.001)
        else:
            led.off()
            speaker.off()
        sleep(0.5)
