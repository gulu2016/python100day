import datetime as dt

# s289-1-1-4 there are some problems caused program to not run
# s289-1-1-1 create a datetime object,it has all time attributes
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
# s289-1-1-2 weekday return the value start from 0, 0 means Monday
print(day_of_week)

# s289-1-1-3 create datetime object using int values
date_of_birth = dt.datetime(year=1995,month=10,day=16,hour=12)
print(date_of_birth)