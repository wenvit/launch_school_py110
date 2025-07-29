'''
Convert a Number to a String Problem Statement
In the previous two exercises, you developed functions 
that convert simple numeric strings to signed integers. 
In this exercise and the next, you're going to reverse 
those functions.

Write a function that converts a non-negative integer 
value (e.g., 0, 1, 2, 3, and so on) to the string 
representation of that integer.

You may not use any of the standard conversion functions 
available in Python, such as str. Your function should 
do this the old-fashioned way and construct the string 
by analyzing and manipulating the number.

'''

def map_digits(digit):

    int_to_str_mapper = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
    }

    return int_to_str_mapper[digit]

def integer_to_string(number):
    list_of_str_digits = []

    if number == 0:
        return map_digits(number)
    else:
        while number > 0:
            digit = number % 10
            string_digit = map_digits(digit)
            list_of_str_digits.insert(0, string_digit)
            number = number // 10

        return ''.join(list_of_str_digits)

# adding repr() to test cases to see string output

print(repr(integer_to_string(4321)))
print(integer_to_string(4321) == "4321")              # True

print(repr(integer_to_string(0)))
print(integer_to_string(0) == "0")                    # True

print(repr(integer_to_string(5000)))
print(integer_to_string(5000) == "5000")              # True

print(repr(integer_to_string(1234567890)))
print(integer_to_string(1234567890) == "1234567890")  # True