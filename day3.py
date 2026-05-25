

#1.program to convert 24 hrs clock into normal clock

time_= input("enter 24 hrs time:")
parts_= time_.split(":")
hours_= int(parts_[0])
min_=int(parts_[1])
print(f"{time_}is converted into {hours_-12}:{min_} pm")


'''
2. list is a collection of  different data type
--> [] and seperated by,
'''
'''
any=[1,"python",[1,2]]
print(any)
'''
'''
any= [1,"python",[1,2,[34,"this is python 3rd class",78],"python is a language",89 ],34,[3,4]]
print(any[2][2][1][8])
'''
'''
append()
'''
'''
any= [1,2,3]
any.append(6)
print(any)any.append(20)
print(any)
this is methods is used to add new item into a list,and it will in the last index position.
syntax --> variable_name. append(item)

'''

'''
immutable
could not able to modify on that particular variable
eg

int, str
mutable

can able to modify on that particular variable
eg

list
'''
'''
any = [1,2,3,4]
any.extend("python")
any.append("python")
print(any)
'''
'''
extend
---------------
this method is used to add itterable into list ,and it will in the in the last index python, each value or substring in each index in the list.
'''
'''
any = [1,2,3]
print(any.pop(0))
pop()

'''
'''
it is used to  remove the item from the list ,but will mention here index position in the pop method.
''''''
any=[1,2,3]
any.remove(2)
print(any)
'''
'''
remove()
--------------
used to remove the item from the list, but will mention here direct in the remove method .
syntax-----------variable_name(item)
'''
