# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  HelloWorld
-----------------------------------------
  File Name    :  date
  Description  :
  Author       :  Edwin
  Date         :  2018/1/6 11:29
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/6 11:29
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

from datetime import datetime, timedelta, timezone
import re
from collections import Counter


# dt_str 时间
def to_timestamp(dt_str, tz_str):
    regular = re.compile(r'^UTC([+|-][0-2]?[0-9]):00$')
    result = regular.match(tz_str)
    assert result, "您输入的时区格式有问题，请重新输入"
    time_zone = result.group(1)
    date = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz_date = date.replace(tzinfo=timezone(timedelta(hours=int(time_zone))))
    print(tz_date.timestamp())


def counter(string):
    c = Counter(string)
    print(c)
    for item in c.items():
        print(item)


if __name__ == '__main__':
    counter('programming')
