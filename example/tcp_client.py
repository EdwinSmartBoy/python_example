# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  python_example
-----------------------------------------
  File Name    :  socket_test
  Description  :
  Author       :  Edwin
  Date         :  2018/1/6 23:30
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/6 23:30
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

import socket

if __name__ == '__main__':
    # 创建socket
    s = socket.socket()
    # 与服务器建立链接
    s.connect(('127.0.0.1', 9999))
    # 接收服务器下发的欢迎消息:
    print(s.recv(1024).decode('utf-8'))
    # 向服务器发送数据
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.send(data)
        # 接收数据
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()
    print("socket close")
