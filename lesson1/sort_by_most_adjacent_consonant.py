'''
Sort Strings by Most Adjacent Consonants
Given a list of strings, sort the list based on the highest number 
of adjacent consonants a string contains and return the sorted list. 
If two strings contain the same highest number of adjacent consonants, 
they should retain their original order in relation to each other. 
Consonants are considered adjacent if they are next to each other 
in the same word or if there is a space between two consonants 
in adjacent words.

Tasks
You are provided with the problem description above. Your tasks for this step are:

Make notes of your mental model for the problem, including:
inputs and outputs.
explicit and implicit rules.
Write a list of clarifying questions for anything that isn't clear.

'''
######### PEDAC #############

### Task 1 --> rules & questions

# Input: list of strings
# Output: list of strings sorted based on highest number of adjacent consonants.
#         Note that it's not clear from problem statement if output is new list
#         or same list (sorted in place)

# Explicit rules:
# 1. Strings sorted based on highest number of adjacent consonants contained in 
#    the string.
# 2. Two strings containing the same number of adjacent consonants retain their original
#    order.
# 3. Adjacent consonants defined as being next to each other disregarding any spaces
#    in between.

# Implicit rules:
# 1. Sort from highest to lowest number of consonants. This is based on reviewing
#    test cases.
# 2. Strings can contain multiple words.
# 3. If a character is not a vowel, it is considered a consonant (disregarding spaces).
#    It's not clear from the problem description or test cases how digits, punctuation, 
#    or other non-alpha characters should be handled so I am making 
#    this assumption.

# Questions:
# 1. Should a new sorted list be returned? Or should the original list be sorted in place?
#    Not clear from test cases. I will return a new list.
# 2. Is case important? Not clear from test cases so I will ignore.
# 3. How should non-alpha characters (not including spaces) be handled? Not clear so I'm
#    ignoring this for now.

#### Task 2 --> test cases

# my_list = ['aa', 'baa', 'ccaa', 'dddaa']
# print(sort_by_consonant_count(my_list))
# # ['dddaa', 'ccaa', 'aa', 'baa']

# my_list = ['can can', 'toucan', 'batman', 'salt pan']
# print(sort_by_consonant_count(my_list))
# # ['salt pan', 'can can', 'batman', 'toucan']

# my_list = ['bar', 'car', 'far', 'jar']
# print(sort_by_consonant_count(my_list))
# # ['bar', 'car', 'far', 'jar']

# my_list = ['day', 'week', 'month', 'year']
# print(sort_by_consonant_count(my_list))
# # ['month', 'day', 'week', 'year']

# my_list = ['xxxa', 'xxxx', 'xxxb']
# print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

#### Task 3 --> data structures

# Based on problem description, we'll be using lists for input & output. 
# A nested list may be useful for the interim sorting step because it would maintain 
# the original order of the strings.


#### Task 4 --> algorithm

# 1. Determine number of adjacent consonants in each string.
#    - initialize a string containing all vowels --> vowels = 'aeiou'
#    - initialize variables for counting number of adjacent consonants and
#      keeping track of maximum number of adjacent consonants for each string
#    - remove any spaces from each string, assign to a new variable
#    - initialize empty list that will be a nested list containing the 
#      the strings with their max adjacent consonants
#    - loop through strings in list
#    - loop through characters in each string (with spaces removed), 
#      if character is not in the vowels string, increment counter by 1. 
#      If current count > max count, reassign max count to current count
#    - if next character in string is a vowel, reset counter to 0
#    - append a list containing the string and the max 
#      number of adjacent consonants to the nested list
#    - for next string in list, reset both counter and max counters to 0
# 
# 2. Sort strings by sorting nested list based on the second element (index 1)
#    which contains the max adjacent consonant count
#    - initialize list for holding the sorted nested list elements to the first element of the 
#      unsorted nested list (i.e. nested list at index 0)
#    - loop over the remaining nested lists in the unordered nested list (i.e., start with index 1)
#    - for each of inner nested lists, compare the integer at index 1 representing the max adjacent
#      consonants to the integer at index 1 of the lists already contained in sorted_strings
#    - insert the list into the appropriate spot of the sorted_strings list
#      based on the max adjacent consonant so that the lists appear in the nested
#      list from high to low. 


##### Task 5 --> implement code

VOWELS = 'aeiou'

def is_consonant(char):
    return char not in VOWELS


# def sort_nested_list(input_nested_list):
#     sorted_list = input_nested_list[0]

#     print(f'sorted_list: {sorted_list}')

#     for lst in input_nested_list[1:]:
#         for lst2 in sorted_list:
#             if lst[1] > 




#     return sorted_list



def sort_by_consonant_count(input_list):
    lists_with_consonant_counts = []

    for string in input_list:
        consonant_count = 0
        max_consonant_count = 0
        string_no_spaces = string.replace(' ', '')
        last_index = len(string_no_spaces) - 1

        for idx in range(len(string_no_spaces)):
            if is_consonant(string_no_spaces[idx]):
                consonant_count += 1
            if consonant_count > max_consonant_count:
                max_consonant_count = consonant_count
            if (idx != last_index) and not is_consonant(string_no_spaces[idx + 1]):
                consonant_count = 0

        lists_with_consonant_counts.append([max_consonant_count, string])

    return sorted(lists_with_consonant_counts, reverse=True)


# my_list = ['can can', 'toucan', 'batman', 'salt pannnnnn', 'aaaaaaa', 'aeiou', '']
# nested = sort_by_consonant_count(my_list)
# print(nested)

#sort_nested_list(nested)

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# # ['dddaa', 'ccaa', 'aa', 'baa']








# # ['salt pan', 'can can', 'batman', 'toucan']

