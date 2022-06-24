from machine import Pin, SoftI2C
import ssd1306
import time

DELAY = 0.2

# ESP8266 Pin assignment
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while (True):  
    oled.text('Hello World!!!', 0, 0)
    oled.show()
    time.sleep(DELAY)
    oled.text('Ganimede.E12', 0, 10)
    oled.show()
    time.sleep(DELAY)
    oled.text('Powered by', 0, 20)
    oled.show()
    time.sleep(DELAY)
    oled.text('microPython', 0, 30)
    oled.show()
    time.sleep(DELAY)
    oled.text('A project by', 0, 40)
    oled.show()
    time.sleep(DELAY)
    oled.text('Francesco Ficili', 0, 50)
    oled.show()
    time.sleep(1)
    oled.fill(0)
    oled.show()
    time.sleep(1)

  
