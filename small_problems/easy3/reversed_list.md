Reversed Lists
Write a function that takes a list as an argument and reverses its elements, in place. That is, mutate the list passed into the function. The returned object should be the same object used as the argument.

You may not use the list.reverse method nor may you use a slice ([::-1]).

##### PEDAC #####

# Define Problem
1. Input: list
   Output: same list object but with elements reversed

2. Explicit rules:
   - Input list must be mutated with same object returned (not new list)
   - Mutated returned list must have elements reversed
   - Cannot use list.reverse method or slicing [::-1]

3. Implicit rules:
   - If list has only one element (len = 1) or no elements ([]), same list is returned

# Test Cases

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True

# Data Structures
Input & output list
Range for looping

# Algorithem
1. Loop over list from index 0 to index of length - 1. Reassign each element based elements from last index to index 0. 
2. If empty list or len of list = 1, return list as is