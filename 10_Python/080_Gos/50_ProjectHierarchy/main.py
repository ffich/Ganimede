from test_module_1 import *

# Create the scheduler
mySched = g_os.sch()

# Add tasks to the scheduler queue
mySched.add_task(MyTask)

# Start the scheduler
mySched.start()