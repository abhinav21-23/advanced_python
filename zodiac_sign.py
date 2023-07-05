def get_chinese_zodiac_sign(year):
    zodiac_signs = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep"]
    start_year = 1924  
    index = (year - start_year) % 12 
    return zodiac_signs[index]
birth_year = int(input("Input your birth year: "))
zodiac_sign = get_chinese_zodiac_sign(birth_year)
print("Your Zodiac sign:", zodiac_sign)
