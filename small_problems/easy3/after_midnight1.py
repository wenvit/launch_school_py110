'''
After Midnight (Part 1)

The time of day can be represented as the number of minutes before or 
after midnight. If the number of minutes is positive, the time is 
after midnight. If the number of minutes is negative, the time is 
before midnight.

Write a function that takes a time using this minute-based format 
and returns the time of day in 24-hour format (hh:mm). Your function 
should work with any integer input.

You may not use Python's datetime module.
'''

def format_time(input_int):
    return str(input_int).rjust(2, '0')

def time_of_day(input_minutes):

    hrs, mins = divmod(abs(input_minutes), 60)

    if abs(input_minutes) >= 1440:
        days, min_remain = divmod(abs(input_minutes), 1440)
        hrs, mins = divmod(min_remain, 60)

    if input_minutes < 0:
        return f'{format_time(23 - hrs)}:{format_time(60 - mins)}'
    else:
        return f'{format_time(hrs)}:{format_time(mins)}'

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
print(time_of_day(1440))