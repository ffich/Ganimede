## Example Description
This example implements a simple communication based on the MQTT protocol.<br>
The software will subscribe to `control` topic, and every time a new data has received will publish a string on the `notification` one.<br>

The following constants need to be redefined by the user:
- `WIFI_SSID`: the name of your WiFi network
- `WIFI_PASSWORD`: the password of your WiFi network
- `MQTT_SERVER`: the IP address of your MQTT server

## Required HW
None

## Setup Instructions
None, just connect the board.

## Additional comments
None