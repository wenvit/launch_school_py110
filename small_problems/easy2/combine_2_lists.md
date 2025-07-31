Combine Two Lists Problem Statement

Write a function that combines two lists passed as arguments and returns a new list that contains all elements from both list arguments, with each element taken in alternation.

You may assume that both input lists are non-empty, and that they have the same number of elements.

##### PEDAC #####

# Define Problem

1. Inputs: two lists
   Outputs: new list with elements of both lists 

2. Explicit rules:
  - New list should contain elements of original lists in 
    alternating order.
  - Each input list contains same number of elements.
  - Each input list is non-empty.
   

# Test Cases

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

# Data Structures

Lists for inputs & outputs

# Algorithm

1. Initialize empty list object to contain new combined output list.
2. Loop over the list indices and append list1 and list2 elements
   to the new list in alternating order.