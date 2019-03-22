# run_until_complete
# 1.loop会被放到future中
# 2.取消future(task)
import time
import asyncio


async def get_html(sleep_time):
    print('waiting')
    await asyncio.sleep(sleep_time)
    print('done after {}s'.format(sleep_time))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    task1 = get_html(2)
    task2 = get_html(3)
    task3 = get_html(4)

    task = [task1, task2, task3]
    # 第一种终止方式 Ctrl + c
    try:
        loop.run_until_complete(asyncio.wait(task))
    except KeyboardInterrupt as e:
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print('cancel task')
            print(task.cancel())

        loop.stop()
        loop.run_forever()

    finally:
        loop.close()
