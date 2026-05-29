'''
modules
-------
a module in python is a file that contains python  code such as
variables
functions
classes
statements

two types of modules
-------------------
user -define
built-in

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

import math
print(math.sqrt(25))

print(math.factorial(10))
print(math. pow(2,5))

from math import sqrt
print(sqrt(25))

import math as m

print(m.factorial(10))
print(m.pow(2,5))

import os

os.remove("deo.txt")

import sys
print(sys.version)
    
print(sys.path)
print(sys.exit)

import random
print(random.randint(1000,9999))

from collections import Counter,defaultdict
data = ['a','b','c','d']
counter = Counter(data)
print(counter)

dd = defaultdict(int)
dd['missing'] +=1
print(dd['missing'])
print(dd)
