'''
sets
a set is a collection of unique and unordered elements
duplicate values are not allowed
represented in curly braces{}
items are not stored in index order
-------------------------------------
'''
any = {1,2,2,3,4}
print(any)
'''
methods:
union()syntax--->variable _name.union(another var)

it will give all values from 2 sets together in once

intersection() to get the common elements from both the sets

syntaxvariable _name.intersection(another var)
difference()
------------
to get the different values from the set
syntax-->variable_name.difference(another var)

add()
------
------>to add new element into set------------only 1 element
syntax-->variable_name.add(element)
remove used to remove are delete from the set but it will throw an error (key error)if element not in set
syntax----------variable name.remove(element)
discard ()
used to remove element from the set but it will not throw an error if element not in set.

------------------------------------------------------------
'''
any = {1,2,2,3,4}
an={34,45,68}
print(any | an)
 
any = {1,2,2,3,4}
an={34,45,68}
print(any - an)
print(any.difference(an)) 
 
any = {1,2,2,3,4}
an={34,45,68}
print(any ^ an)
print(any.symmetric_difference(an)) 
 
any = {1,2,2,3,4}
any.update([41,58,98])
print(any)

any = {1,2,2,3,4}
any.discard(2)
print(any)

any = {1,2,2,3,4}
any.remove(2)
print(any)

