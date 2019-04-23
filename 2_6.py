""" 2.6 Palindrome: Implement a function to check if a linked list is a palindrome. """

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

node1 = Node(1)
node2 = Node(2)
node3 = Node(2)
node4 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4

def palindrome(self):
    curr = self
    list = []
    while curr is not None:
        list.append(curr.value)
        curr = curr.next
    print(list)
    if list[::-1] == list:
        print('Is a palindrome')
    else:
        print('Not a palindrome')
palindrome(node1)
