'''
Practice Problem 1
Given the tuple:

fruits = ("apple", "banana", "cherry", "date", "banana")

How would you count the number of occurrences of "banana" in the tuple?

'''
# Solution:

# 1. apply count method
# 2. use a for loop with a counter that increments when
#    banana is encountered 

# fruits = ("apple", "banana", "cherry", "date", "banana")

# Solution 1
# print(fruits.count('banana'))

# Solution 2

# banana_counter = 0

# for item in fruits:
#     if item == 'banana':
#         banana_counter +=1

# print(banana_counter)

# - - - - - - - - - - - -- - 

# Practice Problem 2

# What is the set's length? Try to answer without running the code.

# numbers = {1, 2, 3, 4, 5, 5, 4, 3}
# print(len(numbers))

# Solution
# 5 because sets contain unique values 

# - - - - - - - - - - - - - -

# Practice Problem 3
# Given two sets:

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# How would you obtain a set that contains all the unique values from both sets?

# Solution:
# Two ways to find union of sets

# print(a | b)
# print(a.union(b))

# - - - - - - - - - - - - - -
# Practice Problem 5
# Calculate the total age given the following dictionary:

# ages = {
#     "Herman": 32,
#     "Lily": 30,
#     "Grandpa": 5843,
#     "Eddie": 10,
#     "Marilyn": 22,
#     "Spot": 237,
# }

# Solution:
# 1. loop over dict values and add age to total
# 2. use sum function

# Solution 1
# total_age = 0

# for person_yrs in ages.values():
#     total_age += person_yrs

# Solution 2

# total_age = sum(ages.values())

# print(total_age)

# - - - - - - - - - - - - - -
# Practice Problem 6
# Determine the minimum age from the above ages dictionary.

# min_age = min(ages.values())

# print(min_age)

# - - - - - - - - - - - - - -

# Practice Problem 7
# What would the following code output? Try to answer without running the code.

# words = ['ant', 'bear', 'cat']
# selected_words = []
# for word in words:
#     if len(word) > 3:
#         selected_words.append(word)

# print(selected_words)

# Solution
# ['bear']

# - - - - - - - - - - - - - -

# Practice Problem 8
# Given the following string, create a dictionary that 
# represents the frequency with which each letter occurs. 
# The frequency count should be case-sensitive. Order doesn't 
# matter

statement = "The Flintstones Rock"

# Pretty printed for clarity
# {
#     'T': 1,
#     'h': 1,
#     'e': 2,
#     'F': 1,
#     'l': 1,
#     'i': 1,
#     'n': 2,
#     't': 2,
#     's': 2,
#     'o': 2,
#     'R': 1,
#     'c': 1,
#     'k': 1
# }

# Solution:
# create a set from statement in order to eliminate duplicate letters
# remove spaces from statement_set
# using dictionary comprehension, loop over characters in 
# how to maintain original order though?

# statement_set = set(statement.replace(' ', ''))

# dict_count = {

#     char: statement.count(char)
#     for char 
#     in statement_set

# }

# another way based on LS solution

# statement_no_spaces = statement.replace(' ', '')
# dict_count = {}

# for char in statement_no_spaces:
#     dict_count[char] = dict_count.get(char, 0) + 1


# print(dict_count)

# - - - - - - - - - - - - - -

# Practice Problem 9
# What is the return value of the list comprehension below? 
# Try to answer without running the code.

#print([num for num in [1, 2, 3] if num > 1])

# Solution
# [2, 3]

# - - - - - - - - - - - - - -
# Practice Problem 10
# What does the following code print and why?

# dictionary = {'a': 'ant', 'b': 'bear'}
# print(dictionary.popitem())
# print(dictionary)

# Solution
# This will print {'b': 'bear'}. The popitem() removes & returns key-value pair
# from a dictionary based on last in/first out. It mutates the dictionary.

# - - - - - - - - - - - - - - 
# Practice Problem 11
# What does the following code return? Try to answer without running the code.

# lst = [1, 2, 3, 4, 5]
# print(lst[:2])

# Solution
# [1, 2]

# - - - - - - - - - - - - - -

# Practice Problem 12
# What would be the output of the below code? 
# Try to answer without running the code.

# frozen = frozenset([1, 2, 3, 4, 5])
# frozen.add(6)
# print(frozen)