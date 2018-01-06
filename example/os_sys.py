# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  HelloWorld
-----------------------------------------
  File Name    :  os_sys
  Description  :
  Author       :  Edwin
  Date         :  2018/1/3 23:02
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/3 23:02
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

import json

if __name__ == '__main__':
    obj = dict(name='小明', age=20)
    s = json.dumps(obj, ensure_ascii=True)
    print(s)
