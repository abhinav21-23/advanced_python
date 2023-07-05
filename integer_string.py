def check_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
input_string = input("Input a string: ")
is_integer = check_integer(input_string)
if is_integer:
    print("The string represents an integer.")
else:
    print("The string is not an integer.")
