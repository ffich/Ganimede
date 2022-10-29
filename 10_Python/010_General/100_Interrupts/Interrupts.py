from machine import Pin, Timer
from time import sleep

button = Pin(0, Pin.IN)

def irq_button(pin):
    print("Button Interrupt occurred!!!")
    
def irq_timer():
    print("Timer Interrupt occurred!!!")

button.irq(trigger=Pin.IRQ_RISING, handler=irq_button)
timer = Timer(-1)
timer = Timer(period=1000, mode=Timer.PERIODIC, callback=irq_timer)

while True:
    sleep(1)