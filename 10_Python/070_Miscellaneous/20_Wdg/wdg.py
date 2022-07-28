from machine import WDT
wdt = WDT() # 2 seconds timeout by default.

while True:
    # read a line
    value = input('Write something within 2 seconds and press enter\n')
    print('\nWatchdog not triggered\n')
    wdt.feed()
