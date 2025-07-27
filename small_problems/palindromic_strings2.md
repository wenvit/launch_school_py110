Palindromic Strings (Part 2) Problem statement
Write another function that returns True if the string passed
as an argument is a palindrome, or False otherwise. This time, 
however, your function should be case-insensitive, and should 
ignore all non-alphanumeric characters. If you wish, you may 
simplify things by calling the is_palindrome function you 
wrote in the previous exercise.


##### PEDAC #####

# Define problem
1. Input: string
   Output: True or False (boolean)

2. Explicit rules:
   - Palindrome defined as a string that reads the same forward and
     backward.
   - Function returns True if string passed as argument is a palindrome,
     False otherwise.
   - Case does not matter, that is, upper and lower case letters should be
     treated the same when determining whether or not string is palindrome.
   - Non-alphanumeric characters should be ignored, that is, only alpha
     characters and digits should be considered when determining whether
     or not string is palindrome.

3. Implicit rules:
   - Input string may consist of multiple words and may contain digits,
     spaces, punctuation.

# Test cases - provided

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True
print(is_real_palindrome('Madam') == True)           # True
print(is_real_palindrome("Madam, I'm Adam") == True) # True

# Data structures
 - String will be passed as argument to function.
 - Function will return boolean True or False

# Algorithm
1. "Clean" the input string by creating a new string with any
   non-alphanumeric characters removed and all cased
   characters set to lower case.
2. Create a new string from all characters in the cleaned
   string in reverse order.
3. Compare the reversed string to the cleaned string.
   If the strings are equal, return True. If the strings are
   not equal, return False.
