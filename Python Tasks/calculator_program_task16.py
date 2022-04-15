# Program for a calculator
print("             *** Task 16 ***               ")
print("Calculator for performing matematical operation")
user_input1 = int(input("Enter one number: "))
user_input2 = int(input("Enter another number: "))
operation_input = input("Enter operator: ")
if operation_input == '+':
    sum = user_input1 + user_input2
    print("Sum of two numbers is: ",sum)
elif operation_input == '-':
    sub = user_input1 - user_input2
    print("Subtraction of two numbers is: ",sub)
elif operation_input == '*':
    prod = user_input1 - user_input2
    print("Product of two numbers is: ",prod)
elif operation_input == '/':
    div = user_input1 / user_input2
    print("Divison of two numbers is: ",div)
elif operation_input == '%':
    mod = user_input1 % user_input2
    print("Modulus of two numbers is: ",mod)
elif operation_input == '**':
    power = user_input1 ** user_input2
    print("Power of two numbers is: ",power)
elif operation_input == '//':
    floor_div = user_input1 // user_input2
    print("Floor Divison of two numbers is: ",floor_div)
else:
    ("Please try with a valid operator")
