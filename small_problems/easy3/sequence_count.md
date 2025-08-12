Sequence Count
Create a function that takes two integers as arguments. The first argument is a count, and the second is the starting number of a sequence that your function will create. The function should return a list containing the same number of elements as the count argument. The value of each element should be a multiple of the starting number.

You may assume that count will always be an integer greater than or equal to 0. The starting number can be any integer. If the count is 0, the function should return an empty list.

##### PEDAC #####

# Define Problem
1. Inputs: two integers: count & starting number
   Outputs: list starting with starting number, containing `count` number of elements

   Explicit rules:
   - First input integer is count. Return list should have number of elements equal 
     to count.
   - Second input integer is starting number. Return list should start with starting number and every integer thereafter is a multiple of starting number
   - Count will always be an integer >= 0
   - Starting number can be any integer
   - If count = 0, return empty list ([])

   Implicit rules:
   - To calculate multiples, multiply starting number by 1, then by 2, then by 3, and so on until the number of elements equal to count is reached.
   - If starting number is positive, all integers will be positive
   - If starting number is negative, all integers will be negative


# Test Cases

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True

# Data Structures
Integers for inputs
Ranges for looping over
List return object

# Algorithm
1. Initialize new list object for return list
2. Multiply starting number by 1 and append to list. Then multiply starting number
by 2 and append to list. Repeat until the list contains number of elements equal
to count. 
3. If count = 0, return []