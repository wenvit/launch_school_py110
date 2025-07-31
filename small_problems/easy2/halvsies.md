Halvsies Problem Statement

Write a function that takes a list as an argument and returns a list that contains two elements, both of which are lists. Put the first half of the original list elements in the first element of the return value and put the second half in the second element. If the original list contains an odd number of elements, place the middle element in the first half list

# Define problem
1. Inputs: list
   Outputs: list with two nested lists

2. Explicit rules
  - The output list should contain two nested lists. The first nested list should contain
    the first half of the original list elements. The second nested list should contain
    the second half of the original list elements.
  - If the original list contains an odd number of elements, put the middle element in the
    first half list.

3. Implicit rules
  - If the original list is empty, each half list in the output list should be empty.
  - If the original list has only one element, the single element should be placed in
    the first half list of the output list.

# Test Cases
All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

# Data structures
Input: list
Output: nested list

# Algorithm

1. Determine length of list. If length is even, divide in 2 (integer division) to determine 
   stop & start index numbers of original list elements to place in first & second half lists. 
   If length is odd, determine middle index which will be last index of first 
   half list with remaining elements placed in second half list.
2. Using the stop & start indexes determined in step 2, create new first half and second
   half lists with slicing applied to original list. 

4. Return list with nested first and second half lists.
5. Handle edge cases of empty list by returning list with two nested empty lists. 
   Also list with single element should return a list with single element in first
   half list and empty list in second half list.