import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait

# 线程池, 为什么要线程池
# 主线程中可以获取某一个线程(任务)的状态, 以及返回值
# 当一个线程完成的时候, 主线程能立即知道
# futures可以让多线程和多进程编码接口一直


def get_html(sleep_time):
    time.sleep(sleep_time)
    print('get page {} success'.format(sleep_time))
    return sleep_time


if __name__ == '__main__':
    executor = ThreadPoolExecutor(2)

    # 单个提交
    # 通过submit函数提交函数到线程池, submit 立即执行
    task1 = executor.submit(get_html, 2)
    task2 = executor.submit(get_html, 3)

    # done方法 用于判定某个任务是否完成, 非阻塞
    print(task1.done())
    # cancel 取消某个任务,在没启动的时候取消, 如果已经启动了, 就没法取消了
    print(task2.cancel())
    print(task2.done())
    # result 阻塞状态, 可以过去task的执行结果
    print(task1.result())
    print(task2.result())

    # 批量启动
    urls = [3, 4, 5]
    all_tasks = [executor.submit(get_html, url) for url in urls]
    # 等待任务结束
    wait(all_tasks)
    print('__main__')
    # 要获取已经成功的task的返回值, 此方法谁先完成获取谁
    for future in as_completed(all_tasks):
        data = future.result()
        print('get {} page success'.format(data))

    # 通过executor 获取已经完成的task, 按照进入顺序获取结果
    for data in executor.map(get_html, urls):

        print('get {} page'.format(data))
