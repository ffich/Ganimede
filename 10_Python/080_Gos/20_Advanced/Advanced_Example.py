from machine import Pin
import machine 
import g_os
import time

# Create LEDs
Led1 = Pin(2, Pin.OUT)
Led2 = Pin(16, Pin.OUT)

def Led1Off ():
    Led1.value(1)

def Led2Off ():
    Led2.value(0)

# Create Task callbacks 
def T1Cbk():
    Led1.value(not Led1.value())
    if timer2.is_expired():
        print("Timer 2 expired - stop Task1 and restart Task2")
        Led1.on()
        timer2.cancel_timer()
        T1.stop_task()
        T2.start_task()
        
    if timer4.is_expired():
        Led1Off()
        print("Timer 4 expired - stop both tasks")
        timer4.cancel_timer()
        T1.stop_task()
        shutdown.set_evt()

def T2Cbk():
    Led2.value(not Led2.value())
    if timer1.is_expired():
        Led2.off()
        print("Timer 1 expired - stop Task2")
        timer1.cancel_timer()
        T2.stop_task()
        
    if timer3.is_expired():
        print("Timer 3 expired - restart Task1 at a faster rate")
        timer3.cancel_timer()
        T1.set_task_period(100)
        T1.start_task()
    
    if shutdown.get_evt():
        Led2Off()
        print("Stopping Task2 using shutdown event")
        T2.stop_task()
        print("Shutting down scheduler...")
        # Shut scheduler down
        mySched.stop()        

# Create Tasks
T1 = g_os.task("Task1", 1000, T1Cbk)
T2 = g_os.task("Task2", 250, T2Cbk)        

# Create virtual timers
timer1 = g_os.vTimer()
timer1.start_timer(2000)
timer2 = g_os.vTimer()
timer2.start_timer(4000)
timer3 = g_os.vTimer()
timer3.start_timer(8000)
timer4 = g_os.vTimer()
timer4.start_timer(10000)

# Create event
shutdown = g_os.event()

# Create the scheduler
mySched = g_os.sch()

# Add tasks to the scheduler queue
mySched.add_task(T1)
mySched.add_task(T2)

# Start the scheduler
mySched.start()

