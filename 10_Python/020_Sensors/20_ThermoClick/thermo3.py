from machine import Pin, I2C
from time import sleep
import ssd1306

# Sensor I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

# OLED
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while (True):
    sleep(1)
    # Ask for the temparature value
    i2c.writeto(0x48, '0')
    # Read data from sensor
    temp = i2c.readfrom(0x48, 2)
    # Data conversion
    temp = (temp[0] << 8 | temp[1]) >> 4
    # Handle negative values
    if temp & (1 << 11):
        temp |= 0xF800
    # Calculate the actual temperature    
    temp = temp * 0.0625
    # Send temperature data to console
    print(temp)
    # Print temperature on OLED
    temp_str = str(temp)
    oled.fill(0)
    oled.text('Temp: ', 0, 0)
    oled.text(temp_str + 'C', 50, 0)
    oled.show()    
    