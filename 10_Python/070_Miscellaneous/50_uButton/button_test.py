from ubutton import uButton
import uasyncio as asyncio
import machine

# Instantiate the controller instance
button = uButton(
    machine.Pin(0, machine.Pin.IN),
    cb_short = lambda: print('short press'),
    short_wait=True,
    cb_long = lambda: print('long press'),
    bounce_time=25,
    long_time=500,
    act_low=True
)

# Get a reference to the event loop
loop = asyncio.get_event_loop()
# Schedule coroutines to run ASAP
loop.create_task(button.run())
# Run the event loop
loop.run_forever()

