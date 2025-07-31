
'''
Halvsies Problem Statement

Write a function that takes a list as an argument and returns 
a list that contains two elements, both of which are lists. 
Put the first half of the original list elements in the first 
element of the return value and put the second half in the second 
element. If the original list contains an odd number of elements, 
place the middle element in the first half list
'''
def halvsies(input_list):

    if len(input_list) == 1:
        half1 = input_list
        half2 = []

    elif len(input_list) % 2 == 0:
        idx_divide = len(input_list) // 2
        half1 = input_list[ :idx_divide]
        half2 = input_list[idx_divide: ]
    elif len(input_list) % 2 == 1:
        idx_divide = len(input_list) // 2 + 1
        half1 = input_list[ :idx_divide]
        half2 = input_list[idx_divide: ]
    else:
        half1 = []
        half2 = []
    
    return [half1, half2]


# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])