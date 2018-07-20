# encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: basenumpy.py
@time: 2018/7/19 8:24
@desc:
'''
import  numpy
# a=[1,2,3,4]
# b=numpy.array(a)
# print(b)
# print(b.size)
# print(b.ndim)
# print(b.dtype)
# print(b.shape)

# b=numpy.ones([10,10])
# # print(b)
# c=numpy.zeros([10,10])
# print(c)
# a=[1,2]
# b=[3,4]
# c=[5,6]
# d=numpy.array([a,b,c])
# print(d)
#
# d=numpy.array(c) #深拷贝
# e=numpy.asarray(c) #浅拷贝
# print(e)

# a=numpy.random.rand(10, 10) #创建指定形状(示例为10行10列)的数组(范围在0至1之间)
# b=numpy.random.uniform(0, 100) #创建指定范围内(0~100)的一个数
# c=numpy.random.randint(0, 10) #创建指定范围内(0~10)的一个整数
# print(c)

# a=numpy.random.normal(1.75, 0.1, (2, 3))#给定均值/标准差/维度(2行3列)的正态分布
# print(a)
# b=a.reshape([1,6])
# print(b)


# a=[1,2]
# b=[3,4]
# c=[5,6]
#
# a1=[1,1]
# a2=[2,2]
# a3=[3,3]
# d=numpy.array([a,b,c])
# d1=numpy.array([a1,a2,a3])
# e=numpy.where(d>3,0,d)
# f=numpy.amax(d,axis=1) #指定轴最小值;axis=0/1; 0表示列1表示行
# g=numpy.amin(d,axis=1) #指定轴最小值;axis=0/1; 0表示列1表示行
# h=numpy.mean(d,axis=1) #指定轴平均值;axis=0/1; 0表示列1表示行
# i=numpy.std(d,axis=1) #指定轴方差;axis=0/1; 0表示列1表示行
# print(d1+d)


# a=[1,2]
# b=[3,4]
# c=[5,6]
# a1=[1,1]
# a2=[2,2]
# d=numpy.array([a,b,c])
# d1=numpy.array([a1,a2])
#
# e=numpy.dot(d,d1)
# print(d)
# print()
# print(d1)
# print()
# print(e)
# v1=[[1,2,3],[4,5,6]]
# v2=[[1,2,3],[4,5,6]]
# a=numpy.vstack((v1,v2)) #矩阵的垂直拼接
# b=numpy.hstack((v1,v2)) #矩阵的水平拼接
# print(b)

# a=numpy.genfromtxt('D:\Users\fandalong341\Downloads\a.txt',dtype=float,comments=',',encoding='utf-8')
# print(a)

# a=numpy.array([[1,2,3],[4,5,6]])
# # print(a.shape)
# # print(a.ndim)
# print(a)
# print(a.itemsize)
# print(a.flags)

# a = numpy.empty([3,2], dtype =  int)
# print(a)

# list=[1,2,3]
# it=iter(list)
# a=numpy.fromiter(it,dtype=float)
# print(a)

# a=numpy.arange(0,4,1,dtype=int)
# print(a)

# a=numpy.linspace(10,20,6)
# print(a)
# a=numpy.logspace(1,20,10)
# print(a)

# a=numpy.arange(10)
# print(a)
# s=slice(2,5,2)
# b=a[s]
# print(b)

# a=numpy.arange(10)
# b=a[2:5:2]
# print(b)

# a=numpy.arange(10)
# b=a[2]
# print(b)

# a = numpy.array([[1,2,3],[3,4,5],[4,5,6]])
# print(a)
# print('\n')
# print('第二列的元素是：')
# print (a[...,1] )
# print('\n')
# print('第二行的元素是：')
# print(a[1,...])
# print('\n')
# print('第二列及其剩余元素是：')
# print (a[...,1:])


# x = numpy.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
# rows = numpy.array([[0,0],[3,3]])
# cols = numpy.array([[0,2],[0,2]])
# y = x[rows,cols]
# # print(y)
# print(x)
# print()
# print(x[1:2,1:2])

# a=numpy.array([[1,2,3],[4,5,6]])
# b=numpy.nditer(a)
# for i in b:
#  print(i)
# a=numpy.array([1,2,3])
# c=a.ravel()
# print(c)


# a=numpy.array([[1,2,3],[4,5,6]])
# b=numpy.transpose(a)
# c=a.T
# print(b)
# print()
# print(c)
# a=numpy.array([[1,2,3],[4,5,6]])
# b=numpy.array([[1,2,3],[4,5,6]])
# c=numpy.concatenate((a, b), axis=0)
# print(c)

# a=numpy.array([[1,2,3],[4,5,6]])
# print(a)
# b=numpy.insert(a,0,[7,8,9],axis=0)
# print(b)
# c=numpy.delete(b,1,axis=0)
# print()
# print(c)

# a=numpy.array([1,1,2,3])
# b=numpy.unique(a)
# print(b)
#
# a = numpy.array([10,10,10])
# b = numpy.array([10,10,10])
# c=numpy.add(a,b)
# print(c)
# d=numpy.subtract(a,b)
# print(d)
# e=numpy.multiply(a,b)
# print(e)
# f=numpy.divide(a,b)
# print(f)
# g=numpy.reciprocal(a)
# print(g)

# a = numpy.array([10,11,10])
# b=numpy.amax(a,axis=0)
# print(a)


# a = numpy.array([[3,7],[9,1]])
# b=numpy.sort(a,axis=0)
# print(b)

# a = numpy.array([[3,7],[9,1]])
# print(a)
# print(id(a))
# print()
# b=a
# print(id(b))


# a = numpy.array([[3,7],[9,1]])
# print(id(a))
# print()
# b=a.copy()
# print(id(b))

import numpy.matlib
# a=numpy.matlib.empty((2,3))
# print(a)


# a=numpy.matlib.zeros((2,3))
# print(a)

# a=numpy.matlib.rand((2,3))
# print(a)

# import numpy.linalg
# import numpy
# a=numpy.array([1,2,3],[1,2,3])
# b=numpy.array([1,2],[1,2],[1,2])
# c=numpy.dot(a,b)
# print(c)
# import numpy
# a=numpy.array([1,2,3])
# numpy.save('a_file.npy',a)
# b=numpy.load('a_file.npy')
# print(b)

a=numpy.array([1,2,3])
numpy.savetxt('a_file.txt',a)
b=numpy.loadtxt('a_file.txt')
print(b)