Counting Up
Write a function that takes an integer argument and returns a list containing all integers between 1 and the argument (inclusive), in ascending order.

You may assume that the argument will always be a positive integer.

##### PEDAC ##### 

# Define Problem
1. Inputs: integer
   Outputs: list of integers

2. Explicit Rules:
   - Output list should contain all integers between 1 and the argument (inclusive)
     in ascending order
   - Assume input will always be positive integer.
3. Implicit Rules:
   - Input of 1 should return 1

# Test Cases
print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True


# Data Structures
Inputs: integer
Outputs: List of integers
Range to generate list of integers from 1 through input integer

# Algorithm
1. Create range starting with 1 through input integer + 1
2. Convert range to a list using list constructor function