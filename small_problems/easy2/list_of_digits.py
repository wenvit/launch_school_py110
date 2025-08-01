'''
List of Digits Problem Statement
Write a function that takes one argument, a positive integer, 
and returns a list of the digits in the number.

'''

def digit_list(input_int):

    digit_list = []

    while input_int > 0:
        input_int, remainder = divmod(input_int, 10)
        digit_list.append(remainder)

    return digit_list

print(digit_list(12345))


# print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
# print(digit_list(7) == [7])                       # True
# print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
# print(digit_list(444) == [4, 4, 4])               # True