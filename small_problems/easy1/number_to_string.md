Convert a Number to a String Problem Statement
In the previous two exercises, you developed functions that convert simple numeric strings to signed integers. In this exercise and the next, you're going to reverse those functions.

Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string representation of that integer.

You may not use any of the standard conversion functions available in Python, such as str. Your function should do this the old-fashioned way and construct the string by analyzing and manipulating the number.

##### PEDAC #####

# Define problem
1. Input: positive integer
   Output: string of corresponding digits

2. Explicit rules:
 - Input integer is non-negative (positive)
 - Cannot use any python functions to convert the integer to 
   an string, that is, cannot use str() constructor function
  
# Test cases - provided

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

# Data structures
 - String inputs
 - Integer output
 - Dictionary to map integers to strings
 - List to store interim converted strings while the integer
   is being processed

# Algorithm
1. Create a dictionary mapping integers to corresponding strings
2. Strip off the individual digits from the number going from
   right (ones digit) to left as follows:
   - number % 10 yields the ones digit, which is converted to a 
     string using the dictionary mapping, then stored in a list
   - number // 10 --> number2
   - number2 % 10 yields tens digit, which is converted to a 
     string using the dict mapping, then stored in a list
   - number2 // 10 --> number3 
   - number3 % 10 yields 100s digit, converted to string using
     dict mapping, then stored in a list
   and so on through all the digits in the integer



