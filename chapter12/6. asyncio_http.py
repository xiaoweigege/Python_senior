# asyncio 中目前没有实现http协议的接口
# 提供的是 TCP UDP 这些低层协议
import time
import asyncio
from urllib.parse import urlparse


async def get_url(url):
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

    # 建立连接
    reader, writer = await asyncio.open_connection(host, 80)
    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # await client.connect((host, 80))
    # http 请求协议
    http_data = "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf-8')
    writer.write(http_data)
    all_lines = list()
    async for line in reader:
        # print(line)
        all_lines.append(line.decode())

    html = ''.join(all_lines)
    return html


async def read_html():
    tasks = [asyncio.ensure_future(get_url('https://www.baidu.com')) for _ in range(40)]
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result, '------')


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.wait(read_html()))

    last_time = time.time()

    print(f'耗时: {last_time-start_time}s')
