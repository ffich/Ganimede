import time
import machine, neopixel
from machine import Pin

NEOPIXEL_NUMBER = 16
np = neopixel.NeoPixel(machine.Pin(2), NEOPIXEL_NUMBER)
button = Pin(0, Pin.IN, Pin.PULL_UP) 

GAME_IN_PROGRESS = True
INT = 50
DELAY = 70
GameColor = (0, 0, INT)
i = 0

Red = (INT, 0, 0)
Green = (0, INT, 0)
Blue = (0, 0, INT)
White = (INT, INT, INT)
Non = (0, 0, 0)
Arr = [Red, Non, Green, Non, Blue, Non]
WIN_SEQ_DELAY = 20

while GAME_IN_PROGRESS:
    if button.value() == 0:
        while button.value() == 0:
            pass
        i = i + 1
        np[i] = GameColor
    else:
        if i > 0:
            np[i] = Non
            i = i - 1
    
    np.write()
    time.sleep_ms(DELAY)
    
    # Winning sequence
    if i == NEOPIXEL_NUMBER - 1:
        print("Won!!!")                
        for i in range(len(Arr)):
            for j in range(NEOPIXEL_NUMBER):
                np[j] = Arr[i]
                np.write()
                time.sleep_ms(WIN_SEQ_DELAY)    
        GAME_IN_PROGRESS = False
        
    