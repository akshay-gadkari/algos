# Chapter 04 - Problem 08 - First Common Ancestor

# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. 
# Avoid storing additional nodes in a data structure. Assume that this tree is not necessarily a binary search tree.
# Assume that nodes in the tree do not have links to their parents.

class Node:
    def __init__(self, v, left=None, right=None):
        self.v = v
        self.left = left
        self.right = right
    def newNode(self, v, left=None, right=None):
        self.v = v
        self.left = left
        self.right = right

node = Node(1)
node3 = Node(3)
node4 = Node(4)

node.newNode(2, left=node3, right=node4)
        
def ancestor(n1, n2):
    
ancestor(node3, node4)
