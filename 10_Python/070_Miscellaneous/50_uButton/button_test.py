from ubutton import uButton
import uasyncio as asyncio
import machine
from machine import Pin
import time

Relay1 = Pin(16, Pin.OUT)
Relay2 = Pin(15, Pin.OUT)

Relay1.off()
Relay2.off()

def Rel1():
    global Relay1
    
    Relay1.on()
    time.sleep(2)
    Relay1.off()
    print('short press')

def Rel2():
    global Relay2
    
    Relay2.on()
    time.sleep(2)
    Relay2.off()
    print('long press')
    
# Instantiate the controller instance
button = uButton(
    machine.Pin(0, machine.Pin.IN),
    cb_short = Rel1,
    short_wait=True,
    cb_long = Rel2,
    bounce_time=25,
    long_time=2000,
    act_low=True
)

# Get a reference to the event loop
loop = asyncio.get_event_loop()
# Schedule coroutines to run ASAP
loop.create_task(button.run())
# Run the event loop
loop.run_forever()

