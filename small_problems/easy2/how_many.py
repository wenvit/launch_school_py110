'''
How Many? Problem Statement

Write a function that counts the number of occurrences 
of each element in a given list. Once counted, print each 
element alongside the number of occurrences. Consider the 
words case sensitive e.g. ("suv" != "SUV").

'''

def count_occurrences(input_list):

    element_counts = {}

    for element in input_list:
        element_counts[element] = element_counts.get(element, 0) + 1
    
    return element_counts




vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

vehicle_counts = count_occurrences(vehicles)

for vehicle, count in vehicle_counts.items():
    print(f'{vehicle} ==> {count}')