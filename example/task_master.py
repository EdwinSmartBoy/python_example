# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  HelloWorld
-----------------------------------------
  File Name    :  task_master
  Description  :
  Author       :  Edwin
  Date         :  2018/1/4 23:25
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/4 23:25
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

import queue
import random
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


def get_task():
    return task_queue


def get_result():
    return result_queue


def start_server():
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    QueueManager.register('get_task_queue', callable=get_task)
    QueueManager.register('get_result_queue', callable=get_result)

    # 绑定端口5000, 设置验证码'abc':
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue:
    manager.start()

    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=30)
        print('Result: %s' % r)

    manager.shutdown()
    print('master exit..')


if __name__ == '__main__':
    start_server()
