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