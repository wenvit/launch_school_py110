
'''
Convert a String to a Number

Write a function that takes a string of digits and
returns the appropriate number as an integer. 
You may not use any of the standard conversion 
functions available in Python, such as int. 
Your function should calculate the result by 
using the characters in the string.

For now, do not worry about leading + or - signs, 
nor should you worry about invalid characters; 
assume all characters are numeric.

'''

# Code implementation

# helper functions

# def map_digits(digit_str):

#     string_to_int_mapper = {
#         '0': 0,
#         '1': 1,
#         '2': 2,
#         '3': 3,
#         '4': 4,
#         '5': 5,
#         '6': 6,
#         '7': 7,
#         '8': 8,
#         '9': 9,
#     }

#     return string_to_int_mapper[digit_str]

# def string_to_integer(num_string):

#     powers = range(len(num_string) - 1, -1, -1)
#     nums = []
#     power_transformation = []

#     for digit in num_string:
#         nums.append(map_digits(digit))

#     for idx, num in enumerate(nums):
#         power_transformation.append(num * 10**powers[idx])

#     return sum(power_transformation)

# print(string_to_integer("4321") == 4321)  # True
# print(string_to_integer("570") == 570)    # True