import threading,time

# print(threading.currentThread())
# print(threading.activeCount())
# print(threading.enumerate())
# print(threading.TIMEOUT_MAX)
#直接调用
# def fun1(arg):
#     print(arg)
# for i in range(5):
#     t=threading.Thread(target=fun1,args=('zhang',))
#     t.start()

#继承threading.Thread 类，覆盖run()方法
class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
        self.arg=arg
    def run(self):#定义每个线程要运行的函数
        time.sleep(1)
        print(self.arg)

for i in range(4):
    t = MyThread(i)
    t.start()





