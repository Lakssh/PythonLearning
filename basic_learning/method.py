# 1 method is defined by a keyword called def <method name> :

def sum(a, b):
    print("Sum inside method is : ", a + b)


def sub(a, b):
    return a - b


def multiply(a, b):
    """
   Get product of two numbers
   :param a:
   :param b:
   :return: multiplied value
   """
    return a * b


n1 = 10
n2 = 25
print('-----' * 20)
sum(n1, n2)
print("Subtraction returned from method is : ", sub(n1, n2))
print('Multiplication of value is : ', multiply(100, 40))

print('-----' * 20)


def is_metro(city):
    metro_list = ['London', 'Manchester', 'Glasgow']
    if city in metro_list:
        return True
    else:
        return False


print('Chennai is metro city : ', is_metro('Chennai'))
print('London is metro city : ', is_metro('London'))

# 2 Positional and Optional paramters
# Positional parameters can be assigned a default value, if no value is provided from outside

print('-----' * 20)


def sum_nums(a=10, b=11):
    return a + b


print("Sum using Positional paramters : ", sum_nums(b=100))
print("Sum of values passed using positional paramters :", sum_nums(10, 20))


def sub_nums(a=100, b=50):
    return a - b


print("Subtraction using changed positions : ", sub_nums(b=20, a=50))

# 3 Scope of variables within methods
# Have local scope and cannot be used outside method

a = 10
print("Value of Global 'a' is : ", a)


def change_value(a):
    print("Value of 'a' inside method is : ", a)
    a = 2
    print("value of 'a' after modifying inside method is : ", a)


change_value(a)
print("Global Value of 'a' after calling change value method is : ", a)


def test_method():
    global a
    print("value of 'a' inside new test method using global variable is : ", a)
    a = 2
    print("value of global variable after modifying 'a' is : ", a)


test_method()
print("Global value of 'a' after modification outside test method is : ", a)


# 4 built in methods for integers
# max() - to identify the maximum of arguments and returns largest one
# min() - to identify the minimum of arguments and returns smallest one
# abs() - it returns the absolute value of the number , that's number distance from 0 , always returns a positive value and takes single argument
# type() - returns the type of data
# *args means method can take multiple parameters

def largest_nums(*args):
    print("Largest number is ", max(args))


largest_nums(-10, 20, 100, -200, 500, -1000)
print("Absolute Number of -20 is : ", abs(-20))
print("Absolute Number of 20 is : ", abs(20))
print(type(-99.99))
