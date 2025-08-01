How Many? Problem Statement

Write a function that counts the number of occurrences of each element in a given list. Once counted, print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").

##### PEDAC ##### 

# Define Problem
1. Inputs: list 
   Outputs: a listing of each element contained in list along with count of occurrences

2. Explicit rules:
  - Output should show each element contained in the original list along with a 
    count of the number of occurrences of that element.
  - Counts of strings are case-sensitive.

3. Implicit rules:
  - Order doesn't matter in output


# Test Cases
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# your output sequence may appear in a different sequence
car => 4
truck => 3
SUV => 1
motorcycle => 2

# Data Structures
Input: list
Output: dictionary with keys consisting of each list element and values
   for the counts of each element

# Algorithm
1. Initialize empty dictionary object to contain element & count pairs 
2. Loop through each list element, add as key to dictionary if not already
   there. Count occurrences and assign value to the key
3. If elemnt is already a key in dictionary, increment count of element (value)
   by one 