import machine, time
from machine import Pin

__version__ = '0.1.0'
__author__ = 'Original driver developed by Roberto Sánchez, adapted to the Grove USRF by Francesco Ficili'
__license__ = "Apache License 2.0. https://www.apache.org/licenses/LICENSE-2.0"
__notes__ = 'Adaptation to the Grove ultrasonic sensor of the original driver for HCSR-04 developed by Roberto Sánchez'

class USRF:
    """
    Driver to use the untrasonic Grove Sensor.
    The sensor range is between 2cm and 4m.
    The timeouts received listening to echo pin are converted to OSError('Out of range')
    """
    def __init__(self, pin, echo_timeout_us=500*2*30):
        self.echo_timeout_us = echo_timeout_us
        self.pin = pin

    def _send_pulse_and_wait(self):
        """
        Send the pulse to trigger and listen on echo pin.
        We use the method `machine.time_pulse_us()` to get the microseconds until the echo is received.
        """
        self.tr_echo = Pin(self.pin, Pin.OUT)
        self.tr_echo.value(0) 
        time.sleep_us(2)
        self.tr_echo.value(1)
        time.sleep_us(5)
        self.tr_echo.value(0)
        self.tr_echo = Pin(self.pin, Pin.IN)
        try:
            pulse_time = machine.time_pulse_us(self.tr_echo, 1, self.echo_timeout_us)
            #print(pulse_time)
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110: # 110 = ETIMEDOUT
                raise OSError('Out of range')
            raise ex

    def distance_mm(self):
        """
        Get the distance in milimeters without floating point operations.
        """
        pulse_time = self._send_pulse_and_wait()

        # To calculate the distance we get the pulse_time and divide it by 2 
        # (the pulse walk the distance twice) and by 29.1 becasue
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.34320 mm/us that is 1mm each 2.91us
        # pulse_time // 2 // 2.91 -> pulse_time // 5.82 -> pulse_time * 100 // 582 
        mm = pulse_time * 100 // 582
        return mm

    def distance_cm(self):
        """
        Get the distance in centimeters with floating point operations.
        It returns a float
        """
        pulse_time = self._send_pulse_and_wait()

        # To calculate the distance we get the pulse_time and divide it by 2 
        # (the pulse walk the distance twice) and by 29.1 becasue
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.034320 cm/us that is 1cm each 29.1us
        cms = (pulse_time / 29) / 2
        return cms