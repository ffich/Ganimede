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

