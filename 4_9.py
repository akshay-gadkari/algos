# Chapter 04 - Problem 10 - Check Subtree
# Problem Statement:
# T1 and T2 are two very large binary trees, with T1 much bigger than T2.
# Create an algorithm to determine if T2 is a subtree of T1. A tree T2 is a subtree of T1
# if there exists a node n in T1 such that the subtree of n is identical to T2. That is,
# if you cut off the tree at node n, the two trees would be identical.

# class node:
#     def __init__(self, v, left=None, right=None):
#         self.v = v
#         self.left = left
#         self.right = right

# class tree:
#     def __init__(self, v):
#         self.root = node(v)
#     def insertleft(self, v, data, left=None, right=None):
#         self.left = node(data)
#         return True
#     def insertright(self, v, data, left=None, right=None):
#         self.right = node(data)
#         return True



# tree = tree(0)
# tree.insertleft(0, 1)
# tree.insertleft(1, 3)
# tree.insertright(0, 2)

# allnodes = []
# def parse(tree, allnodes):
#     try:
#         if tree.root:
#             allnodes.append(tree.root.v)
#             print(allnodes)
#     except AttributeError:
#         print('')
#     if tree.left:
#         allnodes.append(tree.left.v)
#         parse(tree.left, allnodes)
#         print(allnodes)
#     if tree.right:
#         allnodes.append(tree.right.v)
#         parse(tree.right, allnodes)
#         print(allnodes)
#     print(allnodes)

# parse(tree, allnodes)


class node:
    def __init__(self, v, left=None, right=None):
        self.v = v
        self.left = left
        self.right = right

node1 = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)
node5 = node(5)
# node6 = node(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
# node3.left = node6

nodes = []
def parse(node):
    nodes.append(node.v)
    if node.left is not None and node.right is None:
        node = node.left
        nodes.append(node.v)
        parse(node)
    if node.right is not None and node.left is None:
        node = node.right
        nodes.append(node.v)
        parse(node)
    if node.left is None and node.right is None:
        print(nodes)
    if node.left is not None and node.right is not None:
        parse(node.left)
        parse(node.right)
        
parse(node1)
