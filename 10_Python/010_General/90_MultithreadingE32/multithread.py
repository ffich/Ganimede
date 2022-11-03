# This example only works on Ganimede.E32

import _thread
import time

count = 0
 
def T1(p):
  while True:
    time.sleep(p)      
    print("I'm a Thread and I run at " + str(p) + " seconds")

def T2(p):
  while True:
    time.sleep(p)      
    print("I'm a Thread and I run at " + str(p) + " seconds")

def T3(p):
  while True:
    time.sleep(p)      
    print("I'm a Thread and I run at " + str(p) + " seconds")
    
def T4(p):
  while True:
    time.sleep(p)        
    print("I'm a Thread and I run at " + str(p) + " seconds")

_thread.start_new_thread(T1, (2,))
_thread.start_new_thread(T2, (5,))
_thread.start_new_thread(T3, (10,))
_thread.start_new_thread(T4, (4,))

while (True):
    # Main loop
    count += count