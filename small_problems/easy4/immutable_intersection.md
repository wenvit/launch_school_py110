Immutable Intersection
Transform two lists into frozen sets and find their common elements.

##### PEDAC #####

# Define Problem
1. Inputs: lists
   Outputs: set

   Explicit rules: 
   - Input two lists
   - Convert the lists to frozen sets and return new frozen set that is the intersection of both sets, i.e., the values common to both sets


# Test Cases
list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True

# Data Structures
Lists
Frozen sets

# Algorithm

1. Convert lists to frozen sets
2. Find elements common to both frozen sets