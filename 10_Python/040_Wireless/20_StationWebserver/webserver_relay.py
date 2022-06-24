import socket
import network
import esp
esp.osdebug(None)
import gc
gc.collect()
from machine import Pin

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
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ESSID, PWD)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    
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
  if 'GET /?relay=off' in request:
    relay.off() 
  response = web_page()
  conn.send(response)
  conn.close()
