class Animal(object):
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        print("I am Animal……")

    def eat(self):
        pass;
    def talk(self,d):
        d.talk();

    def __del__(self):
        print("Animal 結束")


class People(Animal):
    def __init__(self, name, age, sex):
        super(People,self).__init__(name, age)
        self.sex = sex;
        print("I am people init……")

    def talk(self):
        print("I am a people……")
    def getName(self):
        print(self.name)


    def __del__(self):
        print("people 結束")

class Dog(Animal):
    def __init__(self,name,age,color):
        super(Dog,self).__init__(name,age);
        self.color=color;
    def talk(self):
        print("I am a dog……")

p = People("zhangsan", 12, "m")
d = Dog("dog", 12, "red")

a=Animal('','');
a.talk(p);