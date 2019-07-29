# 3个要点 时间循环 + 回调(驱动生成器) + epoll(IO多路复用)
# asyncio是Python用于解决异步IO编程的一整套解决方案
# Tornado,gevent,Twisted(Scrapy, django channels)

# 使用asyncio
# 使用协程，必须搭配 事件循环才能使用
import time
import asyncio
# 处理回调函数传参问题
from functools import partial


async def get_url(url):
    print(f'start url:{url}')
    # time.sleep(2)
    # 在耗时操作中，需要加上await
    # 主要是在模拟耗时操作
    await asyncio.sleep(2)
    print(f'end url: {url}')
    return url


def callback(future):
    print('send email xiaowei')


def callback_params(url, future):
    print('hello world', url)


if __name__ == '__main__':
    start_time = time.time()
    # 获取asyncio 事件循环
    loop = asyncio.get_event_loop()
    # 阻塞方法，等待函数执行完成，才会执行下一步, 此次是提交单个任务
    # loop.run_until_complete(get_url('https://www.baidu.com'))

    # 提交多个任务
    # tasks = [get_url(f'https://www.baidu.com/{i}') for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))

    # 获取任务的返回值
    # get_future = loop.create_task(get_url(f'https://www.baidu.com/{1}'))
    # 或者
    get_future = asyncio.ensure_future(get_url(f'https://www.baidu.com/{1}'))
    # 给任务添加回调功能
    get_future.add_done_callback(callback)

    # 如果回调函数中 需要 传参数怎么办
    get_future.add_done_callback(partial(callback_params, 'xiaoweigege'))

    # 将任务注册到loop中去
    loop.run_until_complete(get_future)

    return_url = get_future.result()
    print('获取结果', return_url)

    end_time = time.time()

    print(f'总共耗时：{end_time-start_time}')