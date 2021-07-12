
# 1.Get Python Version
import sys
print(sys.version)
print(sys.version_info)

# 2.Get System Data and Time
import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S"))

# 3.Area of a circle
from math import pi
radius = 5
area = 3.14*radius**2
area1 = pi*radius**2
print("Area for radius ", radius, " is : ", area , " and ", area1)

# 4.accepts the user's first and last name and print them in reverse order with a tab between them
#first_name = input("Enter First Name")
#last_name = input("Enter Last Name")
first_name = "Lakshmanan"
last_name = "Chellappan"
print("reversed name is : " , last_name , "\t" ,first_name)

# 5.Reverse a string
string = "TAMIL"
print("Reversed string of ",string," is : ",string[::-1])

# 6. Convert comma separated string to List and Tuple
data= "1,2,3,4,5"
list_variable= data.split(",")
print("list of comma seperated string is : " , list_variable)
print("tuple of comma seperated string is : ", tuple(data.split(",")))

# 7. Print file extension
file_name="Sample.txt"
file_extension = file_name.split(".")
print("File Extension is : " , repr(file_extension[-1]))   # repr returns the string representation

# 8. Print first and last members from the list
list = ["Data","Structure","is","an","interesting","topic"]
print("first member of the list is : ", list[0])
print("last member of the list is : ", list[len(list)-1])   # or simplest way - list[-1]

# 9. tuple to String with formatting
schedule= (10,12,2021)
print("Examination will start from : ",schedule[0]," /",schedule[1], " /",schedule[2])
print("Examination will start from : %i / %i / %i" %schedule)

# 10. get the syntax and description of python built in functions
print("Syntax to get the documentation of python inbuilt function : ",abs.__doc__)
print("Absolute value of -2.45 is : ",abs(-2.45))

# 11. Print calendar of a given month and year
import calendar
print(calendar.month(2021,10))



