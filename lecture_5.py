#excercise 1

names_list = ["John","Mary","Tom","garry","Erica"]

def congratulation_wishes(name):
    print("Congratulations "+name+" !")

for name in names_list:
    congratulation_wishes(name)


#Excercise 2

random_string = "asdqwefghzxcvbn"

num_of_characters = len(random_string)

for i in range(0,num_of_characters):
    print(random_string[i])


#Excercise 3

# lst1 = [3,7,6,8,"a",9,11,15,25]
# lst2 = []
# lst3 = []
# for i in lst1:
#     lst2.append(i**2)
#
# print(lst2)


#excercise 4

# lst1 = [3,7,6,8,"a",9,11,15,25]
#
# for i in lst1:
#     if type(i) == str:
#         raise Exception( i + " was a string, not an integer")
#     else:
#         lst3.append(i ** 2)
#
# print(lst3)

#excercise 5

def square(number):
    return number**2

def max_num(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

def calculate_tax(salary):
    if salary <= 20000:
        return 0
    elif salary > 20000 & salary <= 50000:
        return 0.10*salary
    elif salary >50000 & salary <=10000:
        return 0.20 * salary
    else:
        return 0.30 * salary


def reverse_string(string):
    reversed_string = ""
    for i in range(len(string),0):
        reversed_string = reversed_string + string[i]


def find_average(list_of_numbers):
    n = len(list_of_numbers)
    sum = 0
    for i in list_of_numbers:
        sum = sum + i
    avg = sum / n

import requests

def currency_exchange(date):
    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/v1/currencies/eur.json"

    response = requests.get(url)
    data = response.json()
    print(data)

currency_exchange("latest")








