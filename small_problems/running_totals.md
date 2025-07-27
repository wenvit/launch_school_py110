Running Totals Problem Statement
Write a function that takes a list of numbers and returns a list
with the same number of elements, but with each element's value
being the running total from the original list.


##### PEDAC #####

# Define problem
1. Input: list of integers
   Output: new list of integers

2. Explicit rules:
   - New list has same number of elements
   - Each element in new list is the running total from the
     original list

3. Implicit rules:
  - Order is important. Each element in the new list represents
    the running or cumulative sum of all elements up to and
    and including the element at the same index in the original list

# Test cases - provided

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

# Data structures
lists of integers

# Algorithm
1. Initialize new empty list object for storing the transformed elements
   of the original list.
2. Initialize a variable for storing the cumulative sum of list elements.
3. Loop over original list passed as an argument. For each element of the
   list, add the element (i.e., integer at the current index position)
   to the previous cumulative sum. Append the cumulative sum to the
   new list.

