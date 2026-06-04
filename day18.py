'''
oops(object oriented programming systems)
a class is a blue-print or template used to create object
to create a class use "class" keyword

class stu:
     name = "siri"

2.object. an object is an instance of a class
3.attributes are the variables that belongs to a class or an object 

class stu:
    name="siri"
    def edu(self):
        print("i completed degree")
s1 = stu_()
print(s1.name)

class stu:
    name = "chandu"
s1 = stu_()
print(s1.name)

class stu:
    name = "chandu"
    age = '21'
s1 = stu_()
print(s1.name)
print(s1.age)

class PFS_DA:
    def python(self):
        PFS_DA = "batch_03"
        print("THIS PFS AND DA BATCH03")

    def flask(self):
        PFS = "batch_03"
        print("THIS PFS BATCH03")
class atm:
    def_init_(self,balance,name):
       self.balance = balance
       self.name = name
    def bal_check(self):
        print(f"{self.name} your balance is (self.balance+ 700)")
Access specifiers
-----------------
1.public
----------
this can be accessed from anywhere in the program
2.protected
------------
this is represented using a single underscore(_)
3.private
this is represented using a double underscore(__)
encapsulation
-------------
Is the process of binding data and methods together

class bank:
    def_init_(selfbalance):
        self._balance = balance
        
    def depo_(self,amount):
        self._balance+=amount
        
    def get_bala(self):
        return self._balance
    
acc =bank(1000)
acc.depo_(10000)
print(acc.get_bala())


class stu:
    _name = "teja"
s1 = stu()
print(s1._stu_name)


        
