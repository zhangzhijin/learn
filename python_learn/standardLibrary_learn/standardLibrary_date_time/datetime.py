# encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: datetime.py
@time: 2018/7/4 16:29
@desc:
'''
import datetime
# print(datetime.date.today())

# print(datetime.date.strftime(datetime.date.today(),'%Y-%m-%d %H:%M-%S'))
# print(datetime.date.timetuple(datetime.date.today()))
# print(datetime.datetime.now())
d=datetime.datetime(2014, 8, 15, 8, 12, 34, 790945)
print(d.now())
# print(datetime.datetime.today())
# print(datetime.datetime.strftime(d,'%Y-%m-%d'))
print(d.timetuple())

today = datetime.datetime.today()
d1=datetime.timedelta(days=1)
print(today-d1)