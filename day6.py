'''
type conversions
------------------

int-->


an = 78
us = str(an)
om = float(an)
print(om)
print(type(om))
print(type(us))

str-->can be converted to int if pure int characters are present#same as to float
we can convert string into list and tuple to
str as a user input some = input ("write a text:")
-------------------------------------------------------------------------------------
ex:
'''
an = (5)
print(type(an))

car = 90.78
print(int(car))
print(str(car))
print(type(str(car)))

any = [6,7]
print(str(any))
print(tuple(any))


how = (4,5)
print(list(how))
print(str(how))

num = int(input("enter a number: "))
print(89+num)

some = input("write a text :")
print(some)

any = list (map(int,input("enter numbers:").split()))
print(any)

num = eval(input("enter: "))
print(type(num))

