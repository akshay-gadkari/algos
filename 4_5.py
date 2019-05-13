# Chapter 04 - Problem 05 - Validate BST
# Problem Statement:
# Implement a function to check if a binary tree is a binary search tree (BST).

class Node:
    def __init__(self, v, left=None, right=None):
        self.left = left
        self.right = right
    def newNode(self, v, left = None, right = None):
        self.v = v
        self.left = left
        self.right = right

node = Node(1)
node2 = Node(2)
node3 = Node(3)
node.newNode(1, left = node2, right = node3)

def checkBST(n):
    print(n.v)

checkBST(node)
