from machine import Pin
from umqtt.simple import MQTTClient
import time
import ubinascii
import machine
import network
import esp
esp.osdebug(None)

WIFI_SSID = 'Your network name'
WIFI_PASSWORD = 'Your network password'
MQTT_SERVER = 'Your MQTT server ip address' # e.g.: '192.168.1.10'

RELAY1_PIN = 4
RELAY2_PIN = 5

client_id = ubinascii.hexlify(machine.unique_id())
TOPIC_SUB = b'control'
TOPIC_PUB = b'notification'

# Flag used to identify that a new message has been received
trigger_notification = False
message = ''


# Basic functions to handle the MQTT protocol

def sub_cb(topic, msg):
    """Callback triggered when new message on the subscribed topic arrives"""
    global trigger_notification
    global message
    print((topic, msg))
    message = str(msg, "utf-8")
    trigger_notification = True

def connect_and_subscribe():
    """Connect to the MQTT server and subscribe to TOPIC_SUB"""
    mqtt_client = MQTTClient(client_id, MQTT_SERVER, keepalive=30)
    mqtt_client.set_callback(sub_cb)
    mqtt_client.connect()
    mqtt_client.subscribe(TOPIC_SUB)
    print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_SERVER, TOPIC_SUB))
    return mqtt_client

def restart_and_reconnect():
    """Sleep 10 seconds and restart the board. To be called in case of errors"""
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()


# Class to handle the relay
class Relay():
    def __init__(self, pin):
        self._relay = Pin(pin, Pin.OUT)
        
    def setOn(self):
        self._relay.value(0)
        
    def setOff(self):
        self._relay.value(1)

# Initialize the relays
relay1 = Relay(RELAY1_PIN)
relay2 = Relay(RELAY2_PIN)

# Connect to WiFi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(WIFI_SSID, WIFI_PASSWORD)

while station.isconnected() is False:
    pass


# Connect to the MQTT server
try:
    client = connect_and_subscribe()
except OSError as e:
    restart_and_reconnect()


# Keep listening for new messages
while True:
    try:
        client.check_msg()
        if trigger_notification is True:
            if message == 'on':
                relay1.setOn()
                relay2.setOn()
                client.publish(TOPIC_PUB, 'Relays are ' + message)
            elif message == 'off':
                relay1.setOff()
                relay2.setOff()
                client.publish(TOPIC_PUB, 'Relays are ' + message)
            else:
                print('Insert \'on\' or \'off\'')
            trigger_notification = False
        time.sleep(1)
    except OSError as e:
        print('An error occurred: ' + str(e))
