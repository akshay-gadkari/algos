""" 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other. """

str1="ab1"
str2="aaa"

def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    s1 = ''.join(sorted(str1))
    s2 = ''.join(sorted(str2))
    if str1 == str2:
        return True
    return False
