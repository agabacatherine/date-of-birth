import datetime,calendar
current_year = 2017
date = input("Enter your date of birth (1-31)\n")
endings = ["st","nd","rd"] + 17*["th"]+ ["st","nd","rd"] + 7*["th"] + ["st"]
days = ['Monday','Tuesday','Wednesday','Thursday',
        'Friday','Saturday','Sunday']
month = int(input("Enter the month in which you were born (1-12)\n"))
month_names = ['January', 'February', 'March', 'April', 'May',
               'June', 'July', 'August', 'September', 'October',
               'November', 'December']
year = int(input("What's your age?\n"))
C1 = month_names[month-1]
C2 = int(date)
C3 = (current_year-year)
C4 = date+endings[C2-1]
C5 = calendar.weekday(C3,month,C2)
C6 = days[C5]

this = C1+" ", C2, ",", C3
print("You were born on ",C6,C4,C1, "of the year",C3)

