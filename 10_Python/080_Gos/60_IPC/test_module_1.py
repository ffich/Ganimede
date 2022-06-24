from machine import Pin
import g_os
from Ipc import *

def Task1Callback():
    ToggleLed.set_evt()
    
# Create Task
Task1 = g_os.task("Task1", 1000, Task1Callback)    