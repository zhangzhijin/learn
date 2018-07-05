# encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: event.py
@time: 2018/6/28 17:16
@desc:
'''
import threading,time
e=threading.Event()
def fun1(arvg):
    print('start '+arvg)
    e.wait();
    print('continue ' + arvg)

t1=threading.Thread(target=fun1,args={'A',})
t1.start()
time.sleep(2)
print('main……')
e.set()