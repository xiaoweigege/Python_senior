# 1. run_until_complete
import time
import asyncio

# loop = asyncio.get_event_loop()
#
# # 会停止
# loop.run_until_complete()
# # 不停止
# loop.run_forever()


async def get_html(sleep_time):
    print('waiting')
    await asyncio.sleep(sleep_time)
    print(f'done after {sleep_time}s')


async def compute(x, y):
    print(f'正在计算 {x} + {y}')
    await asyncio.sleep(2)
    print(f'计算结束.')
    return x + y


async def print_sum(x, y):
    number = await compute(x, y)
    print(number)
    return number

if __name__ == '__main__':
    start_time = time.time()
    # task1 = get_html(1)
    # task2 = get_html(2)
    # task3 = get_html(3)

    loop = asyncio.get_event_loop()
    # 协程取消例子。
    # try:
    #     loop.run_until_complete(asyncio.wait([task1, task2, task3]))
    # except KeyboardInterrupt:
    #     all_tasks = asyncio.Task.all_tasks()
    #     for task in all_tasks:
    #         print('task cancel')
    #         print(task.cancel())
    #
    #     loop.stop()
    #     loop.run_forever()
    #
    # finally:
    #     loop.close()

    # 协程嵌套例子
    tasks = [print_sum(1, number) for number in range(1, 10)]
    # get_future = asyncio.ensure_future(*tasks)
    loop.run_until_complete(asyncio.gather(*tasks))

    # print(get_future.result())

    end_time = time.time()

    print(f'总共耗时: {end_time-start_time} s')




