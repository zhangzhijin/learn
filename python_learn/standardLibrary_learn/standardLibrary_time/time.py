#encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: time.py
@time: 2018/7/3 18:20
@desc:
'''
import time

# print(time.gmtime())
# print(time.localtime())

# print(time.timezone)
# print(time.sleep(5))
# print(time.tzname)
# print(time.process_time())
# print(time.perf_counter())
# print(time.clock())
# print(time.asctime(time.localtime(time.time())))
# print(time.mktime(time.localtime()))
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print( time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X'))