'''
Reverse Number
Write a function that takes a positive integer as an argument and returns that 
number with its digits reversed.

'''

def reverse_number(input_num):

    num_string = str(input_num)
    reversed_string = num_string[::-1]

    return int(reversed_string)


print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True