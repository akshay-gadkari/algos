# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.

# Note that an empty string is also considered valid.

# Example 1:
# Input: "()"
# Output: true

# Example 2:
# Input: "()[]{}"
# Output: true

# Example 3:
# Input: "(]"
# Output: false

open_list = ["[","{","("] 
close_list = ["]","}",")"] 

def valid_parentheses(s):
    left = 0
    right = 0
    for i in s:
        if i in lset:
            left += 1
        if i in rset:
            right += 1
        if left == 0 and i in rset:
            print('invalid parentheses')
            return
    print('left:', left)
    print('right:', right)
    if left != right:
        print('invalid parentheses')
        return
valid_parentheses(s)

