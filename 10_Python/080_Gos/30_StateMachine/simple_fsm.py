import g_fsm
import g_os

myVar = 1

sm = g_fsm.StateMachine()

def State1 ():
    print("Hello World!")
    return "STATE2"

def State2 ():
    global myVar
    
    print("This is...")    
    if myVar:
        myVar = 0
        return "STATE3"        
    else:
        myVar = 1
        return "STATE4"
    
def State3 ():
    print("...a simple state machine (A-branch)")
    return "STOP"

def State4 ():
    print("...a simple state machine (B-branch)")
    return "STOP"

def Stop ():
    print("FSM done...restarting")
    sm.restart_fsm()
    return None

sm.add_state("STATE1", State1)
sm.add_state("STATE2", State2)
sm.add_state("STATE3", State3)
sm.add_state("STATE4", State4)
sm.add_state("STOP", Stop)
sm.start_fsm("STATE1", "STOP")

def myTaskCbk():
  sm.run_fsm()

myTask = g_os.task("MyTask", 1000, myTaskCbk)
mySched = g_os.sch()
mySched.add_task(myTask)
mySched.start()

    
