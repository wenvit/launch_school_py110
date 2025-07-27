Convert a String to a Signed Number

In the previous exercise, you developed a function 
that converts simple numeric strings to integers. 
In this exercise, you're going to extend that function 
to work with signed numbers.

Write a function that takes a string of digits and 
returns the appropriate number as an integer. 
The string may have a leading + or - sign; if the 
first character is a +, your function should 
return a positive number; if it is a -, your 
function should return a negative number. 
If there is no sign, return a positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions 
available in Python, such as int. You may, however, 
use the string_to_integer function from the previous exercise.

##### PEDAC #####

# Define problem
1. Input: string of digits
   Output: integer corresponding to the string

2. Explicit rules:
 - If string begins with + or no sign, a positive number should be returned.
 - If string begins with -, a negative number should be returned.
 - Cannot use any python functions to convert the string to 
   an integer, that is, cannot use int() constructor function
 - Assume all characters in the string are numeric.
 - Don't worry about invalid characters.

 3. Implicit rules:
  - Positive numbers are returned with no sign (no + sign)
  
# Test cases - provided

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

# Data structures
 - String inputs
 - Integer output
 - Dictionary to map string digits to integers
 - List to store numbers for summing
 - Range for powers of 10

# Algorithm
1. Strip off any leading + or - signs and set a variable indicating 
   that number returned should be positive or negative:  positive if
   leading character is + or no leading character; negative if leading
   character is -. 
2. Initialize an empty list object for storing integers corresponding
   to each string digit.
3. Create a dictionary to map string digits to integers.
4. Loop through the digits in the list working from left to right: 
   - Convert the digit to an integer based on the dictionary mapping
   - Multiply the integer by 10 raised to the power of the string length
     minus 1. Each subsequent digit would be multiplied by the string length
     minus 2, and so on down to the right-most digit multiplied by 10 to
     the power of 0. Store the results of these calculations in a list.
5. Sum the integers in the list.









