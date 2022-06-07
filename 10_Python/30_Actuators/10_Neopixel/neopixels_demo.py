import time
import machine, neopixel
NEOPIXEL_NUMBER = 60
np = neopixel.NeoPixel(machine.Pin(4), NEOPIXEL_NUMBER)

def demo(np):
    n = np.n

    # cycle
    for i in range(6 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(20)

    # bounce
    for i in range(6 * n):
        for j in range(n):
            np[j] = (0, 0, 255)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(50)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()            

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (0, val, 0)
        np.write()
        
    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (0, 0, val)
        np.write()    

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
    
while (True):
    demo(np)

