# encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: timer.py
@time: 2018/6/28 17:22
@desc:
'''
import threading
def func():
    print('a')
timer = threading.Timer(5, func)
timer.start()
