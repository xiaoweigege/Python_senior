import socket
from threading import Thread

def client(sock, addr):
    data = sock.recv(1024)
    print('接收到{}:{}'.format(addr, data.decode('utf-8')))
    # send_data = input('请回复:')
    # sock.send(send_data.encode('utf-8'))


# SOCK_STREAM 指的是TCP SOCK_DGRAM UDP
# 创建socket对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定地址，端口
server.bind(('0.0.0.0', 8000))
# 监听
server.listen(100)


# 获取客户端请求
# 一次获取1K的数据
while True:
    sock, addr = server.accept()
    Thread(target=client, args=(sock, addr)).start()

sock.close()
server.close()

