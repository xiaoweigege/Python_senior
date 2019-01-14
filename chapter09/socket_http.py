# requests -> urllib -> socket
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
    print(data.decode('utf-8'))


if __name__ == '__main__':
    get_url('https://www.baidu.com')