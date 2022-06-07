from machine import Pin
import time

Led = Pin(16, Pin.OUT)

while (True):
    Led.value(1)
    time.sleep(1)
    Led.value(0)
    time.sleep(1)    