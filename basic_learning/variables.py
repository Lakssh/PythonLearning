
"""1. Objects and References"""

a="London"
b="London"
print(a)
a =123
b =123
#Now the reference London will be sent to garbage collection
print(a)
print(b)
print(a==b)
print (a is b)

print("*******************************")

"""
2. variables Rules
- Starts with letter or underscore
- dont start with a number
- No special characters
- No Keywords
- can have letter , number , underscore
"""

import keyword # List of keywords in python
print(keyword.kwlist)
a=b=c=10
print(a ,b ,c)
x,y,z=10,20,30
print(x,y,z)

print("*******************************")

"""
3. Numbers and Data Types
"""
int_num=10
float_num =10.00
print(type(int_num))
print(type(float_num))
# Exponentiation
print(10**10)
# Remainder / Modulo
print(10%4)
# Order of precedence - BODMAS
print(2+4*3/2)
a=10
a+=10
print("After Addition",a)
a-=10
print("After Subtraction",a)
a*=10
print("After Multiplication",a)
a/=10
print("After division",a)

# Boolean
print("*********Boolean*******")
print(bool(0))
print(bool(1))