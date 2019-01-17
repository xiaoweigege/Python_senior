# Semaphore 是用于控制进入数量的锁
# 文件, 读和写 , 写一般只是用于一个线程写, 读可以允许有多个
# 爬虫的时候限制并发数量
import time
from threading import Thread, Semaphore


class HtmlSpider(Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print('get html text success, {}'.format(self.url))
        self.sem.release()


class UrlProducer(Thread):

    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for page in range(20):
            self.sem.acquire()
            url = 'https://www.baidu.com/{}'.format(page)
            html_thread = HtmlSpider(url, self.sem)
            html_thread.start()


if __name__ == '__main__':
    sem = Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()