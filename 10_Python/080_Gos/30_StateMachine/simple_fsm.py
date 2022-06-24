import fsm
from time import sleep

myVar = 0

sm = fsm.StateMachine()

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

while True:
    sm.run_fsm()
    sleep(1)
    
