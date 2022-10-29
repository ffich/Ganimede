from machine import Pin
import time

Led = Pin(16, Pin.OUT)
SLEEP_S = 1

while (True):
    Led.on()
    time.sleep(SLEEP_S)
    Led.off()
    time.sleep(SLEEP_S)    