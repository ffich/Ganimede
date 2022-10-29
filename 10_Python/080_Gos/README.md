## G-OS
This section shows the usage of G-OS (Ganimede OS). G-OS is a simple object oriented cooperative multitasking library, that allows to schedule periodic tasks on Ganimede (and more in general to all micropython targets) and provides some feature for virtual timing (possibility to create virtual timers) and IPC (inter-task event mechanims) as well. G-OS is simple, but powerful, especially in conjunction with G-FSM, an object oriented implementation of state machine approach using micropython. 

## G-OS Usage
G-OS usage is very simple. You first create you task implementation in form of a callback (micripython function). Then you create the task object (constructor task()) and pass 3 parameters:
- Task name (string)
- Task period in ms (integrer)
- Task callback (the previously created one)

After this you create a scheduler (contructor sch()) and then add the task to the scheduler using the add_task() method. After this you can start the scheduler with the start() method and your task will be dispateched at the defined period. More than one scheduler can be created, but only one scheduler at time can run, so if you create two scheduler the first one started will hold the CPU until it's stopped. Then another scheduler can be ran. This is useful if you want to create more execution modes (e.g. a "normal" mode and a "low power" or "emergency" mode, which execute a different set of tasks).

For example, the following code will run the task myTask at 1s rate:

```
import g_os

def myTaskCbk():
  print("I'm a Task and I run at 1000ms")

myTask = g_os.task("MyTask", 1000, myTaskCbk)
mySched = g_os.sch()
mySched.add_task(myTask)
mySched.start()
```

Remember that the scheduler if fully cooperative, so any blocking function (e.g. sleep()) will prevent other task to be executed. Anyway, as far as you don't use blocking functions inside your task code, all the task will receive some execution time when they are dispateched. If you use G-FSM to implement your code you're pretty sure that all you code is executed as far as the scheduling problem is schedulable (ther is enoug execution time for all the tasks - no starvation).

## G-FSM
G-FSM (Ganimede FSM) is an object oriented library for creating state machines with micropython. Differently from languages like C, Python doesn't have a built in switch...case statement, which makes the implementation of a state machine a bit more annoing as it should be a sequence of if...elif statements. But this is not the only way, you can think about implementing object oriented state machines. G-FSM does exactly this, by providing a class and related methods for creating FSM objects.

## G-FSM Usage
G-FSM is very simple. First you create an instance of the FSM object, using the StateMachine() constructor. Then you define a set of callbacks implementing each state function (a regular Python function). Then you use the add_state method to add states. The state list is a Python dictionary that associates state names (strings) to state callback (the previously defined functions). Once you have added all the states, you need to use the start_fsm() method to start the state machine. This method requires the start state (state name) and - optionally - the stop state. If the stop state is defined, once it's reached, the state machine stops executing. In that case a restart_fsm() method is provided to restart the FSM.

Each state callback has to return the next state to run (in form of the State name). It could be any of the FSM state, including the state owning the callback. The only important thing is that it's returned a state present in the FSM instance dictionary, otherwise G-FSM will thrown an exception.

The example below creates a state machine that endlessy jumps between two states (STATE_A and STATE_B).

```
import g_fsm
import g_os

mySm = g_fsm.StateMachine()

def StateA ():
  print("I'm State A")
  return "STATE_B"
  
def StateB ():
  print("I'm State B")
  return "STATE_A"
  
mySm.add_state("STATE_A", StateA)
mySm.add_state("STATE_B", StateB)
mySm.start_fsm("STATE_A")

def myTaskCbk():
  mySm.run_fsm()

myTask = g_os.task("MyTask", 1000, myTaskCbk)
mySched = g_os.sch()
mySched.add_task(myTask)
mySched.start()
```

## Additional comments
All the examples on this section require to have g_os.py and g_fsm.py saved inside the device file system. You will find these two files in 00_Lib.

