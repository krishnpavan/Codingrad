# Write a program to concatinate two tuples
'''
v = (1,2,3,4,5)
y = (1,2,3,4,5)
Required output = (2,4,6,8,10)
'''

# First tuple details
v = (1,2,3,4,5)

# Second tuple details
y = (1,2,3,4,5)

# Creating an empty list
z = []
# For loop for concatinating two tuples
for i in range(0,5): # looping from 0 to 4 
        result = v[i] + y[i]
        z.append(result) # adding result to empty list z
print(tuple(z)) # to type cast list to tuple
