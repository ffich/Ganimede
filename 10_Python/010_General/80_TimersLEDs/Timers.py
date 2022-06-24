from machine import Pin, Timer

Led1 = Pin(2, Pin.OUT)
    
timer = Timer(-1)    
timer.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:Led1.value(not Led1.value()))