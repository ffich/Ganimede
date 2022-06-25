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
    Led1.value(not Led1.value())
    print("I'm the " + str(T1.Id) + ", and I'm running at " + str(T1.Period) + " ms")    
      
def T2Cbk():
    Led2.value(not Led2.value())
    print("I'm the " + str(T2.Id) + ", and I'm running at " + str(T2.Period) + " ms")       
    
def T3Cbk():
    print("I'm the " + str(T3.Id) + ", and I'm running at " + str(T3.Period) + " ms")

def T4Cbk():
    print("I'm the " + str(T4.Id) + ", and I'm running at " + str(T4.Period) + " ms")

# Create Tasks
T1 = g_os.task("Task1", 1000, T1Cbk)
T2 = g_os.task("Task2", 500, T2Cbk)   
T3 = g_os.task("Task3", 2000, T3Cbk)
T4 = g_os.task("Task4", 4000, T4Cbk)   

# Create the scheduler
mySched = g_os.sch()

# Add tasks to the scheduler queue
mySched.add_task(T1)
mySched.add_task(T2)
mySched.add_task(T3)
mySched.add_task(T4)

# Start the scheduler
mySched.start()


