import socket

# 创建客户端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接

client.connect(('127.0.0.1', 8000))


while True:
    send_data = input('请发送:')
    client.send(send_data.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))

# 关闭连接
client.close()
