#excercise

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is "+ self.name + " and I am " + str(self.age) + " years old.")

p1 = Person("Amit",32)

print(p1.name)
print(p1.age)
print(p1)
p1.greet()


#excercise2

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area_of_rectangle(self):
        area = self.width * self.height
        return area

    def perimeter_of_rectangle(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

r1 = Rectangle(10,20)

print(r1.area_of_rectangle())
print(r1.perimeter_of_rectangle())


