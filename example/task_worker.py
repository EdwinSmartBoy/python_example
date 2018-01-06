# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  HelloWorld
-----------------------------------------
  File Name    :  task_worker
  Description  :
  Author       :  Edwin
  Date         :  2018/1/4 23:38
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/4 23:38
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

import queue
import time
from multiprocessing.managers import BaseManager


# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass


def start_request():
    # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    # 连接到服务器，也就是运行task_master.py的机器:
    server_add = '127.0.0.1'

    print('Connect to server %s...' % server_add)
    # 端口和验证码注意保持与task_master.py设置的完全一致:
    manager = QueueManager(address=(server_add, 5000), authkey=b'abc')
    # 从网络连接:
    manager.connect()
    # 获取Queue的对象:

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 从task队列取任务,并把结果写入result队列:
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d...' % (n, n))
            r = '%d * %d = %d' % (n + 1, n + 1, (n + 1) * (n + 1))
            time.sleep(5)
            result.put(r)
        except queue.Empty:
            print('task queue is empty!')
    # 处理结果
    print('worker exit..')


if __name__ == '__main__':
    start_request()
