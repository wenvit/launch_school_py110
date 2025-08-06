Reverse Number
Write a function that takes a positive integer as an argument and returns that number with its digits reversed.

##### PEDAC #####

# Define Problem
1. Inputs: positive integer
   Outputs: positive integer with digits reversed

2. Explicit rules:
   - Input is a positive integer
   - Return value is a positive integer with digits reversed

3. Implicit rules:
   - For a single digit integer, the return value should be the same number
   - If there are leading zeroes in the reversed integer, they should be dropped.

# Test Cases
print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True

# Data Structures
Integers

# Algorithm
1. Convert input integer to a string
2. Create a new string with the characters reversed
3. Convert the reversed string to an integer