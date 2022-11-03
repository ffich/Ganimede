## Example Description
This example read a Grove Ultrasonic Distance Sensor at a rate of 5ms and if detects an object in a 10cm range, it turns a relay on for 2 seconds.

## Required HW
- [Grove Ultrasonic Distance Sensor](https://www.seeedstudio.com/Grove-Ultrasonic-Distance-Sensor.html)
- [Relay 3 Click](https://www.mikroe.com/relay-3-click)

## Setup Instructions
Connect the Grove Sensor on the Grove connector and the relay 3 cick board on the Mikrobus socket.

## Additional comments
There are no specific drivers for the Grove ultrasonic distance sensor, so I've adapted an existing HCSR-04 library originally developed by Roberto Sánchez (thanks by the way). [Link to the original library](https://github.com/rsc1975/micropython-hcsr04/blob/master/hcsr04.py). Remember to copy the file usrf_grove.py (keep the name) inside the Ganimede file system (in Thonny, File->Save->Micropyhton device).

## Video Example
Check out a [Demonstration Video](https://www.youtube.com/shorts/ZMBBKq8FC8w). 

## Note for HW 0.2 Beta-Testers
Due to an HW design error in order for the example to work you have to remove R3 resistor. The issue will be fixed in the next HW version.
