# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  HelloWorld
-----------------------------------------
  File Name    :  hello
  Description  :  this is a test Class
  Author       :  Edwin
  Date         :  2018/1/2 21:26
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/2 21:26
  Description  :
-----------------------------------------
"""
__author__ = 'Edwin'

import logging

logging.basicConfig(level=logging.INFO)


class Hello(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        print("Hello : name = %s, age = %s" % (self.__name, self.__age))


def foo(s):
    n = int(s)
    logging.info('n = %d' % n)
    return 10 / n


if __name__ == '__main__':
    foo('0')
