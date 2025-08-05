After Midnight (Part 1)

The time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm). Your function should work with any integer input.

You may not use Python's datetime module.

##### PEDAC #####

# Define Problem
1. Input: integer representing minutes
   Output: string in 24-hour format (hh:mm)

2. Explicit rules:
   - The input integer represents minutes 
   - The minutes should be converted to time of day in 24-hour format, hh:mm
   - If the input int is positive, the time is after midnight
   - If the input int is negative, the time is before midnight
   - Cannot use datetime module

3. Implicit rules:
   - 24-hour time format --> hh:mm
     Where hours range from 00 (midnight) to 23 (11:00 pm)
           minutes range from 00 to 59
     So time of day ranges from 00:00 to 23:59
   - There are 1440 minutes in one day, so need to subtract 
     multiples of 1440 minutes if input minutes > 1440

# Test Cases
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

extra test case --> print(time_of_day(1440)) which I believe should be 00:00

# Data Structures
Inputs: integer
Outputs: string

# Algorithm

1. If input minutes >= 1440, take modulo (%) 1440 of input minutes to get remainder of minutes. 
2. If input minutes < 1440, divide minutes by 60 using // operator to get whole hours. Take % 60 to get remaining minutes.
3. If input is negative, subtract hours from 23 and minutes from 60.
If input is positive, hours & minutes will be as calculated.
4. Return hours & minutes from midnight in string format using f-string notation

