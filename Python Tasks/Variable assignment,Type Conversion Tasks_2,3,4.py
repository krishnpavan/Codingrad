#To calculate simple interest
p = 100 # principal amount
t = 50 # time
r = 10 # rate of interest
SI = p*t*r/100
print("simple_interest is: " ,SI)

# To calculate compound interest A = P(1 + r/n)**n*t
#  CI = A - P
# P is the principal amount
# r is the rate of interest(decimal)
# n is frequency or no. of  times the interest is compounded annually
# t is the overall tenure.
n = 14
t = 2
A = (p*(1 + r/n))**n*t
CI = A - p
print("compund_interest is: " ,CI)

#Data types and Type Conversion

a=56  #int
b=-12
c=4.35   #float
d=True   #boolean
e=False   
f=5+6j    #complex

print(type(a),type(b),type(c),type(d),type(e),type(f))

#Type conversion
int()
float()
bool()
complex()
str()
# implicit type conversion
pavan=50   #int to float
s=float(pavan)
print(s)
print(type(s))
kumar=bool(pavan)  # int to bool
print(type(kumar))
venkat=complex(pavan)  #int to complex
print(venkat)
print(type(venkat))

# Explicit conversion
pavan=12.5  #float to int
p=int(pavan)
print(p)
print(type(p))
r=bool(pavan)  #float to bool
print(pavan)
print(type(pavan))
n=complex(pavan)
print(n)
print(type(pavan))  #float to complex

#Explicit type conversion
s=2022.222
c=int(s)
print(c)
print(type(c))

my_fav=str(s)
print(my_fav)
print(type(my_fav))






