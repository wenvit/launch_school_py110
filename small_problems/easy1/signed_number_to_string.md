Convert a Signed Number to a String Problem Statement
In the previous exercise, you developed a function that converts 
non-negative numbers to strings. In this exercise, you're going 
to extend that function by adding the ability to represent negative 
numbers as well.

Write a function that takes an integer and converts it to a 
string representation.

You may not use any of the standard conversion functions available in 
Python, such as str. You may, however, use integer_to_string from 
the previous exercise.

##### PEDAC #####

# Define problem
1. Input: integer
   Output: string of corresponding digits with + or -

2. Explicit rules:
 - Input integer can be positive or negative
 - Cannot use any python functions to convert the integer to 
   an string, that is, cannot use str() constructor function

3. Implicit rules:
 - Strings representing positive numbers should start with +
 - Strings representing negative numbers should start with -
 - String for 0 doesn't have sign
  
# Test cases - provided

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True

# Data structures
 - String inputs
 - Integer output
 - Dictionary to map integers to strings
 - List to store interim converted strings while the integer
   is being processed

# Algorithm
1. If number is positive, return a string consisting of a + concatenated 
   with the string returned by original integer_to_string function.
2. If number is negative, pass absolute value of number to original
   integer_to_string function and add a - character to returned string.
3. If number is 0, return '0'


