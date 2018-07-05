class Dog(object):
    def __init__(self,name,age):
        self.name=name;
        self.age=age;

    def eat(self):
        print("eat a bag^")

    def setName(self,name):
        self.name=name;

    def getName(self):
        print("name:%s"%(self.name))

d=Dog("lis",12);
d.eat();
d.setName("zhangsan")
d.getName();
d1=d
d1.getName()
d1.setName("d1")
d1.getName()
d.getName()
