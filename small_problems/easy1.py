'''
Searching 101
Write a program that solicits six (6) numbers 
from the user and prints a message that describes whether 
the sixth number appears among the first five.

Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.


Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.

'''

##### PEDAC #####

# Define problem
# 1. Inputs: 6 numbers from user input (strings)
#    Outputs: message indicating whether or not 6th number
#             is one of the first 5 numbers entered
# 2. Explicit rules: 
#     - User is asked to input 6 numbers (input function returns
#       strings by default)
#     - If 6th number is one of the first 5 numbers, message
#       is output indicating the 6th number is in the list. 
#       If not, an alternate message is output indicating
#       that the 6th number is not among the the first 5.
#  

# Test cases - provided 

# Data structures
# 1. Input values will be strings. No need to convert to integers because
#    we're not doing any math with them.
# 2. Use list to store all values for searching.

# Algorithm
# 1. Ask user to input 6 numbers. Convert to integers. Note: not doing math
#    but integers will simplify print statement.
#    Use `for` loop for this.
# 2. Initialize empty list to store input integers.
# 3. Append input values to list.
# 4. Search for 6th value among first 5 values in list.
# 5. Print message indicating whether or not 6th value is one of
#    first 5 values.

# Code implementation

input_labels = ['1st', '2nd', '3rd', '4th', '5th', 'last']
input_nums = []

for label in input_labels:
    num = int(input(f'Enter the {label} number: '))
    input_nums.append(num)

if input_nums[-1] in input_nums[:5]:
    print(f'{input_nums[-1]} is in '
          f'{input_nums[0]}, '
          f'{input_nums[2]}, '
          f'{input_nums[3]}, '
          f'{input_nums[4]}, '
          f'{input_nums[5]}.')
else:
    print('nope')


