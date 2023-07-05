def find_median(num1, num2, num3):
    sorted_nums = sorted([num1, num2, num3])
    median = sorted_nums[1]
    return median
num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))
num3 = float(input("Input third number: "))
median = find_median(num1, num2, num3)
print("The median is", median)
