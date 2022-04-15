# Conditional statements practice
# In programming we need to make some decisions and based on these
# situations we will execute next block of code
# Decision making statements decide the direction of flow of program execution
# if else elif statement is used for decision making
'''
if
elif
else
nested if
short hand if
short hand if else
'''
# if statement.
# if statement is most simple decison making statement
# used to decide whether a certain statement or block of statements
# will be executed or not i.e. if certain condition is true then block of statemnt s executed or else will not
# syntax of if statement with indentation as follows
''' 
if condition:
    statement 1
statement 2
'''
# In above case if condition is true,if block
# will consider only statement1 which is inside its block

# Example python if statement
i = 20
if (i>25):
    print("Iam in if statement")
print("Iam not in if statement") # if condition here is false so this statement will be executed

# if-else statement in python
# if statement alone tells us that if condition is true it will execute 
# block of statements and if condition is false it wont
# else statement is used
# if we want to do something else if the condition is flase
# we can use elsestatement with ifstatement 
# to execute a block of when the condition is false
# syntax of if-else statement is as follows
'''
if condition():
    # executes this block if
    # condition is true
else:
    # executes this block if
    # condition is false
'''
# Example for python if else statement
i = 20
if(i<15):
    print("i is smaller than 15")
    print("i am in if block")
else:
    print("i is greater than 15")
    print("i am in else block")
print("i am not in if and not in else Block") # even this statement will be executed
# Above code executes statements in else block as
# the condition in if statement is flase
# also calls statement which is not in else block(without spaces)

# Python if-elif-else statement
# In this user can decide among multiple options
# If statements are executed from top down
# if condition is true, then statement with in if is executed
# rest of the statements are ignored
# if none of the condition is true, then the final else statement will be executed
'''
if (condition):
    statement
elif (condition):
    statement
.
.
.
else:
    statement
'''
# Example
i = 20
if (i == 10): # condition is false
    print('this is if statement')
elif (i == 15): # again condition is false
    print('this is first elif statement')
elif (i == 20): # condition is true and below statement will be executed
    print('this is second elif statement')
else:   # since above condition is true, else block will be ignored
    print('this is else statement')

# nested if statement
# A nested if is an if statement that is target of another i statement
# nested if statement means an if statement inside another if statement
# python allows to nest if statements with in if statements.
# we can place an if statement inside another if statement
# syntax of nested if statement as follows
'''
if (condition):
    # execute when condition1 is true
    if (condition):
         # execute when condition2 is true
    # nested if block ends here
# main if block ends here
'''
# Example python nested if
pavan = 'colony'
kumar = 'venkata'
if pavan == 'colony':
    print('This is main if statement')
    if kumar == 'krishna':
        print('This is nested if statement')
    else:
        print('This is inner else statement')
else:
    print('This is outer else statement')

# use of pass keyword. 
# If no statements with in if condition then use pass keyword
if True:
    pass

# short hand if statement
# whenever there is only single statement to be executed
# inside if block then shorthand if can be used
# statement can be put in same line as the if statement
# syntax is as follows
'''
if condition: statement
'''
# Example 
i = 12
if (i<15): print('i is less than 15')

# short Hand if-else statement
# this is used to write if-else statements in single line
# where there is only one statement to be executed 
# in both if and else block
# syntax is as follows
'''
statement_when_True if condition else statement_when_False
'''
j = 10
print('This is short hand if') if j > 10 else print('This is short hand else')













