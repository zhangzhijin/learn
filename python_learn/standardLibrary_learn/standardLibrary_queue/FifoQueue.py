# encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: queue.py
@time: 2018/7/3 17:14
@desc:
'''
import queue
q=queue.Queue(5)
print(q.qsize()) # queue size
for i in range(5):
     q.put(i)
print(q.qsize())
print(q.full())
while not q.empty():
    print(q.get())
print(q.empty())


