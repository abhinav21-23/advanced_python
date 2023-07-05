def get_season(month, day):
    if (month == 1 and day >= 1) or (month == 2 and day <= 28):
        return "winter"
    elif (month == 3 and day >= 1) or (month == 4 and day <= 30):
        return "spring"
    elif (month == 5 and day >= 1) or (month == 6 and day <= 30):
        return "summer"
    elif (month == 7 and day >= 1) or (month == 8 and day <= 31):
        return "autumn"
    elif (month == 9 and day >= 1) or (month == 10 and day <= 31):
        return "autumn"
    elif (month == 11 and day >= 1) or (month == 12 and day <= 31):
        return "winter"
    else:
        return "Invalid date"
month_input = input("Input the month (e.g. January, February etc.): ")
day_input = int(input("Input the day: "))
month_input = month_input.lower()
month_dict = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}
if month_input in month_dict:
    month_number = month_dict[month_input]
    season = get_season(month_number, day_input)
    print("Season is", season)
else:
    print("Invalid month")
