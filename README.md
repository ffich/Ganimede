# Ganimede
Public Repository for Ganimede board family. 

# Repo Description
This repo contains some getting started material and some example for using Ganimede.E12 with Python, C/C++ and Javascript.

# What Ganimede is?
The Ganimede is a family of fancy development boards based on ESP8266 and ESP32 SoC from EspressIf (I will probably make a version based on R2040 as well).
The idea behind Ganimede is that I started to be bored of soldering, breadboarding and, more in general, to have messy connection between my development board and the sensor and actuators I needed for my experiments.
Additionally, after the experience with Mercury System, I decided to not to do again such a crazy thing in which I had to make all the HW and SW, as it required literally hundreds of days and it's not sustainable (and even if it would be, Anna would probably kill me). Moreover, I do love C, but I understond that this is not the same for everybody and is also a bit limiting, so welcome to Python and Javascript. Last but not least, I wanted to have something really cheap, that can be used by me, friends and (possibly) others.
So, in the end, Ganimede is a development board with the following characteristics:

1. It's based on ESP SoC with integrated peripherals like WiFi, BT and USB
2. It carries some sockets/connectors that allow to use well known standards (Mikroe MikroBUS, SeedStudio grove, others), so no more messy connections with sensor/actuators around your desk.
3. Can be programmed in C/C++, Python and Javascript
4. It's really cheap
5. It's open hardware, I will share schematics and design files
6. It's really simple to use

# Ganimede.E12
The hardware details of Ganimede.E12 are resumed in the picture below:

![HwDetails](https://static.wixstatic.com/media/2492ae_2b2e0d6cc230491f92e3bd0d91141a82~mv2.png/v1/fill/w_1467,h_647,al_c/2492ae_2b2e0d6cc230491f92e3bd0d91141a82~mv2.png)


## Main characteristics of Ganimede.E12:
- USB connection for communication, Power and Flashing
- WiFi
- 11x GPIO
- 2x User LEDs
- 2x User buttons
- 1x MikroBUS Socket
- 1x Grove Connector
- 1x Neopixel/1-wire Connector
- 2x OLED Connectors

If you want more information you can have a look at the [Ganimede.E12 Datasheet](https://2492ae4f-d323-49c0-bc1e-8d5936f83a9d.usrfiles.com/ugd/2492ae_11933c1aee514b55b51fd540d7772119.pdf) and to the [Ganimede.E12 Product Page](https://frafich.wixsite.com/jupitersystem/product-page/ganimede-e12).

# Ganimede.E32
The hardware details of Ganimede.E32are resumed in the picture below:

(To be added)

## Main characteristics of Ganimede.E32:
- USB connection for communication, Power and Flashing
- WiFi
- Bluetooth
- 24x GPIO
- 1x User LEDs
- 2x User buttons
- 1x MikroBUS Socket
- 2x Grove Connector
- 2x Neopixel/1-wire Connector
- 1x OLED Connectors
- 1x SRF04 Connector

If you want more information you can have a look at the [Ganimede.E32 Datasheet](link) and to the [Ganimede.E32 Product Page](link).

