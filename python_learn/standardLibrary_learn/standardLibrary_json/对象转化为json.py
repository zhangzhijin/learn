# encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: 对象转化为json.py
@time: 2018/6/28 14:09
@desc:
'''
import  json
class person(object):
    def __init__(self,name,age,sex):
        self.name=name;
        self.age=age
        self.sex=sex
    def fun1(self,sex):
        pass

p=person('zhangsan',22,'m')
p_s=json.dumps(p,default=lambda obj:obj.__dict__)
print(p_s)
