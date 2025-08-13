'''
Merge Sets
Given two lists, convert them to sets and return a new set which is the union of both sets.


'''

def merge_sets(input_list1, input_list2):
    input_set1 = set(input_list1)
    input_set2 = set(input_list2)

    return input_set1 | input_set2



list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})