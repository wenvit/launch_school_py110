Multiplicative Average
Write a function that takes a list of positive integers as input, multiplies all of the integers together, divides the result by the number of entries in the list, and returns the result as a string with the value rounded to three decimal places.

##### PEDAC #####

# Define Problem

1. Inputs: list of positive integers
   Outputs:  string representing average of integers

2. Explicit rules:
   - Input list contains positive integers
   - Integers in input list must be multiplied together and divided by number of entries.
   - Calculated average will be a float that must be rounded to 3 decimal places and 
     converted to a string


# Test Cases
All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

# Data Structures
Input list
Float for product and average
String for output

# Algorithm

1. Initialize float variable to 1 for storing cumulative product.
2. Find length of list, which will be used as denominator in average calculation
2. Loop through list and multiply each element with previous cumulative product
   using augmented assignment. Divide product by length of list.
3. Round final product to three decimal places and convert to string using
   str function.

