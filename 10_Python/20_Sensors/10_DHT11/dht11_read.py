from machine import Pin, SoftI2C
from time import sleep
import dht
import ssd1306

OFFSET = 70

#sensor = dht.DHT22(Pin(5))
sensor = dht.DHT11(Pin(5))

# ESP8266 Pin assignment
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

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

    temp_string = str(temp)
    hum_string = str(hum)
    temp_f_string = str(temp_f)
    
    oled.fill(0)
    oled.text('Temp[C]:', 0, 0)
    oled.text(temp_string, OFFSET,0)
    oled.text('Hum[%]:', 0, 20)
    oled.text(hum_string, OFFSET, 20)    
    oled.text('Temp[F]:', 0, 40)
    oled.text(temp_f_string, OFFSET, 40)      
    oled.show()    
    
  except OSError as e:
    print('Failed to read sensor.')