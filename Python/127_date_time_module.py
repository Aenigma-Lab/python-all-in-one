import datetime as dt

now = dt.datetime.now()
print(type(now))
year = now.year
print(type(year))
print(now)
if year == 2025:
    print("very good")


month = now.month
day_of_week = now.weekday()
print(day_of_week)

###########################################################
# create own date time object
date_of_birth = dt.datetime(year=1998, month=7, day= 14)
print(date_of_birth)