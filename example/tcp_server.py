# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  python_example
-----------------------------------------
  File Name    :  socket_server
  Description  :
  Author       :  Edwin
  Date         :  2018/1/6 23:15
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/6 23:15
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

import socket
import time
import threading


def tcp_link(sock, address):
    print('Accept new connection from %s:%s' % (sock, address))
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(5)
        if not data or data.decode('utf-8').upper() == 'EXIT':
            break
        sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed' % (sock, address))


if __name__ == '__main__':
    # 创建socket
    s = socket.socket()
    # 绑定端口和地址
    s.bind(('127.0.0.1', 9999))
    # 监听端口 调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
    s.listen(5)
    print('Waiting for connection...')
    # 采用阻塞的方式来接受客户端的链接，accept()会等待并返回一个客户端的连接:
    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcp_link, args=(sock, addr))
        t.start()
