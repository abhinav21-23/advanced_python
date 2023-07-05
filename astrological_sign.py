def get_astrological_sign(day, month):
    if (month == "december" and day >= 22) or (month == "january" and day <= 19):
        return "Capricorn"
    elif (month == "january" and day >= 20) or (month == "february" and day <= 18):
        return "Aquarius"
    elif (month == "february" and day >= 19) or (month == "march" and day <= 20):
        return "Pisces"
    elif (month == "march" and day >= 21) or (month == "april" and day <= 19):
        return "Aries"
    elif (month == "april" and day >= 20) or (month == "may" and day <= 20):
        return "Taurus"
    elif (month == "may" and day >= 21) or (month == "june" and day <= 20):
        return "Gemini"
    elif (month == "june" and day >= 21) or (month == "july" and day <= 22):
        return "Cancer"
    elif (month == "july" and day >= 23) or (month == "august" and day <= 22):
        return "Leo"
    elif (month == "august" and day >= 23) or (month == "september" and day <= 22):
        return "Virgo"
    elif (month == "september" and day >= 23) or (month == "october" and day <= 22):
        return "Libra"
    elif (month == "october" and day >= 23) or (month == "november" and day <= 21):
        return "Scorpio"
    elif (month == "november" and day >= 22) or (month == "december" and day <= 21):
        return "Sagittarius"
    else:
        return "Invalid date"
day_input = int(input("Input birthday: "))
month_input = input("Input month of birth (e.g. March, July etc): ").lower()
sign = get_astrological_sign(day_input, month_input)
print("Your Astrological sign is:", sign)
