# encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: standardLibrary_fileoperation.py
@time: 2018/7/6 17:01
@desc:
'''
import  os,sys


f = open('./test.txt', 'a+')
# f.write("hhhh  ddd")
f.flush()
# print(f.read())
print(f.readline())
print(f.readline())
f.close() #

print(sys.path)

