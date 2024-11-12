#excercise1

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is ",self.name)

p1 = Person("Amit",32)

print(p1.name)
print(p1.age)
print(p1)
p1.myfunc()