## G-OS
This example shows a basic usgae of G-OS (Ganimede OS). G-OS is a simple object oriented cooperative multitasking library, that allows to schedule periodic tasks on Ganimede and provides some feature for virtual timing (possibility to create virtual timers) and IPC (inter-task event mechanims). G-OS is simple, but powerful, especially in conjunction with g-fsm, an object oriented implementation of state machine approach using micropython. 

## Usage
G-OS usage is very simple. You first create you task implementation in form of a callback (micripython function). Then you create the task object (constructor task()) and pass 3 parameters:
- Task name (string)
- Task period in ms (integrer)
- Task callback (the previously created one)

After this you create a scheduler (contructor sch()) and then add the task to the scheduler using the add_task() method. After this you can start the scheduler with the start() method and your task will be dispateched at the defined period. For example, the following code will run the task myTask at 1s rate:

```
import g_os

def myTaskCbk():
  print("I'm a Task and I run at 1000ms")

myTask = g_os.task("MyTask", 1000, myTaskCbk)
mySched = g_os.sch()
mySched.add_task(myTask)
mySched.start()
```

Remember that the scheduler if fully cooperative, so any blocking function (e.g. sleep()) will prevent other task to be executer. Anyway, as far as you don't use blocking functions inside your task code, all the task will receive some execution time when they are dispateched. If you use g-fsm to implement your code you're pretty sure that all you code is executed as far as the scheduling problem is schedulable (ther is enoug execution time for all the tasks - no starvation).

## Example Description
This example shows the usage of virtual timing, task management and application lifecycle. It defines two tasks at 1000 and 500 ms rates and 4 virtual timers that expire after 4, 8, 12 and 16 seconds from starts. Both the task they toggle one of the onboard LEDs. Once each timer expires somethings will change in the application behaviour:

- Timer 1 expiration stops Task2
- Timer 2 expiration stops Task 1 and restarts Task 2
- Timer 3 expiration restarts Task1 at the rate of 100ms
- Timer 4 expiration stops the scheduler and ends the application (ideally a new scheduler can be defined and started)

## Required HW
None

## Setup Instructions
None, just connect the board.

## Additional comments
Remember to save the g_os.py file inside the board file system.

