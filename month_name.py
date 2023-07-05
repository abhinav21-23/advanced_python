def get_month_days(month):
    month_days = {
        'january': 31,
        'february': '28/29',
        'march': 31,
        'april': 30,
        'may': 31,
        'june': 30,
        'july': 31,
        'august': 31,
        'september': 30,
        'october': 31,
        'november': 30,
        'december': 31
    }
    return month_days.get(month.lower(), 'Invalid month')
months_list = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]
input_month = input("Input the name of Month: ")
days = get_month_days(input_month)
print("No. of days:", days, "days")
