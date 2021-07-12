"""
Exception Handling
Exceptions are errors and should be handled in the code
link to python built in exceptions https://docs.python.org/3/library/exceptions.html
try: <Function to be written here>
except: <Exception block, same as catch in java>
else: <executed when there is no exception>
finally: <always executed despite of checking exception>
"""


def exception_handling(a,b,c):
    try:
        div = a + b / c
        print("division is : ", div)
    except ZeroDivisionError:
        print("division by zero is not possible")
        raise Exception("Exception Stack Trace")                        # print exception trace
    except TypeError:
        print("Addition of String is not possible")
    except:
        print("Entered into Exception block")
    else:
        print("Executed when there is no exception")
    finally:
        print("Executed always")


print("****"*10+" Happy Path "+"****"*10)
exception_handling(10,10,2)

print("****"*10+" Type Error for String addition "+"****"*10)
exception_handling(10,"String",10)

print("****"*10+" With Zero division error "+"****"*10)
exception_handling(10,10,0)
