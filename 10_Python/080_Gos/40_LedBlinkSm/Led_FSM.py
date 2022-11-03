from g_fsm import StateMachine
from time import sleep_ms
from machine import Pin
import g_os

TASK_PERIOD_MS = 1

LED_ON_MS = 10
LED_OFF_MS = 990

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
        if counter <= (LED_ON_MS/TASK_PERIOD_MS): # Led on for LED_ON_MS
            counter += 1
        else:
            BlinkSts = BLINK_LONG
            counter = 0
    else:
        if counter <= (LED_OFF_MS/TASK_PERIOD_MS): # Led off for LED_OFF_MS
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
led_sm.start_fsm(WaitSt)

# Create a stask for the FSM
def T1Cbk():
    led_sm.run_fsm()
    
# Create Tasks @ TASK_PERIOD_MS (10 ms)
T1 = g_os.task("Task1", TASK_PERIOD_MS, T1Cbk)

# Create the scheduler
mySched = g_os.sch()

# Add tasks to the scheduler queue
mySched.add_task(T1)

# Start the scheduler
mySched.start()

    
    
    