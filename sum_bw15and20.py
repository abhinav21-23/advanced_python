def sum(a, b):
    sum_result = a + b
    if 15 <= sum_result <= 20:
        return 20
    else:
        return sum_result
input_a = int(input("Enter the first integer: "))
input_b = int(input("Enter the second integer: "))
result = sum(input_a, input_b)
print("Sum:", result)
