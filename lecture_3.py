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

for i in vowels:
    if i in user_string:
        user_string.replace(i,"")

# print(''.join([l for l in user_string if l not in vowels]))

print(user_string)





##C++
"""
#include <iostream>
using namespace std;

int test1() {
    int x,y,z,prod,avg;
    cout << "Type a number: ";
    cin >> x;
    cout << "Type another number: ";
    cin >> y;
    cout << "Type another number: ";
    cin >> z;
    prod = x*y*z;
    avg = (x+y+z)/3;
    cout << "prod is: " << prod;
    cout << "\nAvg is: " << avg;
    return 0;
}


int test2() {
    int a,b,sum;
    cout << "\nType a number: ";
    cin >> a;
    cout << "Type another number: ";
    cin >> b;
    sum = a+b;
    cout << "sum is: " << sum;
    return 0;
}


int main()
{
   test1();
   test2();
   return 0;
}







"""