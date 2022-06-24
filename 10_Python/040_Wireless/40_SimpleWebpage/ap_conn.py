# AP connection library
import network
import socket
import esp
esp.osdebug(None)
import gc
gc.collect()

ESSID_FILE_NAME = 'essid.txt'
PWD_FILE_NAME = 'pwd.txt'

class ap_conn:
    def __init__ (self):
        self.ssid_file = open()
        self.ESSID = self.ssid_file.read(ESSID_FILE_NAME)
        self.ssid_file.close()
        self.pwd_file = open(PWD_FILE_NAME)
        self.PWD = self.pwd_file.read()
        self.pwd_file.close()

    def connect (self):
        self.sta_if = network.WLAN(network.STA_IF)
        if not self.sta_if.isconnected():
            print('connecting to network...')
            self.sta_if.active(True)
            self.sta_if.connect(ESSID, PWD)
            while not self.sta_if.isconnected():
                pass
            print('network config:', self.sta_if.ifconfig())        

    def start_server (self):
        self.addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        self.s = socket.socket()
        self.s.bind(self.addr)
        self.s.listen(5)
