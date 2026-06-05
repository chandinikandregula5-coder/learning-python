'''
Inheritance
-----------
--->this allows one class to aquire the properties and methods of another
class...
types
------
1.single inheritance
--------------------
a class inherits from a single parent class....

class father:
    def land(self):
        print("my father have 5A")

class anu(father):
    def my_own(self):
        print('i have 2A')

2.multiple inheritance:class inherits from multiple parent class
----------------------
father mother
  |     |
        |
  |     |
  child
  
class father:
    def land(self):
        print("my father have 5A")

class mother:
    def gold(self):
        print('my mother have 1 kg G')

class son(father,mother):
      def mine(self):
          print("i have ntg")
          
fam=me()
father.land()
mother.gold()

3.multilevel inheritance
------------------------
a class inherits from a parent class and another class inherits from that child class

class grandfather:
    def land(self):
        print("my  grand father have 5A land")
class father:
    def land(self):
        print("my father have 5A")

class mother:
    def gold(self):
        print('my mother have 1 kg G')

class son(father,mother):
      def mine(self):
          print("i have ntg")
          
fam=me()
father.land()
mother.gold()
all_.son()
all_.land()
all_.flat()
all_.ntg()

4.HIERARCHICAL INHERITANCE
-------------------------
multiple child classes inherits from single parent class

class father:
    def land(self):
        print("my father have 10A")

class teja (father):
    def mine(self):
        print('job')

class raghava(father):
      def bro(self):
          print("jobless")
          
rag=raghava()
rag.land()

so = teja()
so.land()

5.hybride inheritance
this is the combination of two or more types of inheritance

class A:
    def some(self):
        print('class A')
class B(A):
    def any(self):
        print('class B')
class c(A):
    def so(self):
        print('class c')
class D(B,C):
    def ALL_(self):
        print('class D')

how = D()
how.so()
super()method
-------------
super()is used to access methods and constructor of the parent class from the child class

class parent:
    def display(self):
        print('method parent')
        
class child(parent):
    def display(self):
        super().display()
        print('method child')
any_=child()
any_.display()
'''
