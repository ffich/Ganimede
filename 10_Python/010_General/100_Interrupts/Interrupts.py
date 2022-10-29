from machine import Pin, Timer
from time import sleep

button = Pin(0, Pin.IN)

def irq_button(pin):
    print("Button Interrupt occurred!!!")
    
<<<<<<< HEAD
def irq_timer():
=======
def irq_timer(_):
>>>>>>> 7167f27705be46cc1eac1dbe8dc85c7508f8b3e5
    print("Timer Interrupt occurred!!!")

button.irq(trigger=Pin.IRQ_RISING, handler=irq_button)
timer = Timer(-1)
<<<<<<< HEAD
timer = Timer(period=1000, mode=Timer.PERIODIC, callback=irq_timer)
=======
timer.init(period=1000, mode=Timer.PERIODIC, callback=irq_timer)
>>>>>>> 7167f27705be46cc1eac1dbe8dc85c7508f8b3e5

while True:
    sleep(1)