import time

def Task1(Period_ms):
    start = time.ticks_ms()
    
    while True:
        if time.ticks_ms() - start >= Period_ms:
            start = time.ticks_ms()
            # Task code here
            print("I'm a Task and I run at " + str(Period_ms) + " ms")
            # end Task    
        yield None

def Task2(Period_ms):
    start = time.ticks_ms()
    
    while True:
        if time.ticks_ms() - start >= Period_ms:
            start = time.ticks_ms()
            # Task code here
            print("I'm a Task and I run at " + str(Period_ms) + " ms")
            # end Task            
        yield None
        
def Task3(Period_ms):
    start = time.ticks_ms()
    
    while True:
        if time.ticks_ms() - start >= Period_ms:
            start = time.ticks_ms()
            # Task code here
            print("I'm a Task and I run at " + str(Period_ms) + " ms")
            # end Task    
        yield None

def Task4(Period_ms):
    start = time.ticks_ms()
    
    while True:
        if time.ticks_ms() - start >= Period_ms:
            start = time.ticks_ms()
            # Task code here
            print("I'm a Task and I run at " + str(Period_ms) + " ms")
            # end Task            
        yield None        

TaskQueue = [Task1(10000), Task2(5000), Task3(4000), Task4(2000)]

while True:
    for task in TaskQueue:
        next(task)