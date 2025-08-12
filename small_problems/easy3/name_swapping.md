Name Swapping
Write a function that takes a string argument consisting of a first name, a space, and a last name. The function should return a new string consisting of the last name, a comma, a space, and the first name.

You may assume that the names don't include middle names, initials, or suffixes ("Jr.", "Sr.").

##### PEDAC #####

# Define Problem
1. Inputs: string consisting of first name, space, last name
   Outputs: new string consisting of last name, comma, space, first name

2. Explicit rules
   - input string consists of first name, space, last name
   - output string should have last name, comma, space, first name
   - Assume names don't include middle names, initials, suffixes


# Test Cases
print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

# Data Structures
Strings
Possible use of lists for interim processing steps

# Algorithm
1. Split input string along spaces. Using `split` method for this returns a list
2. Return new string with names reversed. Access the list elements using indexing
   then concatenate words in new string using `join` method

