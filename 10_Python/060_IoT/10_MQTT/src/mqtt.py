import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
import network
import esp
esp.osdebug(None)

WIFI_SSID = 'Your network name'
WIFI_PASSWORD = 'Your network password'
MQTT_SERVER = 'Your MQTT server ip address' # e.g.: '192.168.1.10'

client_id = ubinascii.hexlify(machine.unique_id())
TOPIC_SUB = b'control'
TOPIC_PUB = b'notification'

# Flag used to identify that a new message has been received
trigger_notification = False


# Basic functions to handle the MQTT protocol

def sub_cb(topic, msg):
    """Callback triggered when new message on the subscribed topic arrives"""
    global trigger_notification
    print((topic, msg))
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
            client.publish(TOPIC_PUB, 'I\'ve got a new value')
            trigger_notification = False
        time.sleep(1)
    except OSError as e:
        print('An error occurred: ' + e)
