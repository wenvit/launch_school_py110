Matching Parenthesis?
Write a function that takes a string as an argument and returns True if all parentheses in the string are properly balanced, False otherwise. To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

##### PEDAC #####

# Define Problem
1. Input: string
   Output: boolean True or False
2. Explicit rules
   - Return True if all parentheses are properly balanced, false otherwise
   - Properly balanced means matching pairs --> '(' and ')'
3. Implicit rules
   - Order matters, pairs must start with '(' and end with ')'
   - If there are no parentheses, return True

# Test Cases

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

# Data Structures
Strings

# Algorithm
1. Strip out occurrences of '(' and ')' and create new string or list
2. Count occurrences of '(' and ')'
3. If counts are equal and the sequence begins with a '(' and ends with ')'
   return True, otherwise False

