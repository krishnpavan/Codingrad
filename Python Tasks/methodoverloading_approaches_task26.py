'''
When there are two or more methods with the same name 
and are present in the same class, the later method 
overrides the previous methods. As a result, during 
runtime, the namespace which has a unique name for 
each object present in python will update the entry 
in the local namespace and thus avoids existing of 
more than one method with the same name.
Hence, to get over this issue there are a few ways through which method overloading can be achieved.
Method Overloading - Same Class, Same Function and Different Parameters
Overloading means one object can have multiple behaviors
Overloading is one of the domain features of OOPS
Two or more methods have same name but differ in parameters
Parametrs can differ in two types
Number of parameters and Datatype of parameters
The following are method over loading approaches
1. Multiple Dispatch Decorator - 
Decorator is used to implement featurs of one method to other method
2. Based on Argumets
3. Operator Overloading
'''

# Method overloading using Multiple Dispatch operator
# Method with same name and gives output based on number
# and type of parameters with which method is called

# Multiple dispatch decorator method overloading illustration
# importing dispatch 
from multipledispatch import dispatch

# dictionary having product id and its cost
productIdandcost = {1001:10.00,1002:30.00,1003:40.00}

# dictionary having product name and its cost corresponding to product ids mentioned above
productNameandcost = {'pen':10.00,'tape':20.00,'book':30.00}

# method to calculate net amount with product id and its quantity as arguments
@dispatch(int,int)
def CalculateNetAmount(productId,qty):
    cost = productIdandcost[productId]
    netamount = cost * qty
    print(netamount)

# method to calculate net amount with product name and its quantity as arguments
@dispatch(str,int)
def CalculateNetAmount(productName,qty):
    cost = productNameandcost[productName]
    netamount = cost * qty
    print(netamount)

#  method to calculate net amount with product name, its quantity and user defined cost as arguments
@dispatch(str,int,float)
def CalculateNetAmount(productName,qty,cost):
    netamount = cost * qty
    print(netamount)

# calling the method by passing both arguments as int datatype
CalculateNetAmount(1001,2)
# calling the method by passing arguments as string and int datatype
CalculateNetAmount('tape',2)
# calling the method by passing arguments as int,string and float datatype
CalculateNetAmount('Pencil',2,5.00)


# Based on Arguments
'''
Based on type and no of arguments being passed we can 
make the same method differently using conditional statements

'''
# Program to illustrate based on arguments type
# Dictionary having product id and its cost
ProdutIdandCost = {1001:10.00,1002:20.00,1003:30.00}

# Dictionary having product name and its cost correspondig to
# product id's mentioned above
ProductNameandCost = {'Pen':10.00,'Tape':20.00,'Book':30.00}

# Method to calculate net amount based on diferent parameters sent
def CalculateNetAmount(datatype,product,qty):

    # Below code is executed if datatype is integer
    if(datatype == 'int'):
        cost = productIdandcost[product]
        netAmount = cost * qty
        print(netAmount)
    
    # Below code is executed if datatype is string
    if(datatype == 'str'):
        cost = ProductNameandCost[product]
        netAmount = cost * qty
        print(netAmount)

#calling method with int datatype as its arguments
CalculateNetAmount('int',1001,2)

#calling method with str datatype as its arguments
CalculateNetAmount('str','Tape',2)


# Program to illustrate Operator overloading
'''
Operators can also operate differently depending on the operand they are working on.
For example, the ‘+’ operator is used to find the sum of integers, concatenate strings, 
and also to combine two lists and tuples.
Not only do python operators work for in-built classes but also user-defined classes. Therefore, operator overloading helps 
in extending the operability of the operators.
We can extend the operability of the operators using “Magic Methods”.
Magic methods are  constructors or special methods in Python and these methods always begin and 
terminate with a double underscore(__).
__init__() method is one of the examples of magic methods.
'''

# To illustrate operator overloading
class Age():
    def __init__(self,age):
        self.a = age
    # method using __ge__ (greater than or equal to constructor)    
    def __ge__(self,other):
        result = self.a >= other.a  # to check ages of persons
        return result

# Creating objects for the class
PersonA = Age(40)
PersonB = Age(20)

# For checking personA age is greater PersonB age true or not
check = PersonA >= PersonB
print(check)





    
