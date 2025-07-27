
'''
Convert a String to a Signed Number

In the previous exercise, you developed a function 
that converts simple numeric strings to integers. 
In this exercise, you're going to extend that function 
to work with signed numbers.

Write a function that takes a string of digits and 
returns the appropriate number as an integer. 
The string may have a leading + or - sign; if the 
first character is a +, your function should 
return a positive number; if it is a -, your 
function should return a negative number. 
If there is no sign, return a positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions 
available in Python, such as int. You may, however, 
use the string_to_integer function from the previous exercise.
'''

# Code implementation

# helper functions

def separate_sign_and_str(input_str):

    if input_str[0] in ['+', '-']:
        digit_str = input_str[1:]
        sign = input_str[0]
    else:
        digit_str = input_str
        sign = '+'

    return [sign, digit_str]

def map_digits(digit_str):

    string_to_int_mapper = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    return string_to_int_mapper[digit_str]

def string_to_signed_integer(num_string):

    nums = []
    power_transformation = []

    sign_and_str = separate_sign_and_str(num_string)
    powers = range(len(sign_and_str[1]) - 1, -1, -1)

    for digit in sign_and_str[1]:
        nums.append(map_digits(digit))

    for idx, num in enumerate(nums):
        if sign_and_str[0] == '+':
            power_transformation.append(num * 10**powers[idx])
        else:
            power_transformation.append(-num * 10**powers[idx])

    return sum(power_transformation)

# print(string_to_signed_integer("4321") == 4321)  # True
# print(string_to_signed_integer("-570") == -570)  # True
# print(string_to_signed_integer("+100") == 100)   # True
