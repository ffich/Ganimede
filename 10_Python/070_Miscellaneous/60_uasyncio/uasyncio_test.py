import uasyncio as asyncio

count = 0
period = 1000


async def foo(n):
    global count
    while True:
        await asyncio.sleep_ms(0)
        count += 1
        print('Foo', n)


async def main(delay):
    for n in range(1, 4):
        asyncio.create_task(foo(n))
    print('Testing for {:d} seconds'.format(delay))
    await asyncio.sleep(delay)


asyncio.run(main(period))
print('Coro executions per sec =', count/period)