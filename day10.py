
'''
assert is debugging statement used to test whether a condition is true
assert error
'''
num = 10
assert num > 5
print("true")

age = 10 
assert age >=18,"age must be greater than or equal to 18"
print("Eligible")
'''
function ()
a function is a block of code which only execute when it is called
....> you can pass data,known as parameters into a function
to avoid repeated lines in code.

def function_name(parameters):
    ..................
    ..................
function_name(arguments)
'''

num = 9
def even():
    pass
even(num)
    
num = 9
def even(num):
    if num % 2 == 0:
       print(f"{num} even"}
    else:
        print(f"{num}odd")
even (num)
even (109)

num = 9
def even(num,num_2,num_3):
    if num % 2 == 0:
       print(f"{num} even"}
    else:
        print(f"{num}odd")
even (num)
even (109)

ways to pass aruguments
------------------------
1.required arguments
------------------------
2.A function a must be called with the same number of arguments as the parameters.

2.default arguments
---------------------
By default,values is defined at parameters even tho it will take from arguments
key word arguments
--------------------
we can send arguments with key=value syntax.by this,the order of arguments does not matter...
def even(name = "teja", age = 89,sal = 10):
    print(name)
    print(age)
    print(sal)
even("Garikipati",age =89,sal = 75000)

variable length arguments
-------------------------
adding a star (*)before the parameter name in the function, receive a tuple of arguments and can access items with indexes
'''
def even(*name):
    print(name[1])
even("garikapati","teja","chowdary","sony")    

def even(*name):
    print(name[1])
even("garikapati","teja","chowdary","sony")    

name = "teja"
def even(any):
    print(any)
even(name)    
