import time
from machine import Pin

Led1 = Pin(2, Pin.OUT)
Led2 = Pin(16, Pin.OUT)

def TaskOne(Period_ms):
    start = time.ticks_ms()
    
    while True:
        if time.ticks_ms() - start >= Period_ms:
            start = time.ticks_ms()
            # Task code here            
            Led1.value(not Led1.value())
            # end Task    
        yield None

def TaskTwo(Period_ms):
    start = time.ticks_ms()
    
    while True:
        if time.ticks_ms() - start >= Period_ms:
            start = time.ticks_ms()
            # Task code here            
            Led2.value(not Led2.value())
            # end Task          
        yield None

TaskQueue = [TaskOne(1000), TaskTwo(250)]

while True:
    for task in TaskQueue:
        next(task)