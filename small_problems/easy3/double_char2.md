Double Char (Part 2)
Write a function that takes a string, doubles every consonant in the string, and returns the result as a new string. The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.

##### PEDAC #####

# Define Problem
1. Inputs: string
   Outputs: new string with each character that meets certain criteria doubled

2. Explicit Rules:
   - Output is a new string with every character from original string doubled except for the following:  vowels, whitespace, punctuation, digits 

3. Implicit Rules:
   - Empty string should return empty string

# Test Cases

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")

# Algorithm
1. Initialize empty string to store new string
2. Loop over string; check if character is a vowel, digit, punctuation, or whitespace; if not double character using * 2 operator.
3. Concatenate each doubled character to new string