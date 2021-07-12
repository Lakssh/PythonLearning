"""
Object Oriented Programming
"""""

print("*****" * 10 + " Creation of class and instantiation " + "*****" * 10)


class Car(object):  # Class name always starts with Caps

    wheels = 4  # member variables

    def __init__(self, make,
                 model="550i"):  # init method to initialise and pass the attributes to the class. Similar to
        # Similar to constructors in Java
        # Positional attributes with default values can also be created similar to methods
        self.make = make  # Attributes from outside class is passed on to the class and accessed , basically instance variables
        self.model = model
        print("Instance of CAR class is created")

    def car_info(self):
        print("Car Make is  : " + self.make)
        print("car Model is : " + self.model)

    def drive(self):
        print("Car Started.....")

    def stop(self):
        print("Car stopped....")


c1 = Car("bmw", "550z")  # Class Car is instantiated and referenced to c1. And attribute BMW passed on to the class
print(c1.make)  # objects within the class can be accessed after creating the instance as above
c1.car_info()  # more optimized way of doing it

c2 = Car("Audi", "Q3")  # Same Car class instantiated to another variable c2
print(c2.make)
print(c2.model)
c2.car_info()  # optimized way

print("No of Wheels accessed from Member variable is : ", Car.wheels)

# Inheritance
print("*****" * 10 + " Inheritance " + "*****" * 10)

class Bmw(Car):  # create a class and inherit to Car.

    def __init__(self):
        print("Instance of BMW class is created")


bmw = Bmw()
bmw.drive()  # method within the super / parent class can be accessed with the reference for child / derive class
bmw.stop()

# METHOD OVERRIDING
print("*****" * 10 + " Method Overriding " + "*****" * 10)

class Audi(Car):        # Audi inherits Car
    def __init__(self):
        print("Instance of AUDI created")

    def drive(self):
        super().drive()                     # Method in Parent class can also be created using super
        super(Audi,self).drive()            # coding standard to call the method within super class
        print("AUDI Car started.....")      # Method drive from parent class CAR is overridden here

audi = Audi()
audi.drive()