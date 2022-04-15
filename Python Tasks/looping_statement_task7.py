# looping statement
# We can repeat until a set of statement until we stop
# like gaint wheel it keeps on rorating until it is stopped

# while loop
# while loop is used to execute a block of statements
# repeatedly until a given condition is satisfied
# when condition becomes false, the line immediately
# after the loop in the program is executed
# syntax is as follows
'''
while expression:
    statement(s)
'''
# all the statements are indented by same no of
# character spaces after programming construct are
# considered to be part of single block of code
# Python uses indentation as its method of grouping statements
# Example for basic while loop
count = 0
while (count<3):
    count+=1
    print('Hello Pavan')
# Example for while loop with else statement
pavan = 3
while pavan < 20:  # 4 5 6 7 8....20
    print('This is while')
    pavan+=1 # pavan = pavan + 1
else:
    print('stop')


# for loop statement
s = 'pavan'
for i in s:
    if i == 'a':
        print('This is if')
    else:
        print('This is else')

# iterating over range 0 to n-1
n = 4
for i in range(0,n):
    print(i)

# Break and Continue keywords in python
# Break keyword
# Break is used to terminate loop or statement in which it is present
# After that loop will pass the statment that are
# present after break keyword if available
# In nested loop break terminates only those loops which contains break statement
# break keyword using for loop
s = 'pavan'
for letter in s:
    print(letter)
    if letter == 'a':
        break
print('out of for loop')
# break keyword using while loop
i = 0
s = 'pavan'
while True:
    print(s[i])
    if s[i] == 'a':
        break
    i+=1
print('out of while loop')

# continue keyword will execute the next iteration of the loop
# code inside the loop following continue statement
# will be skipped and next iteration of loop will begin
# Syntax
'''
continue
'''
# Example of continue keyword
# Printing number 1 to 10 by skipping number 6
for i in range(1,11):
    if i == 6:
        continue
    else:
        print(i,end=" ")

# To find length of string name using len function
l = 'Pavan Kumar'
print(len(l))
if len(l) == 20:
    print('No of alphabets in l is 20')
elif len(l) < 15:
     print('No of alphabets in l is less than 15')
elif len(l) > 20:
     print('No of alphabets in l is less than 20')
else:
    print('neither')

# Knowing Length of string using len function 
# and printing its range using range function
p = 'pavan'
print(len(p))
for i in range(len(p)):
    print(i,end = " ")



    