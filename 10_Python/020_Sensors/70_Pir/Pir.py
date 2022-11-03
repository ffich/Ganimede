from machine import Pin
import time

Relay = Pin(16, Pin.OUT)
PirSensor = Pin (5, Pin.IN, Pin.PULL_UP)

while (True):
    Pir = PirSensor.value()
    if Pir == 1:
        Relay.value(1)
        time.sleep(2)
    else:
        Relay.value(0)
