# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  HelloWorld
-----------------------------------------
  File Name    :  iterator
  Description  :
  Author       :  Edwin
  Date         :  2018/1/6 16:55
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/6 16:55
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

import time
import itertools


def count():
    iterator = itertools.repeat('hexiaomei', 10)
    for value in iterator:
        time.sleep(1)
        print(value)


def step(c):
    return c.upper()


def take():
    for key, group in itertools.groupby('AAAaaaBBBbbbCCccAAAaa', step):
        print(key, list(group))


if __name__ == '__main__':
    take()
