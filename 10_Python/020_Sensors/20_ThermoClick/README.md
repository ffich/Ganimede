
Example Description
This example read a Texas Instruments TMP102 I2C digialt temperature sensor (on a Thermo 3 click board) and dislay the reault on an OLED and send them over REPL as well. It uses the micropython I2C and SSD1306 libraries.

Required HW
-  [SSD1306 0.96'' OLED display](https://www.amazon.it/AZDelivery-Display-retroilluminato-Raspberry-gratuito/dp/B01L9GC470/ref=sr_1_2?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=CHCOQPCC5U0G&keywords=oled%2B0.96%2Bazdelivery&qid=1656085573&s=electronics&sprefix=oled%2B0.96%2Bazdelivery%2Celectronics%2C73&sr=1-2&th=1****)

- [Thermo 3 click](https://www.mikroe.com/thermo-3-click)

Setup Instructions
Connect the Grove Sensor on the Grove connector and the OLED dislay on CN6 or CN7.

Additional comments
There are no specific driver on micropython for the TMP102 sensor, so the example used the raw I2C to send commands to and read data from the sensor. Check the [TMP102 datasheet](https://download.mikroe.com/documents/datasheets/tmp102-data-sheet.pdf) for additiona details
