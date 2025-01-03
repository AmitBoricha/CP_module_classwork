#mutability

x = 5
print(id(x))

#create 3 different variable
x = 5
y = 5
z = 5

#checking their ids
print(id(x))   #140733933877816
print(id(y))   #140733933877816
print(id(z))   #140733933877816

#python points to the same memory location for all 3 variables

#if we change the value of x, the id changes
x = 10
print(id(x))    #140734747900632



#datastructure excercises

def create_int_list(n):
    li = []
    for i in range(0,n):
        li.append(i)
    return li

x = create_int_list(10)
print("list x: ", x)

print("maximum number: ",max(x))
print("minimum number: ",min(x))

#write a program that takes list of dict with keys name and age and returns a list of names sorted by age in ascending order
li = [{"name": "a","age":10},{"name": "b","age":20},{"name": "c","age":15}]
def sorted_names_by_age(li):
    ages = []
    names = []
    for i in li:
        print(i)
        ages.append(i['age'])
    ages.sort()
    for x in ages:
        for j in li:
            if x == j['age']:
                names.append(j['name'])
    return names




ascending_names_by_age = sorted_names_by_age(li)
print(ascending_names_by_age)


#excercise3

def termostat_regulator(temp,low_temp = 20,high_temp = 27):
    if type(temp) != int:
        print("Please enter an integer")
        exit()
    if temp < low_temp:
        state = 'Turn on heater'
    elif temp > high_temp:
        state = 'Turn on cooler'
    elif temp >= low_temp and temp <= high_temp:
        state = 'do nothing'
    print(state)
    return state

termostat_regulator(temp=15)



#excercise 4

user_name = input("Whats your name?")

def check_if_bond(user_name):
    user_name = user_name.lower().strip()
    if user_name == "james bond":
        print("We've been expecting you, Mr Bond.")
    else:
        print(f"Access Denied:{user_name}")

check_if_bond(user_name)

#excercise 5

x = input("please enter a number")

if "." in x:
    print(x.split(".")[1])
else:
    print(type(x))


#excercise 6
# password_list = []
# def pass_collector(pass):
#     if len(password_list) == 0:
#         x = input("Please Enter your password: ")
#         if len(x) < 8:
#             x = input("Weak password: too short")
#         list.append(x)


""""
x = input("Please enter password")
if len(x) >= 8:
    upper_case = False
    lower_case = False
    has_digit = False
    for i in x:
        if i.isupper():
            upper_case = True
        if i.islower():
            lower_case = True
        if i.isdigit():
            has_digit = True
    if upper_case == lower_case == has_digit == True:
        print("Strong Password.")
    else:
        print("missing character types")

if len(x) < 8:
    print("Too weak. Please enter a different password.")""""








