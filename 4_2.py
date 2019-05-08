# minimal height BST
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
# sorted array
arr = [1, 2, 3, 4, 5, 6, 7, 8]
sorted_arr = sorted(arr)

# bst
def bst(a):
    if not a or len(a) == 0:
        return None
    middle = int(len(a) // 2)
    root = Node(a[middle])
    # print(root.value)
    root.left = bst(a[:middle])
    root.right = bst(a[middle+1:])
    if root.left != None and root.right != None:
        print('value', root.value, 'left', root.left.value, 'right', root.right.value)
    elif root.left is not None and root.right is None:
        print('value', root.value, 'left', root.left.value)
    elif root.right is not None and root.left is None:
        print('value', root.value, 'right', root.right.value)
    return root
bst(sorted_arr)
