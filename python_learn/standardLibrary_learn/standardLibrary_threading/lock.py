import threading,time

# print(threading.currentThread())
# print(threading.activeCount())
# print(threading.enumerate())
# print(threading.TIMEOUT_MAX)
# 直接调用
ac=0;
l=threading.RLock()
def fun1(arg):
    global ac;
    l.acquire();
    ac=ac+1;
    print(ac)
    l.release()
for i in range(5):
    t=threading.Thread(target=fun1,args=('zhang',))
    t.start()
