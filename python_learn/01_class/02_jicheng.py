class Animal(object):
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        print("I am Animal……")

    def eat(self):
        pass;

    def __del__(self):
        print("Animal 結束")


class People(Animal):
    def __init__(self, name, age, sex):
        Animal.__init__(self, name, age)
        self.sex = sex;
        print("I am people……")


    def getName(self):
        print(self.name)


    def __del__(self):
        print("people 結束")


p = People("zhangsan", 12, "m")
