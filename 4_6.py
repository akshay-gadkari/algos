# Chapter 04 - Problem 06 - Successor
# Problem Statement:
# Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree.
# You may assume that each node has a link to its parent.

class Node:
    def __init__(self, v, left=None, right=None):
        self.left = left
        self.right = right
        self.v = v
    def newNode(self, v, left=None, right=None):
        self.v = v
        self.left = left
        self.right = right

node = Node(1)
node2 = Node(2)
node3 = Node(3)

node.newNode(1, left = node2, right = node3)

def next(n):
    if n.left is not None:
        print(n.left.v)
        return
    if n.right is not None:
        print(n.right)
        return
    else:
        print('no node after this')

next(node)
