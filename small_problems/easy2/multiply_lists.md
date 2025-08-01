Multiply Lists Problem Statement

Write a function that takes two list arguments, each containing a list of numbers, and returns a new list that contains the product of each pair of numbers from the arguments that have the same index. You may assume that the arguments contain the same number of elements.

##### PEDAC #####

# Define Problem
1. Inputs: two lists of numbers
   Outputs: new list containing product of each pair of numbers with same index

2. Explicit rules:
  - Pair of numbers with same index numbers from pair of input lists should be multiplied
  - Output list contains the products of pairs of numbers
  - Input lists contain same number of elements

# Test Cases
list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

# Data Structures
Inputs and outputs are all lists

# Algorithm

1. Initialize new list object to empty list for storing products of pairs of numbers
2. Find length of one of the input lists
3. Loop over list indexes, which is set using the range function with a stop integer
   equal to the length of the lists
4. For each index, multiply the element at that index in each list and append to the new list