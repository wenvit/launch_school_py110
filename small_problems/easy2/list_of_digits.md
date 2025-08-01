List of Digits Problem Statement
Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.

##### PEDAC #####

# Define Problem
1. Inputs: positive integer
   Outputs: list of digits in integer

2. Explicit rules:
  - Argument is positive integer
  - List of digits in the number should be returned

# Test Cases

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

# Data Structures
Integer input
List of integers output

# Algorithm
1. Initialize empty list object for storing individual integer 
   digits as output.
2. Loop over original integer from right to left.
  - Remove rightmost digit by applying % 10 operation and getting the
  remainder. Append remainder to new list. 
  - Then apply integer division by 10 (// 10)
  - Continue these operations as long as the number > 0
