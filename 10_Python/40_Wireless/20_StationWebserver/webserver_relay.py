from machine import Pin, Timer
import network
import time
 
Led = Pin(2, Pin.OUT)
print('starting up...')
Led.on()
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('<SSID_Name>', 'Password')
    while not wlan.isconnected():
        pass
print('network config:', wlan.ifconfig())

while (True):
    Led.off()
    time.sleep(0.02)
    Led.on()
    time.sleep(1)   