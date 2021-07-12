"""
Create a dictionary cars with 3 keys - make , model , year
Try to access color key and handle the exception
"""


def exception_handling(key):

    cars = {"bmw":{"year": 2020, "color": "Blue"},"audi" : {"year":'2010',"color": "Red"}}
    try:
        print(cars["audi"][key])
        print(type(cars["audi"][key]))
    except KeyError:
        print ("Key is not available in the dictionary")


exception_handling("test")
exception_handling("color")