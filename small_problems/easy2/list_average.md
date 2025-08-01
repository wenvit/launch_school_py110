List Average

Write a function that takes one argument, a list of integers, and returns the average of all the integers in the list, rounded down to the integer component of the average. The list will never be empty, and the numbers will always be positive integers.

##### PEDAC #####

# Define Problem

1. Inputs: list of integers
   Outputs: average of integers

2. Explicit rules: 
   - Return average of all integers in list
   - Return value should be rounded down to the nearest integer
   - List will never be empty
   - List contains only positive numbers

# Test Cases

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True

# Algorithm
1. Determine length of input list. This will be divider in average calculation.
2. Calculate sum of integers in list using sum function on list.
3. Divide sum of integers by length of list. Use integer division (//) so 
   to round result down to nearest integer.