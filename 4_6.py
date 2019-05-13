# Chapter 04 - Problem 06 - Successor
# Problem Statement:
# Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree.
# You may assume that each node has a link to its parent.

class Node:
    def __init__(self, v, left=None, right=None):
        self.left = left
        self.right = right
    def newNode(self, v, left=None, right=None):
        self.v = v
        self.left = left
        self.right = right

node = Node(1)
node2 = Node(2)

