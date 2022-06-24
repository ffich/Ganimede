from machine import Pin
import onewire
import time, ds18x20

ow = onewire.OneWire(Pin(2))
ds = ds18x20.DS18X20(ow)

while True:
    roms = ds.scan()
    ds.convert_temp()
    time.sleep_ms(1000)
    for rom in roms:
        print(ds.read_temp(rom)

