""" 3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty. """

s1 = [4, 2, 1, 3]
tempstack = []

def isEmpty(s1):
    if len(s1) == 0:
        return True
    return False

def push(s1, e):
    s1.append(e)

def pop(s1):
    s1.pop()

def sortstack(s1):
    while len(s1) > 0:
        tempstack.append(min(s1))
        s1.remove(min(s1))
    return tempstack

print(sortstack(s1))
