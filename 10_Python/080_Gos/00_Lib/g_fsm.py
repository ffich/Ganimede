# G-FSM: Ganimede FSM
# Simple object oriented FSM library for Ganimede Board
# Written by: Francesco Ficili

class StateMachine:
    def __init__(self):
        self.handlers = dict()
        self.state = None
        self.nextState = None
        self.endState = None
        self.running = False
        
    def add_state(self, name, handler):
        self.handlers[name] = handler
        
    def start_fsm(self, startState, endState = "NO_ENDING_STATE"):
        self.state = startState
        self.startState = startState
        self.endState = endState
        self.running = True
        
    def restart_fsm(self):
        self.state = self.startState
        self.running = True
        
    def run_fsm (self):
        if self.running is True:
            try:
                if self.state is self.endState:
                    self.running = False
                    self.handlers[self.state]()                    
                else:
                    self.nextState = self.handlers[self.state]()
                    self.state = self.nextState                
            except:
                print("Invalid state - Something went wrong, check the fsm handlers or the FSM states")
                while True:
                    pass
        
