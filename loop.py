# While loop

i = int(input("Enter the value of i : "))
if i<38:
    i=int(input("Enter the value of i : "))
    print(i)
if i>38 :
    print(input("Enter the smaller value of i : "))
else  :
    print("Done with the loop.")

# Star Pyramid

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    # spaces
    for j in range(rows - i):
        print(" ", end="")
    
    # stars
    for k in range(2 * i - 1):
        print("*", end="")
    
    print()

for i in range(1, 11) :
    if i==5:
        continue;
    print("9 * ", i, "=", 9*i)

for i in range(1, 11) :
    if i==5:
        break;
    print("9 * ", i, "=", 9*i)

def multiply(a1,a2):
    return a1*a2

print(multiply(8,5))
print(multiply(2,"a"))


def multiply(a1,a2):
    print(a1*a2)

print(multiply(8,5))
print(multiply(2,"a"))


def print_name(name):
    print("Hello, "+ name + "!")

user_name= input("Enter your name : ")
print_name(user_name)

def print_age(age):
    print("Your age is " + age)

age = input("Enter your age : ")
print_age(age)

my_list = [1, 2, 3, 4, 5]
print(my_list)

my_tuple = (10, 20, 30)
print(my_tuple)
my_set = {1, 2, 3, 3, 4}
print(my_set)
my_dict = {"name": "Avdesh",  "age": 18, "course": "BTech"}
print(my_dict["name"]) 

def multiply(a1,a2):
    return a1*a2

print(multiply(8,5))
print(multiply(2,"a"))