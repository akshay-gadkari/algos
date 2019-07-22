""" 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures? """

string = "abc"
def is_unique(string):
    count = []
    for i in string:
        if i not in count:
            count.append(i)
    if len(count) < len(string):
        return False
    return True
