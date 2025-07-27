'''
Running Totals Problem Statement
Write a function that takes a list of numbers and returns a list
with the same number of elements, but with each element's value
being the running total from the original list.

'''

# Code implementation

# def running_total(input_list):

#     cum_total_list = []
#     cum_total = 0

#     for num in input_list:
#         cum_total += num
#         cum_total_list.append(cum_total)

#     return cum_total_list


# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True