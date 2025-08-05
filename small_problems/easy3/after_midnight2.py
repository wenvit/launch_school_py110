
'''
After Midnight (Part 2)
As seen in the previous exercise, the time of day can be represented 
as the number of minutes before or after midnight. If the number 
of minutes is positive, the time is after midnight. If the number 
of minutes is negative, the time is before midnight.

Write two functions that each take a time of day in 24 hour format, 
and return the number of minutes before and after midnight, respectively. 
Both functions should return a value in the range 0 through 1439.

You may not use Python's datetime module.

'''

MINS_PER_HR = 60

def parse_hhmm(hhmm):
    return hhmm.split(':')

def after_midnight(hhmm):
    hhmm_list = parse_hhmm(hhmm)
    hrs = int(hhmm_list[0])
    mins = int(hhmm_list[1])

    mins_after_midnight = hrs * MINS_PER_HR + mins 

    if mins_after_midnight < 1440:
        return mins_after_midnight
    else:
        return 0

def before_midnight(hhmm):
    hhmm_list = parse_hhmm(hhmm)
    hrs = int(hhmm_list[0])
    mins = int(hhmm_list[1])

    mins_before_midnight = (23 - hrs) * MINS_PER_HR + (60 - mins)

    if mins_before_midnight < 1440:
        return mins_before_midnight
    else:
        return 0

# Test Cases
print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True