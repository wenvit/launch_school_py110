After Midnight (Part 2)
As seen in the previous exercise, the time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write two functions that each take a time of day in 24 hour format, and return the number of minutes before and after midnight, respectively. Both functions should return a value in the range 0 through 1439.

You may not use Python's datetime module.

##### PEDAC #####

# Define Problem
1. Input: string
   Output: integer representing minutes before or after midnight

2. Explicit rules

Explicit rules:
   - Create two functions:  one that returns number of minutes before midnight
     and the other that returns number of minutes after midnight
   - The input string represents time of day in 24-hr format (hh:mm)
   - Integer returned from both functions should be between 0 and 1439
   - Cannot use datetime module

# Test Cases
print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

# Algorithm
1. Parse input string into the 2-digit hour portion and 2-digit minute portion. 
   Convert hours and minutes strings to integers.
2. For time after midnight: multiply input hour by 60 to convert to minutes, then add the input minutes portion.
3. For time before midnight: first subtract input hours from 23 and minutes from 60. Then multiply the resulting hours by 60 and add the minutes