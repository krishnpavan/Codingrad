# A list in python is used to store the sequece of various types
# Python lists are mutable type  (values can be changed)
# We can modify its elements after its created
# Items in list are separted by camma (,) and 
# enclosed with square brackets []
# List in python are ordered
# lists allows duplicating of elements
# Elements in list are indexed according to definite sequence 

# Creating list
pavan = [] # empty list
print(type(pavan))

# list with different data types
pavan = [1,2.1,'mallik',True]
print(pavan)

# Indexing in list. 
# n elements in list then index starts with 0 i.e n-1
# [start,stop,step] is indexing method in list
pavan = [1,2.1,'mallik',True,1,2,3,4,5,7,8]
print(pavan[7])
print(pavan[3:8])
print(pavan[-1:2]) # negative to positive index is not possible.
print(pavan[2:9:3])
print(pavan[:3])
print(pavan[2:])
print(pavan[9:-6:4])
print(pavan[::-1])

# List methods or functions

# append method in list
# append means adding a sub list
# and always adds elements to end of the list.
pavan = [3,5,8,9,6,8,9]
pavan.append(['kumar','mallik'])
print(pavan)

# extend method in list.
# elements gets added separately at the end 
pavan.extend(['kumar','mallik'])
print(pavan)

# copy method in list. 
# Using copy method original data will not be changed
d = [1,2,3,4,5,6]
x = d.copy()
d.append(12)
print(d)
print(x)

# clear method in list.
# used to delete all the elements with in list
p = [5,6,7,8,9,12]
p.clear()
print(p)

# count method in list.
# Element name needs to be given as its argument
# It counts how many times a element repeated in list.
r = [2,3,4,5,7,8,9,12,11,2,23,4,5,56,45]
print(r.count(2))

# index method in list.
# element name needs to be given as its argument 
# It shows at which index element is in.
q = ['pavan','mallik',5.5,25.5,True]
print(q.index(5.5))

# insert method in list.
# it takes two arguments, 
# first argument is index position and
# second argument is element name to be added at that particular index position 
# n-1 will be not taken.
# element gets added at mentioned index position only
# To add an element at a particular index with in list 
l = [1,21,45,56,67,89,90]
l.insert(0,'pavan')
print(l)

# pop method in list is used to remove element
# at a particular index position
# index position is given as its argument
u = [3,5,6,7,8,9,3,4,5,6]
u.pop(6)
print(u)

# remove method in list is used to remove element from list
# if any duplicates available with in list
# which ever comes first with in list will be removed
# element name is given as its argument.
u.remove(5)
print(u)

# reverse method in list is used to reverse elements
u.reverse()
print(u)

# To find index of element with in list
x = [0,1,6,7,5]
print(range(len(x)))
for i in range(len(x)):
    if x[i] == 7:
        print(i)

# split function is used to convert string to list
str1 = "Hello pavan from Clarivate , Hyderabad"
x = str1.split()
print(x)

# sort method in list is used to sort elements 
# based on asc or des order
#  asc --> des (small to big) or 
# des --> asc (big to small)
'''
Syntax:

list_name.sort(key=…, reverse=…) – it sorts according to user’s choice 

Parameters:

reverse: reverse=True will sort the list descending. Default is reverse=False
key: A function to specify the sorting criteria(s)
'''
k = [4,6,8,10,12,14,16]
k.sort(reverse = True) # will get big to small
print(k)

# List comprehension is single line of code 
# to construct powerful functionality
# are used for creating new lists from other
# iterables like tuples, strings,arrays, lists
# it consists of brackets containing the expression
# which is executed for each element along with for loop
# to iterate over each element
# syntax is as follows
'''
syntax:
list = [expression(element) if cond for item in sequnce]
''' 
# Advantages of list comprehension are as follows
# more time-efficient and space efficient than loops
# require fewer lines of code
# transforms iterative statement into a formula

# To find odd and even numbers between 1 to 10 using 
# list comprehension
list = ["Even" if i % 2 == 0 else "odd" for i in range(10)]
print(list)

# Basic for loop to find odd and even numbers between 1 to 10
for i in range(0,10):
    if i % 2 == 0:
        print('even', end = " ")
    else:
        print('odd', end = " ")
    print(i,end = " ")



