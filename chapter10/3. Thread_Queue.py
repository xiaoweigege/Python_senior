# 线程间通信
# 1. 共享变量 global 缺点 线程不安全
# 2. Queue 线程安全

import time
from threading import Thread
from queue import Queue


def get_detail_html(queue):
    # 爬取文章详情
    print('get detail html start')
    while True:
        if queue.empty():
            break
        url = queue.get()
        print('get detail html {}'.format(url))
        time.sleep(2)


def get_detail_url(queue):
    # 爬取文章列表
    print('get detail url start')

    for page in range(10000000):
        time.sleep(2)
        url = 'http:/hello.com/id={}'.format(page)
        queue.put(url)
        print(url)


if __name__ == '__main__':
    detail_url_queue = Queue()
    for _ in range(10):
        html = Thread(target=get_detail_url, args=(detail_url_queue,))
        html.start()

    time.sleep(5)

    for _ in range(5):
        url = Thread(target=get_detail_html, args=(detail_url_queue,))
        url.start()

    # 队列阻塞主线程, 如果不需要阻塞的话需要 task_done()
    detail_url_queue.task_done()
    detail_url_queue.join()