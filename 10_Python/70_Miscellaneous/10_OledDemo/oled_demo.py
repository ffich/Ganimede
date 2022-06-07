from machine import Pin, SoftI2C
import ssd1306
from time import sleep

# ESP32 Pin assignment 
#i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello World!!!', 0, 0)
oled.show()
sleep(2)
oled.fill(0)
oled.text('Ganimede.E12', 0, 0)
oled.show()
sleep(2)
oled.fill(0)
oled.text('Powered by', 0, 0)
oled.show()
sleep(2)
oled.fill(0)
oled.text('microPython', 0, 0)
oled.show()
sleep(2)
oled.fill(0)
oled.text('A project by', 0, 0)
oled.show()
sleep(2)
oled.fill(0)
oled.text('Francesco Ficili', 0, 0)
oled.show()
sleep(2)
