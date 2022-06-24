import morsecode
import time
from machine import Pin
import neopixel

TIME = 0.15

LED = 0
NEOPIXEL = 1

# !!!! Select one option for imlementation [LED, NEOPIXEL] !!!
IMPLEMENTATION = NEOPIXEL

if IMPLEMENTATION == NEOPIXEL:
    INT = 50
    NEOPIXEL_NUMBER = 16
    np = neopixel.NeoPixel(Pin(2), NEOPIXEL_NUMBER)

    ON = (200, 0, 0)
    OFF = (0, 0, 0)

    def OnCbk ():
        for i in range(NEOPIXEL_NUMBER):
            np[i] = ON
            np.write()
        
    def OffCbk():
        for i in range(NEOPIXEL_NUMBER):
            np[i] = OFF
            np.write()    

    morse = morsecode.Morse(OnCbk, OffCbk, TIME)
    
elif IMPLEMENTATION == LED:
    LED = Pin (16, Pin.OUT)
    morse = morsecode.Morse(LED.on, LED.off, TIME)

while True:
    morse.send("Hello World")
    time.sleep(5)