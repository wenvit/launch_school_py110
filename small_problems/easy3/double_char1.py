'''
Double Char (Part 1)
Write a function that takes a string, doubles every character in the string, 
then returns the result as a new string.

'''
# original solution

# def repeater(input_str):
#     repeated_str = ''

#     for char in input_str:
#         repeated_str += char * 2
#     return repeated_str


# another way
def repeater(input_str):

    return ''.join([char * 2 for char in input_str])

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
