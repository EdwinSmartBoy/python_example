# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  HelloWorld
-----------------------------------------
  File Name    :  url_libs
  Description  :
  Author       :  Edwin
  Date         :  2018/1/6 20:27
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/6 20:27
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

from urllib import request
import json


def fetch_data(url):
    with request.urlopen(url) as f:
        result = f.read()
        person = json.loads(result.decode('utf-8'))
        print('Data', person)
        assert person['query']['results']['channel']['location']['city'] == 'Beijing'
        print('Data', 'ok')


if __name__ == '__main__':
            fetch_data(
                'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
