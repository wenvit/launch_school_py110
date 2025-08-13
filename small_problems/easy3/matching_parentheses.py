'''
Matching Parenthesis?
Write a function that takes a string as an argument 
and returns True if all parentheses in the string 
are properly balanced, False otherwise. 
To be properly balanced, parentheses must occur 
in matching '(' and ')' pairs.

'''
def is_balanced(input_string):

    parens = ''

    for char in input_string:
        if char in ['(', ')']:
            parens += char

    count_left_parens = parens.count('(')
    count_right_parens = parens.count(')')

    if parens:
        return count_left_parens == count_right_parens and \
           parens.startswith('(') and parens.endswith(')')
    else:
        return True 

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True


