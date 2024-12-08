import machine
from time import sleep

servo_line = machine.Pin(2, machine.Pin.OUT)
servo = machine.PWM(servo_line,freq=50)

while True:
    # Duty for servo is between 20 and 120 for 180° roughly (depends on the type of servo)
    servo.duty(20)
    sleep(1)
    servo.duty(120)
    sleep(1)    