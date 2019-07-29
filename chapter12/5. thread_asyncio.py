# 使用多线程的原因： 在协程中集成阻塞I/O
import time
import asyncio
import socket
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor


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
    client.connect((host, 80))
    # http 请求协议
    http_data = "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf-8')
    client.send(http_data)
    data = b''
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            print('break')
            break
    time.sleep(2)
    print(data.decode('utf-8'))
    print('-------------')


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor()
    # executor.submit(get_url, 'https://www.baidu.com/')
    # executor.submit(get_url, 'https://www.baidu.com/')
    # executor.submit(get_url, 'https://www.baidu.com/')
    # 可以执行阻塞的IO
    tasks = []
    for _ in range(10):
        task = loop.run_in_executor(executor, get_url, 'https://www.baidu.com/')
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))

    last_time = time.time()
    print(f'耗时: {last_time-start_time}s')