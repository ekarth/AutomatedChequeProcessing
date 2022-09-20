import datetime
import time
def validate_check_date(date):
    
    correct_date = ''
    for d in date:
        if d.isdigit():
            correct_date += d

        if d == 'O' or d == 'o':
            correct_date += '0'

        elif d == 'l' or d == 'I' or d == 'i':
            correct_date += '1'

        elif d == 'T':
            correct_date += '7'
    
    # print(correct_date)
    day = int(correct_date[:2])
    month = int(correct_date[2:4])
    year = int(correct_date[4:])

    check_date = datetime.date(year, month, day)
    today_date = datetime.date.today()
    is_valid = not((today_date - check_date).days > 90)
    
    return is_valid, int(time.time()*1000)

# print(validate_check_date('2.5 03 2016'))