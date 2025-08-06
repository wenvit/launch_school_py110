Double Char (Part 1)
Write a function that takes a string, doubles every character in the string, then returns the result as a new string.

##### PEDAC #####

# Define Problem
1. Inputs: string
   Outputs: new string with each character doubled

2. Explicit Rules:
   - Output is a new string with every character from original string doubled

3. Implicit Rules:
   - All characters, including spaces and punctuation, should be doubled in new string
   - Empty string should return empty string

# Test Cases

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

# Algorithm
1. Initialize empty string to store new string
2. Loop over string and double each character using * 2 operator.
3. Concatenate each doubled character to new string