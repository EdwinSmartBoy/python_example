# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  HelloWorld
-----------------------------------------
  File Name    :  file_read_writer
  Description  :
  Author       :  Edwin
  Date         :  2018/1/2 22:58
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/2 22:58
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

from io import StringIO


def file_read():
    with open(r'C:\Users\Edwin\Desktop\test.txt', 'a', encoding='utf-8') as f:
        f.write('Hello, world!\n')


def str_read():
    f = StringIO()
    print(f.write('hello'))
    print(f.write('apple'))
    print(f.getvalue())


if __name__ == '__main__':
    str_read()
