Alphabetical Numbers
Write a function that takes a list of integers between 0 and 19 and returns a list of those integers sorted based on the English word for each number:

zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen

##### PEDAC #####

# Define Problem

1. Inputs: list of integers
   Outputs: list of integers sorted based on alphabetical words associated with integers
   Explicit rules: 
    - integers are between 0 and 19
    - the English words for each integer should be sorted alphabetically

# Test Cases

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True

# Data Structures:

Lists for inputs and outputs
Dictionary for mapping integers to English words

# Algorithm
1. Create a dictionary with integer keys with associated words as values
2. Create a dictionary with words as key and associated integers as values
3. Loop through input list, convert each integer to its word in a new list. Sort
   the list of words alphabetically.
4. Convert the sorted words to integers using the other dictionary mapping words to integers