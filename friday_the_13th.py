from datetime import date, datetime

def friday_the_13th():
    month = date.today().month
    year = date.today().year
    

    if date.today().day == 13 and  date.today().weekday() == 4:
        return date.today().strftime("%Y-%m-%d")
    
    if date.today().day < 13:
        if date(date.today().year, date.today().month, 13).weekday() == 4:
            return_date = date(date.today().year, date.today().month, 13)
            return return_date.strftime("%Y-%m-%d")
        
    while True:
        month += 1
        if month > 12: month = 1; year +=1 
        if date(year, month, 13).weekday() == 4:
            return_date = date(year, month, 13)
            return return_date.strftime("%Y-%m-%d")



print(friday_the_13th())

'''
Find the next friday the 13th.

Write a function named friday_the_13th, which takes no parameter, and just returns the date of the next friday the 13th.

If today is a friday the 13th, return it, not the next one.

Return the date as a string of the following format: YYYY-MM-DD.
'''
