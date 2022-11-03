import time
import machine, neopixel

NEOPIXEL_NUMBER = 16
np = neopixel.NeoPixel(machine.Pin(2), NEOPIXEL_NUMBER)

INT_MULTI = 50
INT_SINGLE = 255
DELAY_MULTI = 25
DELAY_SINGLE = 35

RedM = (INT_MULTI, 0, 0)
GreenM = (0, INT_MULTI, 0)
BlueM = (0, 0, INT_MULTI)
WhiteM = (INT_MULTI, INT_MULTI, INT_MULTI)

RedS = (INT_SINGLE, 0, 0)
GreenS = (0, INT_SINGLE, 0)
BlueS = (0, 0, INT_SINGLE)
WhiteS = (INT_SINGLE, INT_SINGLE, INT_SINGLE)

Non = (0, 0, 0)
ArrMulti = [RedM, Non, GreenM, Non, BlueM, Non, WhiteM, Non]
ArrSingle = [RedS, GreenS, BlueS, WhiteS]

while True:
    for i in range(len(ArrMulti)):
        for j in range(NEOPIXEL_NUMBER):
            np[j] = ArrMulti[i]
            np.write()
            time.sleep_ms(DELAY_MULTI)
        
    for i in range(len(ArrSingle)):
        for j in range(NEOPIXEL_NUMBER):
            np[j] = ArrSingle[i]
            np[j-1] = Non
            np.write()
            time.sleep_ms(DELAY_SINGLE)        
    np[j] = Non

