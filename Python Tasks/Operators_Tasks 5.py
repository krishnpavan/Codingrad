# Task 5 - Operators practice

# Arithematic operators 
# Addition, Subtraction, Multiplication, Division,Modulus,Exponent or Power and Floor Division
a = 16
b = 10
print("The sum of a and b is: ",a+b)
print("The difference of a and b is: ",a-b)
print("The product of a and b is: ",a*b)
print("The division of a and b is: ",a/b)
print("The modulus of a and b is: ",a%b)
print("The Power ofa and b is: ",a**b)
# floor divison means,the quotient in divison which is float data type will be converted to int datatype
print("The Floor divison of a and b is: ",a//b) 

# Assignment operators

# Equal to assignment
a = b
print(a,b)

# Add AND assignment
a+=b # similar to a = a + b
print('The sum of a and b is',a)

# Subtract AND assignment
a-=b # similar to a = a - b
print('The difference of a and b is',a)

# Multiplication AND assignment
a*=b # similar to a = a * b
print('The product of a and b is',a)

# Divison AND assignment
a/=b # similar to a = a / b
print('The divison of a and b is',a)

# Modulus AND assignment
a%b # similar to a = a%b
print('The modulus of a and b is',a)

# Relational Operators - used to compare two operands
# less than operator (<)
p = 2
q = 5
print('The smallest one in p and q is p:',p<q)

# greater than operator (>)
p = 2
q = 5
print('The biggest one in p and q is q:',q>p)

# less than or equal operator (<=)
p = 2
q = 5
print('The less than or equal to in p and q is p:',p<=q)

# greater than or equal to operator (>=)
p = 2
q = 5
print('The greater or equal to in p and q is q:',q>=p)

# Equality operator (==)
p = 2
q = 5
print('Are p and q values equal:',p==q)

# Not equal to operator (!=)
p = 2
q = 5
print('p and q values are not equal:',p!=q)

# Logical operators - not,and,or
# Logical not operator
s = 15
t = (not s==20)
print(":",t)

# Logical and operator
# Example 1: When both k and l are same then m is true
k = 10
l = 10
m = ((k and l) == 10) 
print(m)
# Example 2: When both k and l are not same or either of them are 10 then m is false
k = 10
l = 11
m = ((k and l) == 10) 
print(m)

# Logical or operator
# example 1. If atleast one value is true it shows true
r = 10
q = 11
l = ((r or q) == 10) 
print(l)
# example 2. If both values are false it shows false
i = 12
j = 11
k = ((i or j) == 10) 
print(k)

# Membership operators
# used to validate membership of a value
# It tests membership in sequence such as strings,lists or tuples
# 'in' operator checks value present in sequence or not

# Example to check two lists and its common elements
l1 = [1,2,3,4,5]
l2 = [2,6,7,8,9]
for i in l1:
    if i in l2:
        print("Elements in lists l1 and l2 are overlapping")
else:
    print("Elements in lists l1 and l2 are not overlapping")

# 'not in' operator.
# Evaluates to true if it doesnot find element in specified sequence.

# Example. To check elements are present in list or not.
i = 21
j = 20
new_list = [20,15,25,30,42]
if (i not in new_list):
    print("i is not present in available list")
else:
    print("i is present in available list")
if (j in new_list):
    print("j is not present in available list")
else:
    print("j is present in available list")

# identity operators
# 'is' operator 
# Evaluates to true if variables on either side of operator point to same object
# Example
x = 5
if (type(x) is int):
    print("x is int datatype") 
else:
    print("x is not int datatype")

# 'is not' operator
# Evaluates to false if variables on either side of operator points to same object
x = 5.2
if (type(x) is not int):
    print("x is float datatype") 
else:
    print("x is not float datatype")

# Bitwise operators. We use these operators rarely.
# In python, bitwise operators are used to perform bitwise calculations on integers
# Integers are converted into bits and then operations are performed bit by bit
# The result returned will be in decimal format
# &(Bitwise AND),|(Bitwise OR),~(Bitwise NOT),^(Bitwise XOR),>>(Bitwise right shift)
# <<(Bitwise left shift) are some of the bitwise operators

