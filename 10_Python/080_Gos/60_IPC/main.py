from test_module_1 import *
from test_module_2 import *

# Create the scheduler
mySched = g_os.sch()

# Add tasks to the scheduler queue
mySched.add_task(Task1)
mySched.add_task(Task2)

# Start the scheduler
mySched.start()