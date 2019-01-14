# Python socket 编程
1. 弄懂HTTP、Socket 、TCP 这几个概念
2. client和server实现通信
3. socket实现聊天和多用户连接
4. socket模拟HTTP请求

## 5层网络模型
| OSI 层 | 功能 | TCP/IP协议 |
| ----- | ----- | ----- |
| 应用层| 文件传输、电子邮件、文件服务 | HTTP、FTP、SMTP、DNS、Telnet等 |
| 传输层 | 提供端对端的接口 | TCP、DUP |
| 网络层 | 为数据包选择路由 | IP、ICMP等 |
| 数据链路层| 传输有地址的帧、错误检测功能 | ARP等 |
| 物理层 | 物理媒体 | 1000BASE-SX等 |

## socket理解
socket 可以脱离应用层直接与传输层打交道,甚至自己可以实现一个聊天协议

socket 可以实现自己的一个协议,

## HTTP 协议
其实就是一些请求头

GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n

服务端会将这些请求头进行解包, 进行数据提取,处理

客户端请求:

GET /hello.txt HTTP/1.1

User-Agent: curl/7.16.3 libcurl/7.16.3 OpenSSL/0.9.7l zlib/1.2.3

Host: www.example.com

Accept-Language: en, mi

服务端响应:

HTTP/1.1 200 OK

Date: Mon, 27 Jul 2009 12:28:53 GMT

Server: Apache

Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT

ETag: "34aa387-d-1568eb00"

Accept-Ranges: bytes

Content-Length: 51

Vary: Accept-Encoding

Content-Type: text/plain