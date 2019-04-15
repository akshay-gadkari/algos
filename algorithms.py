# def sum1(n):
#     final_sum = 0
#     for x in range(n+1):
#         final_sum += x
#     return final_sum
# #print(sum1(5))

# def sum2(n):
#     #take an input of n and return the sum of the numbers from 0 to n
#     return int(round(n*(n+1))/2)
# #print(sum2(5))

# ch 1 problem 1

# word = 'abc'
# def repeats(word):
#     alist = list(word)
#     blist = sorted(alist)
#     if len(alist) == 1:
#         return None
#     for i in range(len(alist)-1):
#         if blist[i] == blist[i+1]:
#             return blist[i]
#     return None
# print(repeats(word))


#ch 1 problem 2

# str1 = 'alex'
# str2 = 'lexa'
# def is_permutation(str1, str2):
#     if len(str1) != len(str2):
#         return False
#     else:
#         concat1 = ''.join(sorted(str1))
#         concat2 = ''.join(sorted(str2))
#         if concat1 == concat2:
#             return True
#         else:
#             return False
# print(is_permutation(str1, str2))


#ch 1 problem 3


# str1 = 'the quick brown fox jumps over the lazy sheep dog'
# def replace_spaces(str1):
#     newstr = str1.replace(' ', '%20') + '%20'
#     return newstr
# print(replace_spaces(str1))


#ch 1 problem 4

# str1 = 'racecar'
# def is_palindrome_permutation(str1):
#     if len(str1) == 1:
#         return True
#     mylist = sorted(list(str1))
#     for i in mylist:
#         if mylist[i] == mylist[i+1]:
#             count = 1
#             count = count + 1
#             # count the number of each letter
#             # if all but one is even, it's a palindrome




#ch1 problem 5
# Problem Statement:
# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.

# str1 = 'abcc'
# str2 = 'abzcc'

# def n_edits_away(a, b):
#     count = 0
#     position = 0
#     if str1 == str2:
#         return count
#     if len(str1) == len(str2):
#         for i in range(len(str1)):
#             if str1[i] != str2[i]:
#                 count += 1
#         return count + 'edit(s) away'
#     if (len(str1) == len(str2) + 1):
#         for i in range(len(str2)):
#             if str2[i] != str1[i]:
#                 count += 1
#         if count == 1:
#             if len(str2[i-1:]) == len(str1[i:]):
#                 return '1 edit away'
#         return 'over 1 edit away'
#     if (len(str2) == len(str1) + 1):
#         for i in range(len(str1)):
#             if str1[i] != str2[i]:
#                 count += 1
#         if count == 1:
#             if len(str1[i-1:]) == len(str2[i:]):
#                 return '1 edit away'
#         return 'over 1 edit away'
#     else:
#         return '1 or more edits away'
# print(n_edits_away(str1, str1))




# ch1 problem 6
# Implement a method to perform basic string compression using the counts of repeated characters. For example,
# the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the
# original string, your method should return the original string. You can assume the string has only uppercase
# and lowercase letters (a - z).

# s1 = 'aabcccccaaa'

# def compress(a):
#     b = []
#     count = 0
#     for i in range(len(a)):
#         try:
#             if a[i] == a[i+1]:
#                 count += 1
#             else:
#                 b.append(a[i])
#                 b.append(count + 1)
#                 count = 0
#         except IndexError:
#             b.append(a[i])
#             b.append(count + 1)
#     b = ''.join(map(str, b))
#     return b
# print(compress(s1))



# ch 1 problem 6
# Problem Statement:
# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees. Can you do this in place?

# Example:
# [1,2,3,       [7,4,1,
#  4,5,6,   ->   8,5,2,
#  7,8,9]        9,6,3]
import math
import numpy

a = [1,2,3,
     4,5,6,
     7,8,9]

def rotate(square):
    reversed_list = []
    if len(square) % math.sqrt(len(square)) != 0:
        return 'not a square'
    split = list(reversed(square))
    split = numpy.array_split(split,math.sqrt(len(split)))

    zipped = list(zip(*split))
    zipped = list(reversed(zipped))
    return zipped
print(rotate(a))
