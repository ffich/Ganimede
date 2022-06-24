import socket
import network
import esp
esp.osdebug(None)
import gc
gc.collect()
from machine import Pin, I2C
import ssd1306

ip = ""

# Sensor I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

# OLED
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

relay = Pin(16, Pin.OUT)
relay.off()

ssid_file = open('essid.txt')
ESSID = ssid_file.read()
ssid_file.close()
print(ESSID)

pwd_file = open('pwd.txt')
PWD = pwd_file.read()
pwd_file.close()
print(PWD)

def get_relay_sts():
  if relay.value() == 1:
    return "ON"
  else:
    return "OFF"

def web_page():
    relay_state = get_relay_sts()    
    
    html ="""
<html>
<head>
<title>Ganimede Webserver</title>
</head>

<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">

<style>
html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
h1{color: #0F3376; padding: 3vh;}
p{font-size: 1.5rem;}
button{display: inline-block; background-color: #e72d3b; border: none; border-radius: 4px;
color: white; padding: 30px 80px; text-decoration: none; font-size: 50px; margin: 2px; cursor: pointer;}
</style>

<body>

<h1>Ganimede Webserver</h1>

<p>Relay State: """ + relay_state + """</p>

<p><a href="/?relay=on"><button class="button">Relay ON</button></a></p>
<p><a href="/?relay=off"><button class="button">Relay OFF</button></a></p>

</body>
</html>
"""
    return html  

def do_connect():
    global oled
    global ip
    
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ESSID, PWD)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    
    oled.fill(0)
    ip = sta_if.ifconfig()
    oled.text('IP: ', 0, 0)
    oled.text(str(ip[0]), 0, 10)
    oled.show()    
    
do_connect()

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    #print('Content = %s' % str(request))
    if 'GET /?relay=on' in request:
        relay.on()
        relay_sts = 1

    if 'GET /?relay=off' in request:
        relay.off()
        relay_sts = 0

    oled.fill(0)
    oled.text('IP: ', 0, 0)
    oled.text(str(ip[0]), 0, 10)
    oled.text('Relay: ', 0, 40)
    if relay_sts:
        oled.text('ON', 50, 40)
    else:
        oled.text('OFF', 50, 40)
    oled.show()
    response = web_page()
    conn.send(response)
    conn.close()
