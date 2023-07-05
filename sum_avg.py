numbers = []
while True:
    num = int(input("Enter an integer number (enter 0 to finish): "))
    if num == 0:
        break
    numbers.append(num)
sum_numbers = sum(numbers)
average = sum_numbers / len(numbers) if numbers else 0
print("Sum:", sum_numbers)
print("Average:", average)
