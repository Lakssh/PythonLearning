# 1 Comparators
# comparators returns the boolean value True or False
# == --> Value equality
# != --> Not equal
# <  --> less than
# >  --> greater than
# <= --> less than or equal
# >= --> greater than or equal
#

# 2 Boolean Operators
# Boolean Operators returns the boolean value True or False
# and  --> Returns True if both the values are True
# or   --> Returns True if one of the value is True
# not  --> Not True is False
#          Not False is True
# Order of precedence - not , and , or


# 3 Conditional Logic
# if(); , elif(): , else:

if 100 < 10:
    print("100 is greater then 10")  # indentation by multiple of 4 spaces
else:
    print("100 is lesser than 10")

value = "Green"

if value == 'Green':
    print("Go!!!")
elif value == 'Orange':
    print("Prepare to Stop")
else:
    print("Stop!!!")

# 4 Looping - While
# Execute statements repeatedly and conditions used to stop the execution of loops
# Iterable items are strings , lists , tuple , dictionary
# while <condition> :
# break - To break out of the  closest enclosing loop
# continue - Go to the start of the closest enclosing loop
# else : executed when the while condition is false and change can be noticed when a break statement is used where else will not be executed

x = 0
while x < 10:
    print("value of x is : " + str(x))
    x = x + 1
    # if(x==8):
    #     break
    print("*" * 20)
else:
    print("came out of the While condition")

    # Iterate and update a list
num_list = []
num = 0
while num < 10:
    num_list.append(num)
    num += 1
print("Updated List is : ", num_list)

# 5 Looping - For

print("------------------******************* FOR LOOP **********************-------------------")

my_string = "abcabcabc"

for char in my_string:
    if (char == 'a'):
        print(char.upper(), end=" ")
    else:
        print(char, end=" ")
print()

# For loop in List
cars = ['bmw', 'honda', 'benz', 'maruti', 'Hyundai']
for car in cars:
    print(car, end="   ")
print()

# For loop in Dictionary
d = {'one': 1, 'two': 2, 'three': 3}
for k in d:  # returns the key of the dictionary
    print(k + " = " + str(d[k]))

for k, v in d.items():  # returns both the keys and values
    print("Key is", k)
    print("Value is", v)

    # Iterate Multiple list using zip function
    # zip - built in function and creates a pair for the shortest list value. can handle more than 2 lists
l1 = [1, 2, 3, 4]
l2 = [5, 6, 0, 8, 9, 10, 11]
for a, b in zip(l1, l2):
    if (a > b):
        print('value from first list : ', a)
    else:
        print('value from second list : ', b)

    # Range function in For Loop
    # range - built in function , helps to create sequence of numbers and doesnt save in memory
    # useful for generating numbers
    # range( <inclusive starting point> , <exclusive end point> ,<steps to skip> )
a = range(0, 10)
print(a)
print(type(a))
print(list(a))

for num in range(0, 10, 2):
    print("number from range is : ", num)
