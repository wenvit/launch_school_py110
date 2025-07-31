Combining Lists Problem Statement

Write a function that takes two lists as arguments and 
returns a set that contains the union of the values 
from the two lists. You may assume that both arguments 
will always be lists.

##### PEDAC #####

# Define problem

1. Inputs: two lists
   Outputs: set containing union of values from both lists

2. Explicit rules
  - Return value of function is set containing unique value from both lists
  - Assume both arguments will always be lists

3. Implicit rules
  - List elements can be any type
  - I'm assuming an empty set should be returned if both lists are empty
  -

# Test cases - provided

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

- also check for cases of both input lists empty & one input list empty

# Data structures
 - list inputs
 - set output

# Algorithm

1. Initialize empty set object to contain elements from both lists
2. Initialize empty list object to contain concatenated lists
3. Loop through concatenated list and add each element to set. Set will automatically
   retain unique elements only.
3. Return set
