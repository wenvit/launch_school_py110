'''

Searching 101 Problem Statement
Write a program that solicits six (6) numbers 
from the user and prints a message that describes whether 
the sixth number appears among the first five.

Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.


Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.

'''

##### PEDAC #####

# Define problem
# 1. Inputs: 6 numbers from user input (strings)
#    Outputs: message indicating whether or not 6th number
#             is one of the first 5 numbers entered
# 2. Explicit rules:
#     - User is asked to input 6 numbers (input function returns
#       strings by default)
#     - If 6th number is one of the first 5 numbers, message
#       is output indicating the 6th number is in the list.
#       If not, an alternate message is output indicating
#       that the 6th number is not among the the first 5.

# Test cases - provided

# Data structures
# 1. Input values will be strings. No need to convert to integers because
#    we're not doing any math with them.
# 2. Use list to store all values for searching.

# Algorithm
# 1. Ask user to input 6 numbers.
# 3. Append input values to list.
# 4. Search for 6th input value among first 5 values in list.
# 5. Print message indicating whether or not 6th value is one of
#    first 5 values.

# Code implementation

# input_labels = ['1st', '2nd', '3rd', '4th', '5th', 'last']
# input_nums = []

# for label in input_labels:
#     num = input(f'Enter the {label} number: ')
#     input_nums.append(num)

# if input_nums[-1] in input_nums[:5]:
#     print(f'{input_nums[-1]} is in '
#           f"{', '.join(input_nums[:5])}.")
# else:
#     print(f"{input_nums[-1]} isn't in "
#           f"{', '.join(input_nums[:5])}.")

# - - - - - - - - - - - - - -

'''
Palindromic Strings (Part 1)
Write a function that returns True if the string passed as an argument
is a palindrome, False otherwise. A palindrome reads the same forwards
and backwards. For this problem, the case matters and all characters matter.

'''

##### PEDAC #####

# Define problem
# 1. Input: string
#    Output: True or False (boolean)

# 2. Explicit rules:
#    - Palindrome defined as a string that reads the same forward and
#      backward.
#    - Function returns True if string passed as argument is a palindrome,
#      False otherwise.
#    - Case matters
#    - All characters matter
#
# 3. Implicit rules:
#    - Input string may consist of multiple words and may contain digits,
#      spaces, punctuation.

# Test cases - provided

# All of these examples should print True
#  - print(is_palindrome('madam') == True)
#  - print(is_palindrome('356653') == True)
#  - print(is_palindrome('356635') == False)
#  - print(is_palindrome('Madam') == False)
#  - print(is_palindrome("madam i'm adam") == False)

# Data structures
# - String will be passed as argument to function.
# - Function will return boolean True or False

# Algorithm
# 1. Create a new string from all characters in the argument string
#    in reverse order. Because case and all characters matter, the
#    argument string will be reversed as is with no pre-processing steps
#    needed (e.g., no need to remove spaces or other characters or
#    treat upper case letters).
# 2. Compare the reversed string to the argument string.
#    If the strings are equal, return True. If the strings are
#    not equal, return False.

# Code implementation

# def is_palindrome(input_string):

#     reversed_string = input_string[::-1]
#     return input_string == reversed_string

# print(is_palindrome('madam') == True)
# print(is_palindrome('356653') == True)
# print(is_palindrome('356635') == False)
# print(is_palindrome('Madam') == False)
# print(is_palindrome("madam i'm adam") == False)