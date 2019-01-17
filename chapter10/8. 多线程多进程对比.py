# 多进程编程
# 耗CPU的操作, 用多进程编程, 对于I/O操作来说,是用多线程编程
# 进程切换代价要高于多线程
# 1. 对于耗费CPU的操作(计算, 图形处理) 多进程优于多线程
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor


def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)


# 2. 对于I/O操作来说, 多线程优于多进程
def random_sleep(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    # executor = ThreadPoolExecutor(3)
    with ThreadPoolExecutor(3) as executor:
        start_time = time.time()
        all_task = [executor.submit(random_sleep, number) for number in [2] * 30]
        for task in as_completed(all_task):
            data = task.result()
            print(data)
        last_time = time.time()
        print('Thread last time is {}'.format(last_time - start_time))

    with ProcessPoolExecutor(3) as executor:
        start_time = time.time()
        all_task = [executor.submit(random_sleep, number) for number in [2] * 30]
        for task in as_completed(all_task):
            data = task.result()
            print(data)
        last_time = time.time()
        print('Process last time is {}'.format(last_time - start_time))
