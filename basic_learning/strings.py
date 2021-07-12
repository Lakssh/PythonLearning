"""
Example of how string works
Sequence of characters a-z , 0-9 ,@
on single or double quotes
"""

a = "A Simple String"
b = 'String using Single quotes'
print(type(a) , a)
print(type(b) , b)
c ="use single 'quotes' within the string"
d = 'use double "quotes" within the string'
print(c ,d)

# Another way usage of escape sequence \ - says ignore the functionality of the immediate character which is double quotes here

c ='use single \'quotes\' within the string'
d = "use double \"quotes\" within the string"

print(c ,d)

# String Built in methods
print("*******************String Built in Methods*********************")
# Access characters within String
# Index starts from 0 in python
a = "This is my String"
print(a[1])
"""
len() - includes space in between
lower()
upper()
str()
split() - returns a list
"""
print(a.upper())
print(a.lower())
print(len(a))
print(a + str(2))
# concatenation
print("Hello"+ " " +"World")
# replace string
b = "1abc2abc3abc4abc"
print("replaced string is : " , b.replace("abc","xyz"))
print("replaced string using count is : " , b.replace("abc","xyz",2))
# Substring
# Starting index is inclusive , ending index is exclusive
print(b[1])
print("Substring of a range : ",b[1:6]) # substring with a range
print("Substring of a range with Skip steps : ",b[1:6:2]) # no of steps to skip the character in between
print(a[:])
print(a[1:])
print(a[:6])
# Negative index starts from reverse
print("Negative index is : " , a [-1])
print("reverse string is : " , a[::-1]) # skip step should be the negative one

# String formatting using %s and +
city = 'London'
event ='Magic show'
print("Welcome to " +city+ " and enjoy the "+event)
print("Welcome to %s and enjoy the %s" %(city,event))

# Split a string
string = "one two three"
print(type(string.split()))