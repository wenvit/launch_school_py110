
Letter Swap Problem Statement
Given a string of words separated by spaces, write a 
function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, 
and that the string will always contain at least one word. 
You may also assume that each string contains nothing but 
words and spaces, and that there are no leading, trailing, 
or repeated spaces.

##### PEDAC #####

# Define problem
1. Input: string of words separated by spaces
   Output: new string of words with first & last letters 
           of every word swapped

2. Explicit rules:
 - Every word contains at least one letter.
 - String always contains at least one word.
 - Each string contains nothing but words and spaces
 - No leading, trailing, or repeated spaces

3. Implicit rules:
 - Smallest word is one letter
 - String will not contain digits, punctuation or other
   non-alpha characters or spaces

# Test cases - provided

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

# Data structures
 - String inputs
 - String output
 - A list as interim structure for string manipulation

# Algorithm
1. Initialize an empty list for storing the swapped letter words.
2. Split string into words by the spaces. Put into another list.
3. Loop over each word in the list. If length of word > 1, wwap the 
   first & last letters of word and append into the list for 
   the swapped letter words. If length of word = 1, append the word
   into the list as is.
3. Join the swapped-letter words separated by spaces into a new string.
