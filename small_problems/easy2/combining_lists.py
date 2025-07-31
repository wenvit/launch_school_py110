''''
Combining Lists Problem Statement 
Write a function that takes two lists as arguments and 
returns a set that contains the union of the values from 
the two lists. You may assume that both arguments will 
always be lists.
'''

def union(list1, list2):
    combined_list = list1 + list2
    
    union_of_lists = {
        element
        for element 
        in combined_list
    }

    return union_of_lists


print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
print(union([], ['a', 'b', 'c']))
print(union([], []))