""" 2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting. """

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3

node4.next = node2
node2.next = node5

def intersect(self):
    curr = self
    while curr is not None:
        print(curr.value)
        curr = curr.next

intersect(node1)
