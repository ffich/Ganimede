from machine import Pin
import time

Relay1 = Pin(16, Pin.OUT)
Relay2 = Pin(15, Pin.OUT)
Button = Pin(0, Pin.IN, Pin.PULL_UP)

def Relays (val):
    Relay1.value(val)
    Relay2.value(val)

while (True):
    btn = Button.value()
    if btn == 0:
        Relays(1)
        time.sleep(2)
    else:
        Relays(0)

