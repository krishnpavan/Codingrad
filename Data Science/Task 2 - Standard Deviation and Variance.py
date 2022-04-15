print("           ***DATA SCIENCE Task 2 - Standard Deviation and Variance***           ")
print("Standard Deviation - It is used to find the distance of each value from the mean")
print("Variance - It is used to find the relationship between data")

# math library is used for calculations
import math
# taking some sample data
data = [1,2,3,4,5,6,7,8,9,10]
# calculating mean
mean = sum(data)/len(data)
# calculating variance
variance = sum([(x-mean)**2 for x in data])/len(data)
# calculating standard deviation
standard_deviation = math.sqrt(variance)
# printing result
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)





