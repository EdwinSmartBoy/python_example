# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  HelloWorld
-----------------------------------------
  File Name    :  regular
  Description  :
  Author       :  Edwin
  Date         :  2018/1/6 9:17
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/6 9:17
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

import re


def reg_telephone(telephone):
    re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
    result = re_telephone.match(telephone).groups()
    print(result)


def reg_email(email):
    re_email = re.compile(r'^([\w.]*)@([\w]*)\.(cn|com)$')
    result = re_email.match(email)
    if result:
        print(result.groups())
        return True
    else:
        return False


if __name__ == '__main__':
    assert reg_email('someone@gmail.com')
    assert reg_email('bill.gates@microsoft.com')
    assert not reg_email('bob#example.com')
    assert not reg_email('mr-bob@example.com')
