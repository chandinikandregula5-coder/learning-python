'''list comprehension
-------------------
-->lc offers a shortest syntax when we want to create a new list from existing list

'''

'''
old_= [1,2,3,4,5]
new_ = [so if so%2!=0 else "even" for so in old_]
print(new_)
 
generators
--------------
--->generators in python are a special type of itterable ,allowing users to iterate over data efficiently without storing everything in memory...
they generate values lazily using yeild keyword.
why to use generators:generators do not store the entire dataset in memory,the generates values on the fly or runtime.
avoiding unnecesary storage of data speed of execution.
this is also used in pipelines.
how it works
----------
it looks like a normal function but uses the yeild keyword instead of return
when the function is called ,it does not execute immediately.instead ,it return a generator object which can be iterated using loop for or the next() function 

def simple_gen():
    print("start")
    yeild 1
    yeild 2
    yeild 3

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

def any(num):
    for i in range(1, num+1):
        yield i*i
a = any(5)
print(next(a))
print(next(a))
print(next(a))

def sqr(num):
    result = []
    for i in range(1,num+1):
        result.append(i*i)
    return result
print(sqr(7))
'''
so = "quantum computing is an advanced feild of technology that harnesses the laws of quotes "
any = ''
for j in so:
    if j not in "AEIOUaeiou":
        any += j
print(any)        
        














