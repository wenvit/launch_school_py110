'''
Convert a Signed Number to a String Problem Statement
In the previous exercise, you developed a function that converts 
non-negative numbers to strings. In this exercise, you're going 
to extend that function by adding the ability to represent negative 
numbers as well.

Write a function that takes an integer and converts it to a 
string representation.

You may not use any of the standard conversion functions available in 
Python, such as str. You may, however, use integer_to_string from 
the previous exercise.

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

def signed_integer_to_string(number):
    if number > 0:
        return '+' + integer_to_string(number)
    elif number < 0:
        return '-' + integer_to_string(abs(number))
    else:
        return integer_to_string(number)


# adding repr() to test cases to see string output

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True