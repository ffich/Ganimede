from machine import Pin
import g_os

# Create LED
LED = Pin(16, Pin.OUT)

def MyCallback():
    LED.value(not LED.value())
    
# Create Tasks
MyTask = g_os.task("Task1", 1000, MyCallback)    