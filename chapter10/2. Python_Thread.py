# 对于I/O操作来说，多线程和多进程性能差别不大
# 1.通过Thread类实例化
import time
from threading import Thread

# 函数实现多线程


def get_detail_html(url):
    print('get detail html start')
    time.sleep(2)
    print('get detail html end')


def get_detail_url(url):
    print('get detail url start')
    time.sleep(4)
    print('get detail url end')

# 通过继承Thread实现多线程


class GetDetailHtml(Thread):
    def __init__(self, url):
        super().__init__()

    def run(self):
        print('get detail html start')
        time.sleep(2)
        print('get detail html end')


class GetDetailUrl(Thread):
    def __init__(self, url):
        super().__init__()

    def run(self):
        print('get detail url start')
        time.sleep(4)
        print('get detail url end')


if __name__ == '__main__':
    # t1 = Thread(target=get_detail_html, args=('', ))
    # t2 = Thread(target=get_detail_url, args=('', ))
    #
    # # 设置为守护线程, 当主线程退出 子线程也退出
    # # t1.setDaemon(True)
    # t2.setDaemon(True)
    #
    # start_time = time.time()
    # t1.start()
    # t2.start()
    #
    # # 在这儿阻塞, 等待线程执行完成之后 执行之后代码
    # t1.join()
    # t2.join()
    #
    # end_time = time.time()
    # # 当主线程退出的时候, 子线程kill掉
    # print('last time {}'.format(end_time-start_time))

    # 类继承方式

    t1 = GetDetailHtml('')
    t2 = GetDetailUrl('')

    start_time = time.time()
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    end_time = time.time()
    print('last time {}'.format(end_time-start_time))