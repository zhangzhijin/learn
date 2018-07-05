# encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: semaphore.py
@time: 2018/6/29 9:00
@desc:
'''

import time
import threading
semophore=threading.Semaphore(5)   #添加一个计数器
def func():
    semophore.acquire()    #计数器获得锁
    time.sleep(2)   #程序休眠2秒
    print("ok",time.ctime())
    semophore.release()    #计数器释放锁

for i in range(20):
    t1=threading.Thread(target=func,args=()) #创建线程
    t1.start()  #启动线程
