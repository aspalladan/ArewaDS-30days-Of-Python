# Day 16: 30 days of Python programming
# importing the required functions

from datetime import datetime,date,time,timedelta

# Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
d = now.strftime("%m/%d/%Y, %H:%M:%S")
print(d)


# Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)


# Calculate the time difference between now and new year.
t_day = date(2023,2,20)
new_year = date(2024,1,1)
time_to_new_year = new_year - t_day
print(f'Time to new year is {time_to_new_year} ')


# Calculate the time difference between 1 January 1970 and now.
# Option one: Getting the time difference in seconds
# This is the timestamp already calculated above
print(f'The time difference between now and 1 January, 1970,midnight in seconds is {timestamp} ')

# Option two: Getting the time difference in days
# I have already assigned the current year,month and day from above
print(date(year,month,day) - date(1970,1,1)) #19000 plus day



'''Think, what can you use the datetime module for? Examples:
Time series analysis
To get a timestamp of any activities in an application
Adding posts on a blog
So many possibilities but somehow lubridate (R's tidyverse) is much better than what I am seeing here.'''

