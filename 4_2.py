# minimal height BST
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def get(self):
        self.value = value
    def getchildren(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        else:
            print('None')
            return
        return children
# sorted array



arr = [1, 7, 4, 9, 8, 2]
sorted_arr = sorted(arr)
#print(sorted_arr)
