# 3个要点 时间循环 + 回调 + epoll
# asyncio是Python用于解决异步IO编程的一整套解决方案
# Tornado,gevent,Twisted(Scrapy, django channels)

# 使用asyncio
import time
import asyncio
from functools import partial


async def get_html(url):
    print('start get url, {}'.format(url))
    await asyncio.sleep(2)
    print('end get url')
    return 'xiaowei'


def callback(email, future):
    print('send email {}'.format(email))


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # 第一种执行方式
    # loop.run_until_complete(get_html('http://www.baidu.com'))

    # 多任务执行方式
    # tasks = [get_html('http://www.baidu.com') for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))

    # 第一种方式获取返回值
    # get_future = asyncio.ensure_future(get_html('http://www.baidu.com'))
    # loop.run_until_complete(get_future)
    # print(get_future.result())

    # 第二种方式获取返回值
    # task = loop.create_task(get_html('http://www.baidu.com'))
    # # 执行完成之后执行回调
    # # 如果callback 要传参数怎么办 from functools import partial
    # # partial 能将函数包装成另外一个函数
    # task.add_done_callback(partial(callback, '24094264@qq.com'))
    # loop.run_until_complete(task)
    # print(task.result())

    # gather
    # task = [get_html('http://www.baidu.com') for i in range(10)]
    # loop.run_until_complete(asyncio.gather(*task))

    # gather 和 wait 的却别
    # gather 更加高级, 可以执行多组
    group1 = [get_html('http://www.baidu.com') for i in range(10)]
    group2 = [get_html('http://www.xiaowei.com') for i in range(10)]
    loop.run_until_complete(asyncio.gather(*group1, *group2))
    end_time = time.time()
    print(end_time - start_time)
