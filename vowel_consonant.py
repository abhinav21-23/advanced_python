def check_vowel_consonant(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter.lower() in vowels:
        return 'vowel'
    else:
        return 'consonant'
input_letter = input("Input a letter of the alphabet: ")
result = check_vowel_consonant(input_letter)
print(input_letter, "is a", result + ".")
