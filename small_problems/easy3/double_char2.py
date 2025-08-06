'''
Double Char (Part 2)
Write a function that takes a string, doubles every consonant in the string, 
and returns the result as a new string. The function should not double vowels 
('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.

'''

VOWELS = ['a', 'e', 'i', 'o', 'u']

def is_consonant(input_char):

    result = (input_char not in VOWELS) and \
    (not input_char.isdigit()) and \
    (not input_char.isspace()) and \
    (input_char.isalpha())
    
    return result

def double_consonants(input_str):

    repeated_str = ''

    for char in input_str:
        if is_consonant(char):
            repeated_str += char * 2
        else:
            repeated_str += char
    return repeated_str

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")