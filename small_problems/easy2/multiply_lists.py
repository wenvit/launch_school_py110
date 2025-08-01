'''
Multiply Lists Problem Statement

Write a function that takes two list arguments, each containing 
a list of numbers, and returns a new list that contains the 
product of each pair of numbers from the arguments that have 
the same index. You may assume that the arguments contain 
the same number of elements.

'''

def multiply_list(input_list1, input_list2):

    product_list = []

    for idx in range(len(input_list1)):
        product = input_list1[idx] * input_list2[idx]
        product_list.append(product)

    return product_list


# Launch School Solution

# def multiply_list(numbers1, numbers2):
#     return [a * b for a, b in zip(numbers1, numbers2)]


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True