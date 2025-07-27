'''

Searching 101 Problem Statement
Write a program that solicits six (6) numbers 
from the user and prints a message that describes whether 
the sixth number appears among the first five.

'''

##### PEDAC #####

# Define problem
1. Inputs: 6 numbers from user input (strings)
   Outputs: message indicating whether or not 6th number
            is one of the first 5 numbers entered
2. Explicit rules:
    - User is asked to input 6 numbers (input function returns
      strings by default)
    - If 6th number is one of the first 5 numbers, message
      is output indicating the 6th number is in the list.
      If not, an alternate message is output indicating
      that the 6th number is not among the the first 5.

# Test cases - provided
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

# Data structures
1. Input values will be strings. No need to convert to integers because
   we're not doing any math with them.
2. Use list to store all values for searching.

# Algorithm
1. Ask user to input 6 numbers.
3. Append input values to list.
4. Search for 6th input value among first 5 values in list.
5. Print message indicating whether or not 6th value is one of
   first 5 values.
