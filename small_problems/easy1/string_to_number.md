
Convert a String to a Number

Write a function that takes a string of digits and
returns the appropriate number as an integer. 
You may not use any of the standard conversion 
functions available in Python, such as int. 
Your function should calculate the result by 
using the characters in the string.

For now, do not worry about leading + or - signs, 
nor should you worry about invalid characters; 
assume all characters are numeric.

##### PEDAC #####

# Define problem
1. Input: string of digits
   Output: integer corresponding to the string

2. Explicit rules:
 - Cannot use any python functions to convert the string to 
   an integer, that is, cannot use int() constructor function
 - Assume all characters in the string are numeric.
 - Don't worry about invalid characters.

# Test cases - provided

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

# Data structures
 - String inputs
 - Integer output
 - Dictionary to map string digits to integers
 - List to store numbers for summing
 - Range for powers of 10

# Algorithm
1. Initialize an empty list object for storing integers corresponding
   to each string digit.
2. Create a dictionary to map string digits to integers.
3. Loop through the digits in the string working from left to right: 
   - Convert the digit to an integer based on the dictionary mapping
   - Multiply the integer by 10 raised to the power of the string length
     minus 1. Each subsequent digit would be multiplied by the string length
     minus 2, and so on down to the right-most digit multiplied by 10 to
     the power of 0. Store the results of these calculations in a list.
2. Sum the integers in the list.









