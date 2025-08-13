'''
Alphabetical Numbers
Write a function that takes a list of integers between 0 and 19 
and returns a list of those integers sorted based on the English 
word for each number:

zero, one, two, three, four, five, six, seven, eight, nine, ten, 
eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, 
eighteen, nineteen
'''

INTEGERS = range(20)
WORDS = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', \
         'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', \
         'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')

INT_TO_WORDS = dict(zip(INTEGERS, WORDS))
WORDS_TO_INT = dict(zip(WORDS, INTEGERS))

def alphabetic_number_sort(input_numbers):

    convert_to_words = [
        INT_TO_WORDS[num]
        for num
        in input_numbers
    ]

    convert_to_words.sort()

    convert_to_ints = [
        WORDS_TO_INT[word]
        for word
        in convert_to_words

    ]

    return convert_to_ints


input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)