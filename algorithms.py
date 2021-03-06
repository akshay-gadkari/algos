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

# import math
# import numpy

# a = [1,2,3,
#      4,5,6,
#      7,8,9]

# def rotate(square):
#     reversed_list = []
#     if len(square) % math.sqrt(len(square)) != 0:
#         return 'not a square'
#     split = list(reversed(square))
#     split = numpy.array_split(split,math.sqrt(len(split)))

#     zipped = list(zip(*split))
#     zipped = list(reversed(zipped))
#     return zipped
# print(rotate(a))




# Chapter 01 - Problem 08 - Set Zero - CTCI 6th Edition page 91

# Problem Statement:
# Write an algorithm such that if an element in an MxN matrix is 0, its entire
# row and column are set to 0.

# Example:
# [1, 2, 0, 4,      [0, 0, 0, 0,
#  1, 2, 3, 4,  ->   0, 2, 0, 4,
#  0, 2, 3, 4]       0, 0, 0, 0]

# import numpy
# import math
# rectangle = numpy.matrix('1 2 0 4; 1 2 3 4; 0 2 3 4')
# def set_zero(matrix):
#     # which rows and columns to change to zeroes
#     rows = []
#     columns = []
#     # add which rows have zeroes to the rows list2
#     for i in range(len(rectangle)):
#         if 0 in rectangle[i]:
#             rows.append(i)
#     # add which columns have zeroes to the columns list
#     rectangle2 = rectangle.transpose(1,0)
#     for i in range(len(rectangle2)):
#         if 0 in rectangle2[i]:
#             columns.append(i)
#     for r in rows:
#         rectangle[r] = 0
#     for s in columns:
#         rectangle[:,s] = 0
#     print('')
#     # print('rows', rows)
#     # print('columns', columns)
#     return rectangle
# print(set_zero(rectangle))


# Chapter 01 - Problem 09 - String Rotation - CTCI 6th Edition page 91

# Problem Statement:
# Assume you have a method isSubstring() which checks if one word is a substring of
# another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
# only one call to isSubstring().
# Example:
# stringRotation("waterbottle", "erbottlewat")

# def isSubstring(s1, s2):
#     if s2 in s1:
#         return True
#     return False

# def stringRotation(string, rotated):
#     string = 2*string
#     if len(string) == len(rotated)*2:
#         return isSubstring(string, rotated)
#     else: False

# print(stringRotation("waterbottle", "erbottlewat"))


""" 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed? """

# class llNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

# #from online
# def deleteDups(self, head):
#     if head is None:
#         return 'None'
#     curr = head
#     while curr is not None:
#         inner = curr
#         while inner.next is not None:
#             if inner.next.val == curr.val:
#                 inner.next = inner.next.next
#             else:
#                 inner = inner.next
#         curr = curr.next
#     return head

# 1 = llNode("3")
# 2 = llNode("7")
# 3 = llNode("10")
# 4 = llNode("7")
# print(1.nextNode)

""" 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list. """
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# node1 = Node(12)
# node2 = Node(99)
# node3 = Node(37)

# node1.next = node2
# node2.next = node3

# def kth_element(self, k):
#     curr = self
#     position = 0
#     matrix = []
#     while curr is not None:
#         position += 1
#         appended = [curr.value, position]
#         matrix.append(appended)
#         curr.position = position
#         curr = curr.next
#     if curr is None:
#         matrix = matrix[::-1]
#         print(matrix[k-1][0])

# kth_element(node1, 2)


# """ 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node. 

# EXAMPLE
# Input: the node c from the linked list a -> b -> c -> d -> e -> f
# Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f"""

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# node1 = Node(12)
# node2 = Node(99)
# node3 = Node(37)
# node4 = Node(22)

# node1.next = node2
# node2.next = node3
# node3.next = node4

# def delete_middle_node(self, node):
#     curr = self
#     while curr is not None:
#         if curr.next == node:
#             curr.next = curr.next.next
#         print(curr.value)
#         curr = curr.next

# delete_middle_node(node1, node2)



""" 2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x. The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions. 
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 with partition x=5
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""

# class Node:
#     def __init__(self, value, next=None, prev=None):
#         self.value = value
#         self.next = next
#         self.prev = prev

# node1 = Node(12)
# node2 = Node(99)
# node3 = Node(37)
# node4 = Node(22)
# node5 = Node(50)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# node2.prev = node1
# node3.prev = node2
# node4.prev = node3
# node5.prev = node4

# def partition(self, num):
#     curr = self
#     passed_num = False
#     matrix = []
#     counter = 0
#     while curr is not None:
#         matrix.append(curr.value)
#         if curr.value == num:
#             passed_num = num
#         if passed_num == num and curr.value < passed_num:
#             # move current node to before node 37
#             print('prev is', curr.prev.value, 'and curr is', curr.value, 'next is', curr.next.value)
#             curr.prev.next = curr.next # skips the current value
#             curr.next = curr.prev
#         print(curr.value)
#         curr = curr.next
#     # while curr is not None:
#     #     if curr.value == num and counter == 0:
#     #         curr.prev.next = curr.next
#     #         counter += 1
#     print(matrix)

# partition(node1, 37)



'''2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list. 
EXAMPLE
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Ll:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

first = Ll()
second = Ll()

first.push(7)
first.push(1)
first.push(6)

second.push(5)
second.push(9)
second.push(2)

combined = []

def first_list(self):
    curr = self
    list1 = []
    while curr is not None:
        list1.append(curr.data)
        curr = curr.next
    map(str, list1)
    list1 = map(str, list1)
    list1 = ''.join(list1)
    print(list1)
    combined.append(list1)
first_list(first.head)

def second_list(self):
    curr = self
    list2 = []
    while curr is not None:
        list2.append(curr.data)
        curr = curr.next
    map(str, list2)
    list2 = map(str, list2)
    list2 = ''.join(list2)
    print(list2)
    combined.append(list2)
second_list(second.head)

def add():
    results = list(map(int, combined))
    result = results[0] + results[1]
    print(result)
add()
