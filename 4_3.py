# Chapter 04 - Problem 03 - List of Depths
# Problem Statement:
# Given a binary tree, design an algorithm which creates a linked list
# of all the nodes at each depth (e.g., if you have a tree with
# depth D, you'll have D linked lists).

alist = []
from collections import defaultdict

class Tree:
    def __init__(self):
        self.tree = defaultdict(list)
    def addEdge(self, root, child):
        self.tree[root].append(child)
    def get(self, position):
        return self.tree[position]
    # def getChild(self, position, child):
    #     return self.tree[position].get(child)

tree = Tree()
tree.addEdge(0, 1)
tree.addEdge(1, 2)
tree.addEdge(1, 3)
tree.addEdge(3, 4)
tree.addEdge(2, 5)
tree.addEdge(4, 6)

# depth = 1
def dfs(tree, element, depth):
    visited = []
    a = tree.get(element)
    # depth = 1
    if a is not None and len(a) > 0:
        visited.append(a)
        depth += 1
        print('element', a, 'with a depth of', depth)
        a = a[0]
        dfs(tree, a, depth)
    # print('visited:', visited[0])
dfs(tree, 0, 0)
