'''                              ** Task 27 **                                                    '''
'''                Object Oriented Programming features practice                                  '''

# class(template)
'''
1. We will deine class by using keyword 'class'
2. Blueprint to create objectd
3. Collection of objects is called class
4. To get output only class is not sufficient
5. Objects need to be declared to get required output
'''
# Example - Fruits is class and 
# Types fruits like Oranges,Apples,Grapes etc are objects

# object 
# physical entity (real)
'''
1. object is an instance of a class
2. instance means object is a small part or a element with in a class
3. memory is created when object is declared
4. We will get out only when object is declared

'''
# object examples - apple,mango,banana etc


# attribute (variable) or data members
'''
a = 20 # in oops a is called as attribute or data members
color = 'blue'
'''


# Method(behaviour) or functions
# will be doing some work mentioned below
'''
eat()
sleep()
run()
talk()
'''


# self keyword means owned by me only
# self means current class
'''
using self keyword we can access the attributes and methods
of the current class only
'''

# Syntax of class
'''
class Class_name:
    constructor
    attributes
    methods
'''


# Example to illustrate class 
# With one object
'''
Points to remember:
1. Constructor should always start with capital
2. In method self keyword should always given to access 
   current class attributes
3. To create memory we need to declare object
4. For one class we can create as manay as objects
5. when we write function with in class we must use self keyword
'''
# class with one method and one object
from re import A, L
from this import d


class Pavan: # class keyword class name
    a = 10 # data member or attribute
    def Output(self): # method(self), self keyword is default
        print(self.a) # To access current class attributes or methods we use self keyword
obj = Pavan() # declaring of object using class name. Memory gets created in class
obj.Output() # using object we can call the method



# One more example to illustrate class 
# Here we declare two objects with same method
class Mallik:
    a = 10 # attribute
    def display(self): 
        print(self.a)

krishna = Mallik() # object declaration
kumar = Mallik() # another object created
krishna.display()
kumar.display()




# class with sting as its attribute
class Pavan: # class keyword class name
    a = 'Employee' # data member or attribute
    def Output(self): # method(self), self keyword is default
        print(self.a)
obj = Pavan() # declaring of object
obj.Output() # using object we can call the method


# class with my two vehicle names as attributes
class Pavan_vehicle():  # class name
    bike = 'Honda Levo'  # attribute declaration
    scooty = 'Yamaha Fascino' # attribute declaration
    def vehicle_name(self): # Vehicle_name is a member function
        print(self.bike)  # to print my output
        print(self.scooty)  # to print my output
venkat = Pavan_vehicle() # Declaring object name venkat
venkat.vehicle_name() # calling the member function method

# objects are used to store in memory
# In lamda function we passed data using object,
# But we call it as object not variable
# In lambda we assigned something and considered it as object 
# instead of variable 

# __init__ - 
# For Initializing all the attributes in one place

'''
1. Constructors are generally used for instantiating an
object. 
2. The task of constructors is to initialize(assign values)
to the data members of the class when an object of the class 
is created.
3. In Python the __init__() method is called the constructor
and is always called when an object is created

does'nt support multiple constructor 
'''
# class name and constructor name should be same in 
# other programming language
# if we declare object in constructor once no need to call 
# it automatically gets executed
# Python doesnot support multiple constructors
# costructor types are default constructors, parametarized constructors
# overriding constructor
# __init__ is called as method or constructor
# it is used for initialisig or declaring all
# attributes at a time by keeping in __init__ constructor
# constructor type is __init__
# So many constructors are available in python 

# Example for __init__ illustration
class Pavan(): # class name
    # __init__ constructor method 
    # To initialise all parameters a,b,c at one place
    def __init__(self,a,b,c): # a,b,c are parameters
        # Always remember left side is attribute or variable
        # right side is called value
        # so in self.x = a. a,b,c known as values
        # so x,y,f are attributes or data members
        # self.x,self.y,self.f is used to access
        # x,y,f attributes through out program using
        # self keyword
        self.x=a # 10
        self.y=b # 1
        self.f=c # 2

    def display(self): # display(self) is member function
        print(self.x)
        print(self.y)
        print(self.f)
        

# object declaration
# values to parameters a,b,c are passed inside class function
mallik = Pavan(10,1,2) # 10 stores in a, 1 stores in b and 2 stores in c
# object name . method name()
mallik.display()




# Bike purchase program using __init__ constructor
class Bikes: # class declaration or definition
    def __init__(self,brand,milage,cost,cc,color):
        self.a=brand
        self.x=milage
        self.z=cost
        self.s=cc
        self.j=color
    def bike_details(self):
        print('Bike Brand',self.a)
        print('Bike Milage',self.x)
        print('Bike Cost',self.z)
        print('Bike CC  ',self.s)
        print('Bike Color',self.j)
brands=input('Enter the Brand Name: ')
Milages=input('Enter the Milage: ')
Costs=float(input('Enter the cost of Bike: '))
cc = input('Enter CC: ')
color =input('Enter the Color Name: ')

Bike_obj=Bikes(brands,Milages,Costs,cc,color)
Bike_obj.bike_details()


# Inheritance
# Single Parent child
# multiple
# multilevel
# heirarchy

# Single Inheretence - child syntax outputChild(self)
# parent property is output member function
# object is created in child class
# if object is created in Parent class, no use of inheritance property

class Parent():
    def output(self):
        print('This is parent class')

class Child(Parent): # syntax for child class
    def outputChild(self): # output member function properties gets inherits here
        print('This is child class')

 # creating object for Child() function
obj_i = Child() 
# using Child() object calling parent member function output(self)
obj_i.output()
# using Child() object calling child member function outputChild()    
obj_i.outputChild()


# __init__ can be used in both parent and child class
# Data need to be passed from child 
# Both parameters are not same
# Take 3 parameters in parent and 2 parameters in child
# then pass these in child
# Gettig Typeerror missing one required positonal argument
# when trying to access parent objects through child function
class Parent():
    def __init__(self,i,j):
        self.p = i
        self.l = j
    
    def OutputParent_details(self):
        print('Value of i is: ',self.p)
        print('Value of j is: ',self.l)

i= 10
j= 20

class Child():
    def __init__(self,m,n,o):
        self.e = m
        self.f = n
        self.g = o
    def OutputChild_details(self):
        print('Value of m is: ',self.e)
        print('Value of n is: ',self.f)
        print('Value of o is: ',self.g)
m= 30
n= 40
o= 50
# Creating an object to access child function properties
final_obj = Child(m,n,o)
# Accessing child properties using its own member function
final_obj.OutputChild_details()

# Multiple inheritence
# Two parent classes and one child class
# We can access father and mother classes properties using
# child function and syntax is Child(Father class name,Mother class name)
class Father:
    def output(self):
        print('this is father class')
class Mother:
    def outputM(self):
        print('this is mother class')
class Child(Father,Mother): # Syntax imp
    def outputChild(self):
        print('this is child class')
# creating an object for child() function
ice = Child()
# Accessing father function properties by using child object
ice.output()
# Accessing mother function properties by using child object
ice.outputM()
# Accessing child's own properties using child's object
ice.outputChild()


# Multi level Inheritence
# For getting output,we need to call all the member functions 
# using objects
# If we use __init__ then no need to call, it automatically returns output
class GrandFather:
    def outputgf(self):
        print('this is Grand father class')
class Father(GrandFather): # syntax imp
    def outputf(self):
        print('this is father class')
class Child(Father): # syntax imp
    def outputc(self):
        print('this is child class')
# Creating object 'kumar' for child() 
kumar = Child()
# Accessing grandfather properties using child object
kumar.outputgf()
# Accessing father properties using child object
kumar.outputf()
# Accessing child own properties using child object
kumar.outputc()

# Heirarchy Inheritence
# One Parent class and two child classes
# We need to create objects for both child classes
# child1 will have properties of its own and father properties
# child2 will have properties of its own and father properties
# But child1 cant access child2 properties and vice versa
class Father(): # 100cr
    def outputf(self):
        print('this is father class')
class Child1(Father): # syntax imp # 50cr
    def outputc1(self):
        print('this is child 1 class')
class Child2(Father): # syntax imp # 50cr
    def outputc2(self): 
        print('this is child 2 class')

# child1 object declaration
krishn = Child1()
# child2 object declaration
venkat = Child2()
# accessing father properties using child1 object
krishn.outputf()
# accessing father properties using child2 object
venkat.outputf()
# accessing child1 properties using its own child 1 object
krishn.outputc1()
# accessing child2 properties using its own child 2 object
venkat.outputc2()


# Polymorphism - many forms
# 1. method overriding means
# Different class, Same method names, Different Parameters
# 2. method overloading means
# Same class, Same method names, Different Parameters

# Method overloading illustration
#  using default parameters and keyword 'None'
class Methodoverload:
    # using None keyword we can avoid error
    def something(self,a=None,b=None,c=None): 
        print(a,b,c)
# creating object for Memberoverload() function
obj=Methodoverload()
# accessing member function something() by specifying all three different parameters
obj.something(1,2,3)
# accessing member function something() by specifying only two different parameters
obj.something(1,2)
# accessing member function something() by specifying only one parameter
obj.something(1)


# Method overriding
# Different classes, same method names, Different Parameters

# Methodoverriding program illustration
# super keyword is used to access parent class and
# current class attributes or methods
# self keyword is used to access only current class
# attributes or methods
class Methodoverri:
    def display(self):
        print("this is parent class")

class Child(Methodoverri):
    def display(self):
         print("this is child class")
         super().display()
      
obj=Child()
obj.display()





# Encapsulation
# Binding of data or wrapping of data
# Access specifiers private,public,protected,and
# public anyone can access
# protected only their own generation can use
# private only by own class can access
# private __ (double underscore)
# protected _ (single underscore)


# Encapsulation illustration
class Gfather:
    def __init__(self,a):
        self._y=a # y is protected
class Father(Gfather):
    def display1(self):
        print(self._y)
class Child2(Father):
    def display2(self):
        print("child2",self._y)
obj = Child2(12)
obj.display2()



# Abstraction means Hiding
# One class abstractor method then its called abstractor base class
# Abstract method has no body,
# If body is there then implemention happens and hiding will not happen
# for abstract class objects cant be created
# @ decorator is used to implement features of one 
# method to other method

# To understand above points
# abc module, ABC class, abstractmethod method
from abc import ABC,abstractmethod 
class Parent(ABC): # abstract base class
    # @ is known as decorator.
    # abstractmethod functionalities will be given to done method functionalities
    @abstractmethod
    def done(self): # abstract function
        pass  # to skip body of abstract class we use pass keyword
    def func2(self): # normal function
        print('this is parent')

class Child(Parent):
    def done(self,a):
        print('this is child',a)

# creating object for child function
obj=Child()
# calling child method done()
obj.done(10)
# calling parent method using child object
obj.func2()
