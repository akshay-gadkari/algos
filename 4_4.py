# Chapter 04 - Problem 04 - Check Balanced
# Problem Statement:
# Implement a function to check if a binary tree is balanced.
# For the purposes of this question, a balanced tree is defined to be a tree
# such that the heights of the two subtrees of any node never differ by more than one.

class Node:
    def __init__(self, v, left = None, right = None):
        self.v = v
        self.left = left
        self.right = right
    def get(self):
        return self.v
    def newNode(self, v, left = None, right = None):
        self.v = v
        self.left = left
        self.right = right
    def getChildren(self):
        if self.right is not None:
            right = self.right
        if self.left is not None:
            left = self.left
        children = left + right
        return children

node = Node(1)
node4 = Node(4)
node2 = Node(2, left = node4)
node3 = Node(3)
# node2.newNode(6)
node.newNode(1, left = node2, right = node3)

def check(n):
    try:
        if n.left is not None:
            print(n.left.v)
        if n.right is not None:
            print(n.right.v)
    except AttributeError:
        return
    check(n.right)
    check(n.left)
check(node)
