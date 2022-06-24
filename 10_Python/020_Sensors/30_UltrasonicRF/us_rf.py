import time
from usrf_grove import USRF
from machine import Pin

Sensor = USRF(pin = 5, echo_timeout_us = 1000000)
Relay = Pin(15, Pin.OUT)

while (True):
    time.sleep_ms(5)
    Dist = Sensor.distance_cm()
    if Dist < 10:
        Relay.on()
        time.sleep(2)
    else:
        Relay.off()
    