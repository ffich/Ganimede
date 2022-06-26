## Getting Started with MicroPython and Ganimede
MicroPython is a perfect environment to be used with Ganimede Boards. In order to get started with Ganimede and MicroPython you need to:

1. Download the MicroPython Firmware
2. Flash the downloaded image on Ganimede using ESPTool
3. Download and install a MicroPython compatible IDE (e.g. Thonny)

Then you can start developing your MicroPython applications with Ganimede.

## Download the MicroPython Firmware
You can download the MicroPython firmware image from the download section of MicroPython website: https://micropython.org/download/

The correct image to flash depends on the Ganimede board, have a look at the table below:
| Ganimede Board | MicroPython Target  | Download Link                                       |
|----------------|:-------------------:|:---------------------------------------------------:|
| Ganimede.E12   | ESP8266             | https://micropython.org/download/esp8266/           |
| Ganimede.E32   | ESP32               | https://micropython.org/download/esp32/             |

We recommend to download the last stable version, but bear in mind that the repository may be aligned to an older version of MicroPython.

## Flash the MicroPython Firmware
Once you have downloaded the MicroPython firmware, you need to flash it on Ganimede. To do this you need to download ESPtool from the following link: https://github.com/espressif/esptool

Then you need to use this tool to flash the FW on the board. Ganimede doesn't have an auto-programming circuitry, so it has to be explicitly put in programming mode, and this happes if the board boot with the Flash button (GPIO0) at the low state. To do this:

1. Press and hold the Flash button
2. Reset the board by pressing and releasing the Reset button

Once you have put the board in programming state you can flash the MicroPython FW. This requires tipycally two steps:

1. Erase the board issuing:
``` 
esptool.py --port [VCP] erase_flash

```
Where VCP is the communication port associated by the system to the board (e.g. a COM port in Windows or /dev/ttyUSB0 in Linux)

2. Deploy the FW by issuing:
``` 
esptool.py --port [VCP] --baud 460800 write_flash --flash_size=detect 0 esp8266.bin
``` 
Where VCP is as above and esp8266.bin is the binary image previously downloaded.

You can follow the following tutorials on the MicroPython website if needed:

| Ganimede Board | MicroPython website Getting Started                                       |
|----------------|:-------------------------------------------------------------------------:|
| Ganimede.E12   | https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#intro  |
| Ganimede.E32   | https://docs.micropython.org/en/latest/esp32/tutorial/intro.html          |

## Download and Install Thonny
Once the MicroPython firmware is correctly installed, you can download Thonny from the following link: https://thonny.org/

## Potential issues with ESPTool
In case of issues with ESPTool, check the EspressIf ESPTool troubleshooting section: https://docs.espressif.com/projects/esptool/en/latest/esp8266/troubleshooting.html

## Example List 
The following examples are provided:

- General
  - Blink 
  - USB Console
  - Click Relay
  - OLED Text
  - OLED Shapes
  - Basic Multitasking
  - LED Multitasking
  - LED Timer

- Sensors
  - DHT11
  - Thermo Click (TM102)
  - Ultrasonic Distance Sensor (Range Finder)
  - BME Sensor (F)
  - Air Quality Sensor (F)
  - DS18B20
  - PIR Sensor

- Actuators
  - Neopixels
  - Stepper (F)
  - DC Mortor Control (F)
  - Servo
  - Buzzer (F)

- Wireless
  - AP webserver
  - Station Webserver
  - AP Form
  - AP Conn Library (and webpages exampels)

- Communication
  - CAN (F)
  - RS485 (F)

- IoT 
  - MQTT Basic (A)
  - MQTT BME sensor (A)
  - MQTT Relay (A)

- Miscellaneous
  - File System (A)
  - Watchdog (A)
  - RTC (A)
  - Morse Code
  - uButton
  - uAsyncIO (F)
  - Machine Learning (F)

- G-OS (Ganimede OS)
  - Basic
  - Advanced
  - State Machine
  - LedBlink State Machine
  - Project Hyerarchy
  - InterProcess Communication


