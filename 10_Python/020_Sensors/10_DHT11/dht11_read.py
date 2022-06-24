from machine import Pin, SoftI2C
from time import sleep
import dht
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

#sensor = dht.DHT22(Pin(5))
sensor = dht.DHT11(Pin(5))

while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
    
    temp_str = str(temp)
    temp_f_str = str(temp_f)
    hum_str = str(hum)
    
    oled.fill(0)
    oled.text('Temp C.: ', 0, 0)
    oled.text(temp_str + ' C', 70, 0)
    oled.text('Temp F.: ', 0, 10)
    oled.text(temp_f_str + ' F', 70, 10)
    oled.text('Hum.   : ', 0, 20)
    oled.text(hum_str + ' %', 70, 20)
    oled.show()        
     
  except OSError as e:
    print('Failed to read sensor.')