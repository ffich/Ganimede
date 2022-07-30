## Example Description
This example is an extension of the [IoT/MQTT](https://github.com/ffich/Ganimede/tree/main/10_Python/060_IoT/10_MQTT) sample and is used to trigger two relays via the MQTT protocol.<br>
The `control` topic is supposed to send a message with either `on` or `off`, then the relays are triggered and the new status will be published on the `notification` topic.<br>

Apart from the constants already mentioned in [IoT/MQTT](https://github.com/ffich/Ganimede/tree/main/10_Python/060_IoT/10_MQTT) it is necessary to define the two pins that control the relays:
- `RELAY1_PIN`
- `RELAY2_PIN`

## Required HW
For this example a two channel relay module was used.

## Setup Instructions
None, just connect the board and the relays.

## Additional comments
None