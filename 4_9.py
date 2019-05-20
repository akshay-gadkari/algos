# Chapter 04 - Problem 10 - Check Subtree
# Problem Statement:
# T1 and T2 are two very large binary trees, with T1 much bigger than T2.
# Create an algorithm to determine if T2 is a subtree of T1. A tree T2 is a subtree of T1
# if there exists a node n in T1 such that the subtree of n is identical to T2. That is,
# if you cut off the tree at node n, the two trees would be identical.

class node:
    def __init__(self, v, left=None, right=None):
        self.v = v
        self.left = left
        self.right = right

class tree:
    def __init__(self):
        self.root = None
    def insert(self, data, left=None, right=None):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = node(data, left = None, right = None)
            return True

tree = tree()
tree.insert(1, left = 2, right = 3)
# tree.insert(3, left = 5, right = 6)
