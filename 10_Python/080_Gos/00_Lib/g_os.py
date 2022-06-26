# G-OS: Ganimede OS
# Simple cooperative os library with virtual timing and IPC features.
# Written by: Francesco Ficili

import time

# Constants Values

# Status
STOPPED = 0
RUNNING = 1

# Timer status
TIMER_CANCELED = 0
TIMER_ACTIVE = 1

# Events
EVT_CLEAR = 0
EVT_SET = 1

# Tasks
class task:
    def __init__ (self, ID, Period_ms, task_cbk):
        self.Period = Period_ms
        self.TaskSts = RUNNING
        self.tCbk = task_cbk
        self.Id = ID
         
    def set_task_period (self, Period_ms):
        self.Period = Period_ms        
        
    def start_task (self):
        self.TaskSts = RUNNING
    
    def stop_task (self):
        self.TaskSts = STOPPED        
                
    def task_body (self):
        start = time.ticks_ms()
        
        while True:
            if self.TaskSts is RUNNING:                
                if time.ticks_ms() - start >= self.Period:
                    start = time.ticks_ms()          
                    self.tCbk()
                yield None
            else:
                yield None      

# Scheduler
class sch:
    def __init__ (self):
        self.TaskList = list()
        self.TaskQueue = list()
        self.SchedSts = RUNNING
        self.Alarms = list()
                           
    def add_task (self, Task):
        self.TaskQueue.append(Task.task_body())        
        self.TaskList.append(Task)
        
    def remove_task (self, Task):        
        self.TaskQueue.pop(self.TaskList.index(Task))
        self.TaskList.pop(self.TaskList.index(Task))
        
    def print_task_list (self):
        for task in self.TaskList:
            print(task.Id)

    def start (self):
        print("Starting scheduler...")
        while self.SchedSts is RUNNING:
            for task in self.TaskQueue:
               next(task)
               
    def stop (self):
        print("Canceling scheduler... ")
        self.TaskQueue.clear()
        self.SchedSts = STOPPED

# Virtual Timers
class vTimer:
    def __init__ (self):
        pass
              
    def start_timer (self, Timeout_ms):
        self.Timeout = Timeout_ms
        self.start = time.ticks_ms()
        self.TimerSts = TIMER_ACTIVE
        
    def cancel_timer (self):
        self.TimerSts = TIMER_CANCELED
        
    def is_expired (self):
        if self.TimerSts is TIMER_ACTIVE:
            if time.ticks_ms() - self.start >= self.Timeout:
                return True
            else:
                return False

# IPC - Events
class event:
    def __init__ (self):
        self.Evt = EVT_CLEAR
    
    def set_evt (self):
        self.Evt = EVT_SET
        
    def get_evt (self):
        if self.Evt is EVT_SET:
            self.Evt = EVT_CLEAR
            return True
        else:
            return False