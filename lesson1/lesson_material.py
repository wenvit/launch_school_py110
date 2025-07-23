##### Sequences
## increment list elements by 1
# numbers = [1, 2, 3, 4]

# idx = 0

# for idx in range(len(numbers)):
#     numbers[idx] += 1

# print(numbers)

##
# join method only works with strings
# one way to get around this with a list comprehension

# my_list = [1, 2, 3, 4]
# my_list_strings = [str(element) for element in my_list]
# print(my_list_strings)
# print(repr(', '.join(my_list_strings)))

## pop quiz: 

# dict1 = {
#     'apple': 'Produce',
#     'carrot': 'Produce',
#     'pear': 'Produce',
#     'broccoli': 'Produce',
#     }

# print(dict1)

# dict1['pear'] = 'fruit'
# dict1['broccoli'] = 'vegetable' 

# print(dict1)

## sets

# fruits = {'apple', 'banana', 'cherry'}
# fruits.add('grape')
# print(fruits)

# fruits.add('kiwi')
# print(fruits)

## enumerate

# colors = ["red", "green", "blue"]

# for idx, color in enumerate(colors):
#     print(idx, color)

# print(tuple(enumerate(colors)))

## unpacking

# numbers = [1, 2, 3, 4, 5]
# tup1 = (6, 7, 8)
# tup2 = (9, 10, 11)

# joined_collections = [*numbers, *tup1, *tup2]
# print(joined_collections)

## another example with ** operator

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}

# merged_dict = {**dict1, **dict2}

# print(merged_dict)


# PEDAC 

"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection
should be case-sensitive.
"""

# Test cases:

# Comments show expected return values
# palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
# palindrome_substrings("palindrome") # []
# palindrome_substrings("")           # []
# palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
# palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]

"""
input: string
output: list containing all palindromic substrings with 
        length >= 2 char(implicit requirement)

Rules:
Explicit requirements
 - Returned list should contain all substrings that are palindromes and have length 
   >= 2 characters
 - Palindromes are case-sensitive
Implicit requirements
 - If string doesn't contain any palindromic substrings, return empty list
 - If input string is empty, return empty list

"""

# - - - - - - - - - - - - - - 

####  we want to select the key-value pairs where the value is 'Fruit'.

# def select_fruit(input_dict):
#     output_dict = {}

#     for key, val in input_dict.items():
#         if val == 'Fruit':
#             output_dict[key] = val

#     return output_dict

# produce = {
#     'apple': 'Fruit',
#     'carrot': 'Vegetable',
#     'pear': 'Fruit',
#     'broccoli': 'Vegetable',
# }

# print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }

# - - - - - - - - - - - - - - 

# def double_numbers(numbers):
#     doubled_nums = []

#     for current_num in numbers:
#         doubled_nums.append(current_num * 2)

#     return doubled_nums


#### example of mutating original list

# def double_numbers():

#     for idx in range(len(my_numbers)):
#         my_numbers[idx] *= 2

#     return my_numbers


# my_numbers = [1, 4, 3, 7, 2, 6]
# print(double_numbers()) # [2, 8, 6, 14, 4, 12]
# print(my_numbers)                 # [1, 4, 3, 7, 2, 6]


# - - - - - - - - - - - - - -

# def double_odd_indexes(input_numbers):
#     doubled_nums = []

#     for idx in range(len(input_numbers)):
#         if idx % 2 == 1:
#             doubled_nums.append(input_numbers[idx] * 2)
#         else:
#             doubled_nums.append(input_numbers[idx])
            
#     return doubled_nums

# my_numbers = [1, 4, 3, 7, 2, 6]
# print(double_odd_indexes(my_numbers))  # [1, 8, 3, 14, 2, 12]

# # not mutated
# print(my_numbers)                      # [1, 4, 3, 7, 2, 6]

# - - - - - - - - - - - - - -

# Try coding a function that lets you multiply every list element by a 
# specified value. As with double_numbers, don't mutate the list, 
# but return a new list instead.

# def multiply(input_numbers, factor):
#     result = []

#     for number in input_numbers:
#         result.append(number * factor)
#     return result
    

# my_numbers = [1, 4, 3, 7, 2, 6]
# print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]
# print(my_numbers)