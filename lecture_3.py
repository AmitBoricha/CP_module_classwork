def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        return "error: cant divide by 0"
    return a / b


def power(a, b):
    return a ** b


def modulo(a, b):
    return a % b


print(multiply(10, 5))

print(subtract(6, 3))

print(multiply(68.75, 0))

print(divide(100, 7))

print(divide(100, 0))

print(modulo(100, 7))

print(power(2, 3))

x = 5
y = 3

print(multiply(x, y))

# print(X for X in [10,5,6] if X % 2 == 0)

# name =input( "What is your name?")
# print(name)


X = 10
Y = 15

# if X > Y:
#     print(True)
# else:
#     print(False)

print(X > Y)

A = "asdqwe"
B = "wenfwfe"

if A == B:
    print("THey are same")

if A != B:
    print("THey are not same")


# datatypes
#1
user_string = input("Please enter a string:")

print("Number of characters in given string: ",len(user_string))

#2
int_x = int(input("Enter x int value:"))

int_y = int(input("Enter y int value: "))

print("Addition of two integer is:",int_x+int_y )

vowels = ["a","e","i","o","u"]

print(''.join([x for x in user_string if x not in vowels]))