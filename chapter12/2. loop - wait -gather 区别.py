# 3个要点 时间循环 + 回调(驱动生成器) + epoll(IO多路复用)
# asyncio是Python用于解决异步IO编程的一整套解决方案
# Tornado,gevent,Twisted(Scrapy, django channels)

# 使用asyncio
# 使用协程，必须搭配 事件循环才能使用
import time
import asyncio


async def get_url(url):
    print(f'start url:{url}')
    # time.sleep(2)
    # 在耗时操作中，需要加上await
    # 主要是在模拟耗时操作
    await asyncio.sleep(2)
    print(f'end url: {url}')
    return url


if __name__ == '__main__':
    start_time = time.time()
    # 获取asyncio 事件循环
    loop = asyncio.get_event_loop()

    # 提交多个任务 wait
    # tasks = [get_url(f'https://www.baidu.com/{i}') for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))

    # 提交多个任务 gather
    # tasks = [get_url(f'https://www.baidu.com/{i}') for i in range(10)]
    # loop.run_until_complete(asyncio.gather(*tasks))

    # gather 和  wait 的 区别
    # 1. gather 等级 更高 可以分组
    group1 = [get_url(f'https://www.baidu.com/{i}') for i in range(10)]
    group2 = [get_url(f'https://www.xiaoweigege.com/{i}') for i in range(10)]
    # 或者
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    # 任务取消
    # group2.cancel()

    loop.run_until_complete(asyncio.gather(group1, group2))


    end_time = time.time()

    print(f'总共耗时：{end_time-start_time}')