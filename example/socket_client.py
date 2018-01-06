# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  python_example
-----------------------------------------
  File Name    :  socket_demo
  Description  :
  Author       :  Edwin
  Date         :  2018/1/6 22:57
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/6 22:57
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

import socket

if __name__ == '__main__':
    # 创建一个socket:  IPV4 socket.AF_INET  SOCK_STREAM指定使用面向流的TCP协议
    s = socket.socket()
    # 建立连接:
    s.connect(('www.sina.com.cn', 80))
    # 发送数据: 要求返回首页内容
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    # 接收新浪服务器返回的数据：
    buffer = []
    # 每次最多接收1k字节:
    while True:
        data = s.recv(1024)
        if data:
            buffer.append(data)
        else:
            break
    data = b''.join(buffer)
    print(data)
    s.close()
    # 把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    with open(r'C:\Users\Edwin\Desktop\sina.html', 'wb') as f:
        f.write(html)
