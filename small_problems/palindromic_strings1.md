
Palindromic Strings (Part 1) Problem Statement
Write a function that returns True if the string passed as an argument
is a palindrome, False otherwise. A palindrome reads the same forwards
and backwards. For this problem, the case matters and all characters matter.

##### PEDAC #####

# Define problem
1. Input: string
    Output: True or False (boolean)

# 2. Explicit rules:
    - Palindrome defined as a string that reads the same forward and
      backward.
    - Function returns True if string passed as argument is a palindrome,
      False otherwise.
    - Case matters
    - All characters matter
#
 3. Implicit rules:
    - Input string may consist of multiple words and may contain digits,
      spaces, punctuation.

# Test cases - provided

# All of these examples should print True
  - print(is_palindrome('madam') == True)
  - print(is_palindrome('356653') == True)
  - print(is_palindrome('356635') == False)
  - print(is_palindrome('Madam') == False)
  - print(is_palindrome("madam i'm adam") == False)

# Data structures
 - String will be passed as argument to function.
 - Function will return boolean True or False

# Algorithm
1. Create a new string from all characters in the argument string
    in reverse order. Because case and all characters matter, the
    argument string will be reversed as is with no pre-processing steps
    needed (e.g., no need to remove spaces or other characters or
    treat upper case letters).
2. Compare the reversed string to the argument string.
    If the strings are equal, return True. If the strings are
    not equal, return False.


