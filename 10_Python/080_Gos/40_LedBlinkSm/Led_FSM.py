from fsm import StateMachine
from time import sleep_ms
from machine import Pin
import g_os

# Led object
LED = Pin(16, Pin.OUT)

# StateMachine object
led_sm = StateMachine()

# Constants
BLINK_SHORT = 0
BLINK_LONG = 1

BlinkSts = BLINK_SHORT

# States
WaitSt = "WAIT"
BlinkSt = "BLINK"

# Globals
counter = 0

def WaitState():
    global BlinkSts
    global counter 
    
    if BlinkSts is BLINK_SHORT:
        if counter <= 2: # Blink at 20ms
            counter += 1
        else:
            BlinkSts = BLINK_LONG
            counter = 0
    else:
        if counter <= 50: # LED off for 0.5 seconds
            counter += 1
        else:
            BlinkSts = BLINK_SHORT
            counter = 0
    return BlinkSt
    
def BlinkState():
    global LED
    
    if BlinkSts is BLINK_SHORT:
        LED.on()
    else:
        LED.off()
    return WaitSt

# Initialize the state machine
led_sm.add_state(WaitSt, WaitState)
led_sm.add_state(BlinkSt, BlinkState)
led_sm.start_fsm(WaitSt, "STOP")

# Create a stask for the FSM
def T1Cbk():
    led_sm.run_fsm()
    
# Create Tasks @ 10ms
T1 = g_os.task("Task1", 10, T1Cbk)

# Create the scheduler
mySched = g_os.sch()

# Add tasks to the scheduler queue
mySched.add_task(T1)

# Start the scheduler
mySched.start()

    
    
    