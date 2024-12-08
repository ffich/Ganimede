from machine import Pin, SoftI2C
from time import sleep
import onewire
import time, ds18x20
import ssd1306

GanimedeE12 = 0
GanimedeE32 = 1
BOARD = GanimedeE12

if BOARD is GanimedeE12:
    # ESP8266 Pin assignment
    i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
    
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)    

ow = onewire.OneWire(Pin(2))
ds = ds18x20.DS18X20(ow)

while True:
    roms = ds.scan()
    ds.convert_temp()
    time.sleep_ms(1000)
    # Only one sensor attached
    temp = ds.read_temp(roms[0])
    print(temp)
    temp_str = str(temp)
    oled.fill(0)
    oled.text('Temp: ', 0, 0)
    oled.text(temp_str + ' C', 50, 0)
    oled.show()           
        
        
    

