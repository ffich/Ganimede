## Example Description
This example shows the usage of project hierarchy and IPC. Two modules are developed (test_module_1 and test_module_2). Each one of them implement a g-os task and the task 1 drive the board LED toggle (performed by task 2) using an inter-task event (stored in the Ipc.py module). This example demonstrates how you can build modular embedded application using micropython and g-os.  

## Required HW
None

## Setup Instructions
None, just connect the board.

## Additional comments
Remember to save the g_os.py, test_module_1.py, test_module_2.py and Ipc.py files inside the board file system.
