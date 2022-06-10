# Ganiemede.E12
Public Repo for Ganimede.E12 board. 

# Repo Description
This repo contains some getting started material and some example for using Ganimede.E12 with Python, C/C++ and Javascript.

# What Ganimede.E12 is?
The Ganimede.E12 is a fancy development board based on ESP8266 SoC from EspressIf and, more specifically, on the ESP-12 SoM developed by AI-Thinker.
The idea behind Ganimede.E12 (and more in general to all the Ganimede family) is that I started to be bored of soldering, breadboarding and, more in general, to have messy connection between my development board and the sensor and actuators I needed for my experiments.
Additionally, after the experience with Mercury System, I decided to not to do again such a crazy things in which I had to make all the HW and SW, as it required literally hundreds of days and it's not sustainable (and even if it would be, Anna would kill me). Moreover, I do love C, but I understond that this is not the same for everybody and is also a bit limiting, so welcome to Python and Javascript. Last but not least, I wanted to have something really cheap, that can be used by me, friends and (possibly) others.
So, in the end, Ganimede.E12 is a development board with the following characteristics:

1. It's based on ESP8266, 4MB Flash, Integrated USB and WiFi
2. It carries some sockets/connectors that allow to use well known standards (Mikroe MikroBUS, SeedStudio grove, others), so no more messy connections with sensor/actuators around your desk.
3. Can be programmed in C/C++, Python and Javascript
4. It's really cheap, target price is 15€
5. It's open hardware, I will share schematics and design files
6. It's really simple to use

# Board Description
The hardware details of the board are resumed in the picture below:

![HwDetails](https://static.wixstatic.com/media/2492ae_2b2e0d6cc230491f92e3bd0d91141a82~mv2.png/v1/fill/w_1467,h_647,al_c/2492ae_2b2e0d6cc230491f92e3bd0d91141a82~mv2.png)


## Main characteristics:
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






