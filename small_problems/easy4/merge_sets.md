Merge Sets
Given two lists, convert them to sets and return a new set which is the union of both sets.

##### PEDAC #####

# Define Problem
1. Inputs: lists
   Outputs: set

   Explicit rules: 
   - Input two lists
   - Convert the lists to sets and return new set that is the union of both sets

   Implicit rules:
   - Output will only contain unique values from both input lists because it's a set

# Test Cases

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True

# Data Structures
Lists
Sets

# Algorithm

1. Convert lists to sets
2. Join sets together into new set