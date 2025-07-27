
Letter Counter (Part 2) Problem Statement
Modify the word_sizes function from the previous exercise to exclude
non-letters when determining word size. For instance, the word 
size of "it's" is 3, not 4.

##### PEDAC #####

# Define problem
1. Input: string of zero or more space-separated words
   Output: dictionary showing number of words of different sizes

2. Explicit rules:
   - Input string can contain zero or more words.
   - Words are separated by spaces.
   - Words consist of any sequence of non-space characters.

3. Implicit rules:
   - Dictionary keys are the word length, and values are the
     number of words of that length.
   - Punctuation and other non-space characters should not be counted 
     when determining word length.
   - Order of the key-value pairs doesn't matter.
   - An empty string should result in an empty dictionary.

# Test cases - provided

All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

# Data structures
 - String inputs
 - Dictionary outputs
 - Use a list for the interim step of splitting the string into
   individual words for looping over.

# Algorithm
1. Initialize empty dictionary for result.
2. "Clean" the string by removing any non-alpha characters that aren't
   spaces.
3. Split input string based on spaces into individual words.
    Put words in list.
4. Loop over list of words. For each word:
    - Count length of word
    - Add key of word length to dictionary if it doesn't already exist
      and set value for that key to 1
      If key of word length is already in dictionary, increment value
      for that key by 1


