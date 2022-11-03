from machine import Pin, Signal
import g_os

# Create LEDs
Led1_pin = Pin(16, Pin.OUT)
Led2_pin = Pin(2, Pin.OUT)

Led1 = Signal(Led1_pin, invert=False)
Led2 = Signal(Led2_pin, invert=True)

# Both Leds off
Led1.off()
Led2.off()

# Create Task callbacks 
def T1Cbk():
    if timer2.is_expired():
        print("Timer 2 expired - stop Task1 and restart Task2")
        Led1.off()
        timer2.cancel_timer()
        T1.stop_task()
        T2.start_task()  
    elif timer4.is_expired():
        Led1.off()
        Led2.off()
        print("Timer 4 expired - stop both tasks")
        timer4.cancel_timer()
        T1.stop_task()
        T2.stop_task()
        print("Shutting down scheduler...")
        # Shut scheduler down
        mySched.stop()
    else:    
        Led1.value(not Led1.value())        

def T2Cbk():
    if timer1.is_expired():
        Led2.off()
        print("Timer 1 expired - stop Task2")
        timer1.cancel_timer()
        T2.stop_task()        
    elif timer3.is_expired():
        print("Timer 3 expired - restart Task1 at a faster rate")
        timer3.cancel_timer()
        T1.set_task_period(100)
        T1.start_task()
    else:    
        Led2.value(not Led2.value())

# Create Tasks
T1 = g_os.task("Task1", 1000, T1Cbk)
T2 = g_os.task("Task2", 500, T2Cbk)        

# Create virtual timers
timer1 = g_os.vTimer()
timer1.start_timer(4000)
timer2 = g_os.vTimer()
timer2.start_timer(8000)
timer3 = g_os.vTimer()
timer3.start_timer(12000)
timer4 = g_os.vTimer()
timer4.start_timer(16000)

# Create the scheduler
mySched = g_os.sch()

# Add tasks to the scheduler queue
mySched.add_task(T1)
mySched.add_task(T2)

# Start the scheduler
mySched.start()

