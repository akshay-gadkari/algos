# Chapter 04 - Problem 08 - First Common Ancestor

# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. 
# Avoid storing additional nodes in a data structure. Assume that this tree is not necessarily a binary search tree.
# Assume that nodes in the tree do not have links to their parents.

# Traverse the tree recursively using a function whose return value indicates the presence of nodes 1 and 2
# in the current node's left or right subtrees. The function also passes a reference to a Null node that is changed
# to the identity of the first common ancestor if such a node exists. At each recursive call, the function returns one of
# the following: "1" if the current node is an ancestor of node1, "2" if the current node is an ancestor of node2, 
# "3" if the current node is an ancestor of both nodes 1 and 2 or "0" in case the current node is an ancestor
# of neither nodes 1 or 2. The function recurses until nodes1 and 2 are found and their presence is "bubbled up"
# the tree in the form of the return values. If case "3" is encountered and the reference is still Null, the reference
# is assigned the current node which by definition is the first common ancestor.
# The terminating condition of the function is finding node1, node2, or Null.


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
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node.newNode(2, left=node3, right=node4)
        
def ancestor(node, n1, n2):
    print('left:',node.left.v)
    print('right:', node.right.v)
    if node.left == n1 and node.right == n2:
        print('yes!')
        return
    else:
        if node.left is not None:
            node = node.left()
            ancestor(node, n1, n2)
        if node.right is not None:
            node = node.right()
            ancestor(node, n1, n2)
    return

ancestor(node, node3, node4)
