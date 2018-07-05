# encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: condition.py
@time: 2018/6/28 16:53
@desc:
'''
import threading,time
# 商品
product = None
# 条件变量
con = threading.Condition()

# 生产者方法
def produce():
    global product

    if con.acquire():
        while True:
            if product is None:
                print('product ……')
                product = 'anything'

                # 通知消费者，商品已经生产
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)


# 消费者方法
def consume():
    global product
    if con.acquire():
        while True:
            if product is not None:
                print('consuming')
                product = None
                # 通知生产者，商品已经没了
                con.notify()

            # 等待通知 释放锁
            con.wait()
            time.sleep(2)


t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)
t2.start()
t1.start()
