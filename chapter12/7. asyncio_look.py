import asyncio

total = 0


async def add():
    global total
    for _ in range(1000000):
        total += 1


async def desc():
    global total
    for _ in range(1000010):
        total -= 1


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    tasks = [add(), desc()]

    loop.run_until_complete(asyncio.wait(tasks))

    print(total)