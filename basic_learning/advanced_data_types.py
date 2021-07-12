"""
Data Type to store more than one value in a variable name
List        - Sequenced , Mutable data in Square brackets separated by comma starts with index 0
            - Built in methods :len(returns the number of items in the list,
                            append (Add a value at the end of the list),
                            insert(insert a value in the provided index),
                            index (returns the index of the provided value) ,
                            pop(returns & removes the last list) ,
                            remove (remove items from the list by providing the value)
                            slicing - [<inclusive starting index> : <Exclusive end index> : <indices/ steps to skip> ]
                            sort (sorts alphabetically and no return)
                            count (to identify the no of times a value is repeated in the list)
Dictionary  - Mutable Data Type to store than one value in a variable , interms of key value pairs
            - are in curly braces {}  in key : value pairs separated by commas,
            - Not sequenced , no indexing
            - Built in methods :    keys (Returns the list of keys in the dictionary)
                                    values (Returns the list of values in the dictionary)
                                    items (returns keys nd values in the dictionary in a Tuple)
                                    copy (copy one dictionary to the other)
                                    clear (clears the dictionary)
                                    pop (removes the specified key and the value)
Tuple       - Immutable data (cannot change) in paranthesis (separated by comma starts with index 0)
            - Built in Methods : index (returns the index of the provided value)
                                 count (to identify the no of times a value is repeated in the tuple)
                                 slicing - same as list


"""
print("*#" * 20)
print("List")
print("*#" * 20)
cars = ["bmw", "honda", "vauxhall"]
empty_list = []
num_list = [1, 2, 3]
print("Cars list : ", cars)
print("Empty list is : ", empty_list)
print("cars with index : " + cars[2])
print("Sum of lists : ", num_list[0] + num_list[1] + num_list[2])
# Can Assign value to a certain index
cars[1] = "benz"
print("updated cars list: ", cars)
# List built in Methods
print("Length of list is : ", len(cars))
cars.append("Audi")
cars.insert(1, "Tesla")
print(cars)
print("Index of the car Audi is : ", cars.index("Audi"))
updated_cars = cars[0: len(cars): 2]
print("updated cars using slicing is : ", updated_cars)
# Reverse the lists
reverse_cars = cars[::-1]
print("reversed cars are : ", reverse_cars)

print("*#" * 20)
print("Dictionary")
print("*#" * 20)
cars_dict = {"Model": "BMW", "Year": "2020", "Make": "German"}
print(cars_dict)
print("Access Dictionary : ", cars_dict['Year'])
empty_dictionary = {}
empty_dictionary["value1"] = "Test Value"
print(empty_dictionary)

print("*#" * 20)
print("Nested Dictionary")
print("*#" * 20)
cars_nested = {"bmw": {"Model": "550i", "Year": 2020}, "audi": {"Model": "A3", "Year": 2022}}
print(cars_nested)
car = "audi"
print("Nested car value is : ", cars_nested[car]['Year'])
print(cars_dict.keys(), cars_nested.keys())

print("*#" * 20)
print("Tuple")
print("*#" * 20)
my_tuple = (1, 2, 3, 4, 5, 1, 1, 1, 2, "India")
print(type(my_tuple))
print(my_tuple.count(1))
print(my_tuple.index("India"))
