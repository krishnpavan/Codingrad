print("            ***DATA SCIENCE Task 1 - Mean, Median and Mode***            ")

print("Mean - It is used to know average value") 

def mean(list_of_nums):
    sum = 0
    for i in list_of_nums:
        sum += i
        return sum/len(list_of_nums)
print("Mean Value is : ", mean([1,2,3,4,5,6,7,8,9,10]))

print("Median - It is used to know midpoint value")
def median(list_of_nums):
    list_of_nums.sort()
    if len(list_of_nums) % 2 == 0:
        return (list_of_nums[int(len(list_of_nums)/2)] + list_of_nums[int(len(list_of_nums)/2)-1])/2
    else:
        return list_of_nums[int(len(list_of_nums)/2)]
print("Median Value is : ", median([1,2,3,4,5,6,7,8,9,10]))
print("Mode - It is used to find most common values")
def mode(list_of_num):
    max_count = (0,0)
    for i in list_of_num:
        repeat = list_of_num.count(i)
        if repeat > max_count[0]:
            max_count = (repeat,i)
    return max_count[1]
print("Mode Value is : ", mode([1,2,4,6,5,5,7,8,9,10]))