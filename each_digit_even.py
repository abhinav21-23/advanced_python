def check_even_digits(num):
    num_str = str(num)
    for digit in num_str:
        if int(digit) % 2 != 0:
            return False
        else:
            return True
numbers = []
for num in range(100, 401):
    if check_even_digits(num):
        numbers.append(str(num))
print(",".join(numbers))
