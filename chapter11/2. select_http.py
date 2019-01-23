import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


# 使用select实现http请求
selector = DefaultSelector()
urls = []
stop = False


class Fetcher(object):

    def readable(self, key):

        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            print(self.data.decode('utf-8'))
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True
            self.client.close()

    def connected(self, key):
        selector.unregister(key.fd)
        http_data = "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(
            self.path, self.host).encode('utf-8')
        self.client.send(http_data)
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.data = b''
        self.host = url.netloc
        self.path = url.path
        if self.path == '':
            self.path = '/'

        # 建立socket链接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError:
            pass

        # 注册
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    # 事件循环,不停的请求socket的状态并调用对应的回调函数 Tronado, gevent
    # 本质上就是 回调 + 事件循环(select/poll/epoll)
    # 1.select 本身不支持register模式,
    # 2.socket状态变化以后的回调是由程序员完成的
    while not stop:

        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)


if __name__ == '__main__':

    for p in range(20):
        url = 'https://www.baidu.com/'
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)
    loop()
