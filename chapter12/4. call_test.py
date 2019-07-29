import asyncio


def callback(sleep_time):
    print('sleep {}s success'.format(sleep_time))


def stop_loop(loop):
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # 即可执行，是指在队列当中顺序优先
    loop.call_soon(callback, 2)
    # 用法一样，添加了线程安全。
    loop.call_soon_threadsafe(callback, 3)
    # loop.call_soon(stop_loop, loop)
    # run_forever 是不会停止的, 添加stop_loop函数，使其停止

    # 指定时间执行
    loop.call_later(2, callback, 3)
    # loop.call_later(3, stop_loop, loop)

    # 单调时间指定运行，是指loop内部的时间
    now = loop.time()
    print(now)
    loop.call_at(now + 4, callback, 4)
    loop.call_at(now + 5, callback, 5)
    loop.call_at(now + 6, stop_loop, loop)

    loop.run_forever()