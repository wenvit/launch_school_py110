
'''

Searching 101 Problem Statement
Write a program that solicits six (6) numbers 
from the user and prints a message that describes whether 
the sixth number appears among the first five.

'''

# Code implementation

input_labels = ['1st', '2nd', '3rd', '4th', '5th', 'last']
input_nums = []

for label in input_labels:
    num = input(f'Enter the {label} number: ')
    input_nums.append(num)

if input_nums[-1] in input_nums[:5]:
    print(f'{input_nums[-1]} is in '
          f"{', '.join(input_nums[:5])}.")
else:
    print(f"{input_nums[-1]} isn't in "
          f"{', '.join(input_nums[:5])}.")
    
# Test cases - provided
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 17

# 17 is in 25,15,20,17,23.

# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 18

# 18 isn't in 25,15,20,17,23.