# encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: basematplotlib.py
@time: 2018/7/20 10:12
@desc:
'''
import matplotlib
import  matplotlib.pyplot
# x=[1,2,3,4]
# y=[1,2,3,5]
# matplotlib.pyplot.plot(x,y)
# matplotlib.pyplot.show()

# x=[1,2,3,4]
# y=[1,2,3,5]
# x1=[10,11,12,19]
# y1=[3,4,5,59]
# matplotlib.pyplot.plot(x,y,'r.--')
# matplotlib.pyplot.plot(x1,y1)
# matplotlib.pyplot.xlabel('m')
# matplotlib.pyplot.ylabel('rmb')
# matplotlib.pyplot.title('title')
# matplotlib.pyplot.show()

#
# x=[1,2,3,4]
# y=[1,2,3,5]
# x1=[3,4,6,1]
# y1=[3,4,5,9]
# matplotlib.pyplot.subplot(2,1,1)
# matplotlib.pyplot.title('title1')
# matplotlib.pyplot.xlabel('m')
# matplotlib.pyplot.ylabel('rmb')
# matplotlib.pyplot.plot(x,y,)
# matplotlib.pyplot.axis([0,10,0,10])
#
# matplotlib.pyplot.subplot(2,1,2)
# matplotlib.pyplot.title('title2')
# matplotlib.pyplot.plot(x1,y1)
# matplotlib.pyplot.xlabel('m')
# matplotlib.pyplot.ylabel('rmb')
# matplotlib.pyplot.show()


#
# x=[1,2,3,4]
# y=[1,2,3,5]
# x1=[3,4,6,1]
# y1=[3,4,5,9]
# matplotlib.pyplot.figure(1)
# matplotlib.pyplot.title('title1')
# matplotlib.pyplot.xlabel('m')
# matplotlib.pyplot.ylabel('rmb')
# matplotlib.pyplot.plot(x,y,)
# matplotlib.pyplot.axis([0,10,0,10])
#
# matplotlib.pyplot.figure(2)
# matplotlib.pyplot.title('title2')
# matplotlib.pyplot.plot(x1,y1)
# matplotlib.pyplot.xlabel('m')
# matplotlib.pyplot.ylabel('rmb')
# matplotlib.pyplot.show()

#
# x=[1,2,3,4]
# y=[1,2,3,5]
# x1=[0.1,0.4,0.2,0.1]
# y1=[0.3,0.3,0.2,0.3]
# fig=matplotlib.pyplot.figure(1)
# axe1=fig.add_axes([0.2,0.1,0.8,0.8]) #left bottom width heigh
# axe1.set_xlabel("x")
# axe1.set_ylabel("y")
# axe1.set_title("big")
# axe1.legend(loc=2)
# axe1.plot(x,y)
#
# axe2=fig.add_axes([0.3,0.5,0.3,0.3]) #left bottom width heigh
# axe2.set_xlabel("x1")
# axe2.set_ylabel("y1")
# axe2.set_title("big1")
# axe2.plot(x1,y1)
# matplotlib.pyplot.show()


x=[1,2,3,4]
y=[1,2,3,5]
x1=[0.1,0.4,0.2,0.1]
y1=[0.3,0.3,0.2,0.3]
fig=matplotlib.pyplot.figure(1)
axe1=fig.add_axes([0.2,0.1,0.8,0.8]) #left bottom width heigh
axe1.set_xlabel("x")
axe1.set_ylabel("y")
axe1.set_title("big")
axe1.plot(x,y,label='y=x')
axe1.plot(x1,y1,label='y1=x1')
axe1.legend(loc=2)
matplotlib.pyplot.show()