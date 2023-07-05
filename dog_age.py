def calculate_dog_age(human_years):
    if human_years <= 2:
        dog_years = human_years * 10.5
    else:
        dog_years = 21 + (human_years - 2) * 4
    return dog_years
human_age = int(input("Input a dog's age in human years: "))
dog_age = calculate_dog_age(human_age)
print("The dog's age in dog's years is", dog_age)
