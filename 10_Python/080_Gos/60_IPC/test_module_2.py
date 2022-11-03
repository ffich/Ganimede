from machine import Pin
import g_os
from Ipc import *

# Create LED
LED = Pin(16, Pin.OUT)

def Task2Callback():
    if ToggleLed.get_evt():
        LED.value(not LED.value())
        
# Create Task
Task2 = g_os.task("Task2", 10, Task2Callback)    