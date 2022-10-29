## Example Description
This example shows how to use the watchdog.<br>
The implementation uses the built-in library functions to instantiate the watchdog and the related `feed` method to keep resetting it. If an input is not given within 2 seconds, the WDG triggers a reset.<br>

## Required HW
None

## Setup Instructions
None, just connect the board and see that if not keyboard input is provided via the REPL within 2 seconds, the reset is performed.

## Additional comments
None