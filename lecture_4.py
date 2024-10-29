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
def sorted_dict(li):
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


ascending_names_by_age = sorted_dict(li)
print(ascending_names_by_age)








