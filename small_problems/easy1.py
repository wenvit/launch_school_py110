'''

Searching 101 Problem Statement
Write a program that solicits six (6) numbers 
from the user and prints a message that describes whether 
the sixth number appears among the first five.

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
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 17

# 17 is in 25,15,20,17,23.

# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 18

# 18 isn't in 25,15,20,17,23.

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
Palindromic Strings (Part 1) Problem Statement
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

# - - - - - - - - - - - - - -


'''
Palindromic Strings (Part 2) Problem statement
Write another function that returns True if the string passed
as an argument is a palindrome, or False otherwise. This time, 
however, your function should be case-insensitive, and should 
ignore all non-alphanumeric characters. If you wish, you may 
simplify things by calling the is_palindrome function you 
wrote in the previous exercise.
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
#    - Case does not matter, that is, upper and lower case letters should be
#      treated the same when determining whether or not string is palindrome.
#    - Non-alphanumeric characters should be ignored, that is, only alpha
#      characters and digits should be considered when determining whether
#      or not string is palindrome.
#
# 3. Implicit rules:
#    - Input string may consist of multiple words and may contain digits,
#      spaces, punctuation.

# Test cases - provided

# print(is_real_palindrome('madam') == True)           # True
# print(is_real_palindrome('356653') == True)          # True
# print(is_real_palindrome('356635') == False)         # True
# print(is_real_palindrome('356a653') == True)         # True
# print(is_real_palindrome('123ab321') == False)       # True
# print(is_real_palindrome('Madam') == True)           # True
# print(is_real_palindrome("Madam, I'm Adam") == True) # True

# Data structures
# - String will be passed as argument to function.
# - Function will return boolean True or False

# Algorithm
# 1. "Clean" the input string by creating a new string with any
#    non-alphanumeric characters removed and all cased
#    characters set to lower case.
# 2. Create a new string from all characters in the cleaned
#    string in reverse order.
# 3. Compare the reversed string to the cleaned string.
#    If the strings are equal, return True. If the strings are
#    not equal, return False.

# Code implementation

# def clean_string(input_string):
#     cleaned = ''

#     for char in input_string:
#         if char.isalnum():
#             cleaned += char.lower()
#     return cleaned

# def is_real_palindrome(input_string):

#     cleaned_string = clean_string(input_string)
#     reversed_string = cleaned_string[::-1]

#     return reversed_string == cleaned_string

# print(is_real_palindrome('madam') == True)           # True
# print(is_real_palindrome('356653') == True)          # True
# print(is_real_palindrome('356635') == False)         # True
# print(is_real_palindrome('356a653') == True)         # True
# print(is_real_palindrome('123ab321') == False)       # True
# print(is_real_palindrome('Madam') == True)           # True
# print(is_real_palindrome("Madam, I'm Adam") == True) # True

# - - - - - - - - - - - - - -
'''
Running Totals Problem Statement
Write a function that takes a list of numbers and returns a list
with the same number of elements, but with each element's value
being the running total from the original list.
'''

##### PEDAC #####

# Define problem
# 1. Input: list of integers
#    Output: new list of integers

# 2. Explicit rules:
#    - New list has same number of elements
#    - Each element in new list is the running total from the
#      original list
#
# 3. Implicit rules:
#   - Order is important. Each element in the new list represents
#     the running or cumulative sum of all elements up to and
#     and including the element at the same index in the original list

# Test cases - provided

# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True

# Data structures
# lists of integers

# Algorithm
# 1. Initialize new empty list object for storing the transformed elements
#    of the original list.
# 2. Initialize a variable for storing the cumulative sum of list elements.
# 3. Loop over original list passed as an argument. For each element of the
#    list, add the element (i.e., integer at the current index position)
#    to the previous cumulative sum. Append the cumulative sum to the
#    new list.


# Code implementation

# def running_total(input_list):
#     cum_total_list = []
#     cum_total = 0

#     for num in input_list:
#         cum_total += num
#         cum_total_list.append(cum_total)

#     return cum_total_list


# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True
# - - - - - - - - - - - - - -
'''
Letter Counter (Part 1) Problem Statement
Write a function that takes a string consisting of zero or more
space-separated words and returns a dictionary that shows the
 number of words of different sizes.

Words consist of any sequence of non-space characters.
'''

##### PEDAC #####

# Define problem
# 1. Input: string of zero or more space-separated words
#    Output: dictionary showing number of words of different sizes

# 2. Explicit rules:
#    - Input string can contain zero or more words.
#    - Words are separated by spaces.
#    - Words consist of any sequence of non-space characters.

# 3. Implicit rules:
#    - Dictionary keys are the word length, and values are the
#      number of words of that length.
#    - Punctuation and other non-space characters impact word length.
#      For instance commas, periods, apostrophes should be added to
#      the length of words they are next to or part of (if there are no spaces
#      separating the word and non-alpha character).
#    - Order of the key-value pairs doesn't matter.
#    - An empty string should result in an empty dictionary.

# Test cases - provided

# All of these examples should print True

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

# string = 'Humpty Dumpty sat on a wall'
# print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

# print(word_sizes('') == {})

# Data structures
#  - String inputs
#  - Dictionary outputs
#  - Use a list for the interim step of splitting the string into
#    individual words for looping over.

# Algorithm
# 1. Initialize empty dictionary for result.
# 2. Split input string based on spaces into individual words.
#    Put words in list.
# 3. Loop over list of words. For each word:
#     - Count length of word
#     - Add key of word length to dictionary if it doesn't already exist
#       and set value for that key to 1
#       If key of word length is already in dictionary, increment value
#       for that key by 1


# Code implementation

# def word_sizes(input_string):
#     result = {}

#     words = input_string.split()

#     for word in words:
#         dict_key = len(word)
#         result[dict_key] = result.get(dict_key, 0) + 1

#     return result

# All of these examples should print True

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

# string = 'Humpty Dumpty sat on a wall'
# print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

# print(word_sizes('') == {})

# - - - - - - - - - - - - - -

'''
Letter Counter (Part 2) Problem Statement
Modify the word_sizes function from the previous exercise to exclude
non-letters when determining word size. For instance, the word 
size of "it's" is 3, not 4.

'''

##### PEDAC #####

# Define problem
# 1. Input: string of zero or more space-separated words
#    Output: dictionary showing number of words of different sizes

# 2. Explicit rules:
#    - Input string can contain zero or more words.
#    - Words are separated by spaces.
#    - Words consist of any sequence of non-space characters.

# 3. Implicit rules:
#    - Dictionary keys are the word length, and values are the
#      number of words of that length.
#    - Punctuation and other non-space characters should not be counted 
#      when determining word length.
#    - Order of the key-value pairs doesn't matter.
#    - An empty string should result in an empty dictionary.

# Test cases - provided

# All of these examples should print True

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 3})

# string = 'Humpty Dumpty sat on a w@ll'
# print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

# print(word_sizes('') == {})

# Data structures
#  - String inputs
#  - Dictionary outputs
#  - Use a list for the interim step of splitting the string into
#    individual words for looping over.

# Algorithm
# 1. Initialize empty dictionary for result.
# 2. "Clean" the string by removing any non-alpha characters that aren't
# #  spaces.
# 2. Split input string based on spaces into individual words.
#    Put words in list.
# 3. Loop over list of words. For each word:
#     - Count length of word
#     - Add key of word length to dictionary if it doesn't already exist
#       and set value for that key to 1
#       If key of word length is already in dictionary, increment value
#       for that key by 1


# Code implementation

# def clean_string(input_string):
#     cleaned = ''

#     for char in input_string:
#         if char.isalpha() or char.isspace():
#             cleaned += char.lower()
#     return cleaned

# def word_sizes(input_string):
#     result = {}

#     cleaned_string = clean_string(input_string)

#     words = cleaned_string.split()

#     for word in words:
#         dict_key = len(word)
#         result[dict_key] = result.get(dict_key, 0) + 1

#     return result

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 3})

# string = 'Humpty Dumpty sat on a w@ll'
# print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

# print(word_sizes('') == {})

# - - - - - - - - - - - - - -

'''
Letter Swap
Given a string of words separated by spaces, write a 
function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, 
and that the string will always contain at least one word. 
You may also assume that each string contains nothing but 
words and spaces, and that there are no leading, trailing, 
or repeated spaces.


'''
##### PEDAC #####

# Define problem
# 1. Input: string of words separated by spaces
#    Output: new string of words with first & last letters 
#            of every word swapped

# 2. Explicit rules:
#  - Every word contains at least one letter.
#  - String always contains at least one word.
#  - Each string contains nothing but words and spaces
#  - No leading, trailing, or repeated spaces

# 3. Implicit rules:
#  - Smallest word is one letter
#  - String will not contain digits, punctuation or other
#    non-alpha characters or spaces

# Test cases - provided

# print(swap('Oh what a wonderful day it is')
#       == "hO thaw a londerfuw yad ti si")  # True
# print(swap('Abcde') == "ebcdA")            # True
# print(swap('a') == "a")                    # True

# Data structures
#  - String inputs
#  - String output
#  - A list as interim structure for string manipulation

# Algorithm
# 1. Initialize an empty list for storing the swapped letter words.
# 2. Split string into words by the spaces. Put into another list.
# 2. Loop over each word in the list. Swap the first & last letters
#    of each word and append into the list for the swapped letter words.
# 3. Join the swapped-letter words separated by spaces into a new string.

# Code implementation

def swap(input_string):

    original_words = input_string.split()
    swapped_words = []

    if len(input_string) == 1:
        return input_string

    for word in original_words:
        if len(word) > 1:
            switcheroo = word[-1] + word[1:-1] + word[0]
            swapped_words.append(switcheroo)
        else:
            swapped_words.append(word)

    return ' '.join(swapped_words)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True









