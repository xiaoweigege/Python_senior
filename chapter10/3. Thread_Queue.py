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
        url = queue.get()
        print('get detail html {}'.format(url))
        time.sleep(2)

    print('get detail html end')


def get_detail_url(queue):
    # 爬取文章列表
    print('get detail url start')
    time.sleep(4)
    while True:
        queue.put('http://hello.com/id={}'.format(1))

    print('get detail url end')


if __name__ == '__main__':
    detail_url_queue = Queue()
