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
    def __init__(self, v):
        self.root = node(v)
    def insertleft(self, v, data, left=None, right=None):
        self.left = node(data)
        return True
    def insertright(self, v, data, left=None, right=None):
        self.right = node(data)
        return True
        
tree = tree(0)
tree.insertleft(0, 1)
tree.insertright(0, 2)

allnodes = []
def parse(tree, allnodes):
    if tree.root:
        allnodes.append(tree.root.v)
    if tree.left.v:
        allnodes.append(tree.left.v)
    if tree.right.v:
        allnodes.append(tree.right.v)
    print(allnodes)

parse(tree, allnodes)
