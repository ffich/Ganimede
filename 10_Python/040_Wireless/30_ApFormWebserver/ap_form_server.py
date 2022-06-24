try:
  import usocket as socket
except:
  import socket
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

def find_between(s, first, last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def format_string (string):
    string = string.replace('%21', '\x21')
    string = string.replace('%22', '\x22')
    string = string.replace('%23', '\x23')
    string = string.replace('%24', '\x24')
    string = string.replace('%25', '\x25')
    string = string.replace('%26', '\x26')
    string = string.replace('%27', '\x27')
    string = string.replace('%28', '\x28')
    string = string.replace('%29', '\x29')
    string = string.replace('%2A', '\x2A')
    string = string.replace('%2B', '\x2B')
    string = string.replace('%2C', '\x2C')
    string = string.replace('%2D', '\x2D')
    string = string.replace('%2E', '\x2E')
    string = string.replace('%2F', '\x2F')
    
    string = string.replace('%3A', '\x3A')
    string = string.replace('%3B', '\x3B')
    string = string.replace('%3C', '\x3C')
    string = string.replace('%3D', '\x3D')
    string = string.replace('%3E', '\x3E')
    string = string.replace('%3F', '\x3F')
    string = string.replace('%40', '\x40')
    
    string = string.replace('%5B', '\x5B')
    string = string.replace('%5C', '\x5C')
    string = string.replace('%5D', '\x5D')
    string = string.replace('%5E', '\x5E')
    string = string.replace('%5F', '\x5F')
    string = string.replace('%60', '\x60')
    string = string.replace('%61', '\x61')
    
    string = string.replace('%7B', '\x7B')
    string = string.replace('%7C', '\x7C')
    string = string.replace('%7D', '\x7D')    
    return string

def web_page():
  html = """<!DOCTYPE html>
<html>
<meta name="viewport" content="width=device-width, initial-scale=1">
<head> <title>Ganimede Web Setup</title> </head>
<link rel="icon" href="data:;base64,=">
  
<h2>Ganimede Web Setup</h2>
<h3>Please enter data:</h3>
  
<form action="/" method="GET">
    <label for="ssid">SSID:</label><br>
    <input type="text" id="ssid" name="ssid"><br>
    <label for="password">Password:</label><br>
    <input type="text" id="password" name="password"><br><br>
    <left><button type="submit">Submit</button></left>
</form>      
</html>
"""
  return html

SSID = "ganimede"
PWD = "ganimede"

ap_if = network.WLAN(network.AP_IF)

print("Configuration AP")
ap_if.active(True)
ap_if.config(essid=SSID, password=PWD)
ap_if.ifconfig(('192.168.0.1', '255.255.255.0', '192.168.0.1', '8.8.8.8'))

while not ap_if.isconnected():
    pass

print('Connection successful')
print(ap_if.ifconfig())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 80))
s.listen(1) 
 
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(2096) 
    request = str(request)
    print('Content = %s' % request)
    
    # Find ssid and password    
    new_ssid = find_between(request, 'ssid=', '&password=')
    new_pwd = find_between(request, '&password=', ' HTTP/1.1')

    new_ssid = format_string(new_ssid)
    new_pwd = format_string(new_pwd)
    
    f = open('ssid.txt', 'w')
    f.write(new_ssid)
    f.close()        
    
    f = open('pwd.txt', 'w')
    f.write(new_pwd)
    f.close()
        
    print(new_ssid)
    print(new_pwd)
    
    response = web_page()
    conn.send(response)
    conn.close()
    