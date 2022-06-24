import os
import network
import ujson
import usocket
import uselect
from machine import Pin, reset

class ESPLed():
    def __init__(self):
        self.led = Pin(2, Pin.OUT)

    def activate(self):
        self.led.value(0)

    def deactivate(self):
        self.led.value(1)

class ESPButton():
    def __init__(self):
        self.button = Pin(0, Pin.IN)

    def isPressed(self):
        if self.button.value() == 0:
            return True
        else:
            return False

class AdHocNetwork():
    def __init__(self):
        self.ap_if = network.WLAN(network.AP_IF)
        self._activate()
        self.ap_if.config(essid = "Ganimede E12", password = "0123456789", authmode=3)
        self.ap_if.ifconfig(('192.168.0.1', '255.255.255.0', '192.168.0.1', '8.8.8.8'))

    def _activate(self):
        self.ap_if.active(True)

    def _deactivate(self):
        self.ap_if.active(False)

    def close_socket(self):
        self.s.close()
        self._deactivate()

    def open_socket(self):
        self.s = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
        self.s.setsockopt(usocket.SOCK_STREAM, usocket.SO_REUSEADDR, 1)
        try:
            self.s.bind(('', 80))
        except:
            pass
        self.s.listen(5)

    def _handle_data(self, data):
        file = open('networkData.json', 'w+')
        file.write(data)
        file.close()

    def listen(self):
        isListenNeeded = True
        conn, addr = self.s.accept()
        request = str(conn.recv(1024))[1:-1]
        try:
            while True:
                request += str(conn.recv(1024))[2:-1]
                conn.setblocking(False)
        except:
            pass
        if request.find('POST'):
            startJson = request.find('{')
            endJson = request.rfind('}') + 1
            request = request[startJson:endJson]
            try:
                json = ujson.loads(request)
                if json['networkName'] != "" and json['networkPassword'] != "":
                    self._handle_data(request)
                    isListenNeeded = False
            except:
                print("error")
            response = str(request)

        conn.send('HTTP/1.1 200 OK\n')
        conn.send("Access-Control-Allow-Origin: *\n")
        conn.send("Access-Control-Allow-Headers: *\n")
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()

        return isListenNeeded


class StationNetwork():
    def __init__(self):
        try:
            file = open('networkData.json', 'r')
            data = file.read()
            data = ujson.loads(data)
            self.networkName = data['networkName']
            self.networkPassword = data['networkPassword']
            self.sta_if = network.WLAN(network.STA_IF)
            self.sta_if.active(True)
            self.sta_if.connect(self.networkName, self.networkPassword)
            while not self.sta_if.isconnected():
                pass
        except:
            self.networkName = ""
            self.networkPassword = ""
            self.sta_if = network.WLAN(network.STA_IF)

    def open_socket(self):
        self.s = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
        self.s.setsockopt(usocket.SOCK_STREAM, usocket.SO_REUSEADDR, 1)
        try:
            self.s.bind(('', 80))
        except:
            pass
        self.s.listen(5)
        self.poller = uselect.poll()
        self.poller.register(self.s, uselect.POLLIN)

    def close_socket(self):
        self.s.close()
        self.sta_if.active(False)

    def listen(self):
        event = self.poller.poll(100)
        request = ""
        for (fd, event) in event:
            if event == uselect.POLLIN:
                conn, addr = self.s.accept()
                request = str(conn.recv(1024))
                if request.find('POST'):
                    startJson = request.find('{')
                    endJson = request.rfind('}') + 1
                    request = request[startJson:endJson]
                    try:
                        request = ujson.loads(request)
                    except:
                        print("error")
                    response = str(request)

                conn.send('HTTP/1.1 200 OK\n')
                conn.send("Access-Control-Allow-Origin: *\n")
                conn.send("Access-Control-Allow-Headers: *\n")
                conn.send('Content-Type: text/html\n')
                conn.send('Connection: close\n\n')
                conn.sendall(response)
                conn.close()

        return request

def handleAdHocNet():
    if not 'networkData.json' in os.listdir():
        adHocNetwork = AdHocNetwork()
        adHocNetwork.open_socket()

        while adHocNetwork.listen():
            pass
        adHocNetwork.listen()
        adHocNetwork.close_socket()

def main():
    handleAdHocNet()
    led = ESPLed()
    button = ESPButton()
    stationNetwork = StationNetwork()
    stationNetwork.open_socket()
    count = 0
    while True:
        req = stationNetwork.listen()
        if req != "":
            try:
                if req['ledStatus'] is True:
                    led.activate()
                else:
                    led.deactivate()
            except:
                pass

        if button.isPressed():
            count+=1
            if count == 90:
                os.remove('networkData.json')
                stationNetwork.close_socket()
                reset()
        else:
            count = 0

main()