"""
https://docs.python.org/3/library/
"""

import math             # importing a complete built in module
from math import sqrt   # importing a specific method in a module
import basic_learning.object_oriented_programming as ext    #importing a complete file external to python library and within our framework
from basic_learning.exercise_tax_calculation import calculate_tax

class ModulesDemo():

    def builtin_module(self,a):
        print("Square root using parent module import is : " ,math.sqrt(a))
        print("Square root using method import is : " , sqrt(a))

    def external_module(self):
        ext.Audi
        calculate_tax("London" , 20000)

m = ModulesDemo()
m.builtin_module(10000)
m.external_module()