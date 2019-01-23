# 1. epoll并不代表一定比select好
# 在高并发情况下, 连接活跃度不是很高, epoll比select好
# 并发性不高, 同时连接很活跃, select比epoll好

import socket
from urllib.parse import urlparse


def get_url(url):
    """
    通过socket请求html
    :param url:
    :return:
    """
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置非阻塞
    client.setblocking(False)
    try:
        client.connect((host, 80))
    except BlockingIOError:
        pass
    # http 请求协议
    http_data = "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf-8')
    # 一直循环请求
    while True:
        try:
            client.send(http_data)
            break
        except OSError:
            pass
    data = b''
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError:
            continue
        if d:
            data += d
        else:
            print('break')
            break
    print(data.decode('utf-8'))


if __name__ == '__main__':
    get_url('https://www.baidu.com')