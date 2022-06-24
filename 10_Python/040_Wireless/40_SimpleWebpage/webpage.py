import ap_conn
import socket
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

def webpage_template ():
  html = """

"""
  return html

def webpage_1 ():
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

def webpage_2 ():
  html = """<!DOCTYPE html>
<html>
<meta name="viewport" content="width=device-width, initial-scale=1">
<head>
<style>
.button {
  background-color: tomato;
  color: white;
  border: 2px solid black;
  margin: 20px;
  padding: 20px;
}
</style>
</head>
<body>

<h1>Sample Button webpage</h1>
<p>Make a choiche:</p>
<p><a href="/?something"><button class="button">Button 1</button></a><a href="/?something_else"><button class="button">Button 2</button></a></p>

</body>
</html>
"""
  return html

def webpage_3 ():
  html = """<!DOCTYPE html>
<html>
<meta name="viewport" content="width=device-width, initial-scale=1">
<head>
</head>
<body>

<h3>Sample Webpage</h3>
<p>Make a choiche:</p>
<p><a href="/?something"><button type="button">Button1</button></a></p>
<p><a href="/?something_else"><button type="button">Button1</button></a></p>

</body>
</html>
"""
  return html

def webpage_4 ():
  html = """
<!DOCTYPE HTML>
<html>
<meta name="viewport" content="width=device-width, initial-scale=1">
<body>

<h2>JavaScript Confirm Box</h2>


<button onclick="myFunction()">Try it</button>

<p id="demo"></p>

<script>
function myFunction() {
  var txt;
  if (confirm("Press a button!")) {
    txt = "You pressed OK!";
  } else {
    txt = "You pressed Cancel!";
  }
  document.getElementById("demo").innerHTML = txt;
}
</script>

</body>
</html>
"""
  return html


conn = ap_conn.ap()
conn.connect()
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  response = webpage_4()
  conn.send(response)
  conn.close()
