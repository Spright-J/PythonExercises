from datetime import datetime

todays_date = datetime.now().date()
time_now = datetime.now().time()

print("Today is " + todays_date.strftime("%Y-%m-%d") + " and it is " + time_now.strftime("%I:%M:%S") + ".")




'''
Write a program printing the current date (year month day hour minute and seconds) in a human readable format.

It should look like this:

Today is 2015-09-17 and it is 09:34:35.
Beware the width is constant: 9h should displayed as 09:00:00, not 9:00:00, same for the month, day, and so on.

'''