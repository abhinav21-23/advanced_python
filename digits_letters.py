def count_digits_letters(string):
    digit_count = 0
    letter_count = 0
    for char in string:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            letter_count += 1
    return digit_count, letter_count
input_string = input("Enter a string: ")
digits, letters = count_digits_letters(input_string)
print("Letters:", letters)
print("Digits:", digits)
