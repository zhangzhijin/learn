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
import queue,threading
class job(object):
    def __init__(self,name,grade):
        self.name=name;
        self.grade=grade;
    def __cmp__(self,other):
        return cmp(self.grade,other.grade)
    def get_info(self):
        print(self.name)

    def __lt__(self, other):
        return self.grade < other.grade

j1=job('job1',1);
j2=job('job2',2);

q=queue.PriorityQueue()

q.put(j1);
q.put(j2);

def process_job(q):
    while True:
        next_job=q.get();
        next_job.get_info()
        q.task_done()
t=threading.Thread(target=process_job,args=(q,))
t.start();
q.join()
print('end')


