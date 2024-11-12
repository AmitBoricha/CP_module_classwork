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


#excercise3

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self,deposit_amt):
        self.balance =+ deposit_amt

    def withdraw(self,withdraw_amt):
        self.balance -= withdraw_amt

    def check_balance(self):
        print("current balance is: ",self.balance)


a1 = BankAccount()
a1.check_balance()
a1.deposit(10000)
a1.check_balance()
a1.withdraw(2000)
a1.check_balance()


#excercise 4

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        print(f"{self.year}, {self.make} {self.model}")


c1 = Car("Mazda","6", 2022)

c1.description()