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

# node5 = Node(5)
node = Node(1)
node4 = Node(4)
node2 = Node(2, left = node4)
node3 = Node(3)
node.newNode(1, left = node2, right = node3)

def check(n, counter = 0):
    try:
        if n.left is not None:
            print(n.v, "left:", n.left.v)
        if n.right is not None:
            print(n.v, "right", n.right.v)
    except AttributeError:
        return
    if not (n.right is not None and n.left is not None):
        # print('this one\'s balanced')
        counter += 1
    # else:
    #     counter += 1
    if counter >= 3:
        print('not balanced')
    else:
        print('balanced')
    check(n.right, counter)
    check(n.left, counter)
check(node)
