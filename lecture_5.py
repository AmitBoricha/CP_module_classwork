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

lst1 = [3,7,6,8,"a",9,11,15,25]
lst2 = []
lst3 = []
for i in lst1:
    lst2.append(i**2)

print(lst2)


#excercise 4

lst1 = [3,7,6,8,"a",9,11,15,25]

for i in lst1:
    if type(i) == str:
        raise Exception( i + " was a string, not an integer")
    else:
        lst3.append(i ** 2)

print(lst3)





