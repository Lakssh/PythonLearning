
class Fruits(object):
    def __init__(self):
        print("Fruits class instantiated")

    def nutrition(self):
        print("Fruits Nutrition is called")

    def fruit_shape(self):
        print("Fruits shape is spherical")

class Strawberry(Fruits):
    def __init__(self):
        Fruits.__init__(self)
        print("Strawberry fruit is instantiated")

    def nutrition(self):
        super(Strawberry ,self).nutrition()
        print("Strawberry is vitamin rich")

    def color(self):
        print("Color of the fruit is red")

print("**** " *20 +" From child class and inherited from parent class " + "****" * 20)

s = Strawberry()
s.nutrition()
s.color()
s.fruit_shape()

print("****" * 20 + " From Parent class " + "****" * 20)

f = Fruits()
f.nutrition()
f.fruit_shape()
