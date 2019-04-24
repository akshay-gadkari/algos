""" 2.8 Loop detection: Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.

DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C -> D -> E -> C (the same C as before)
Output: C """

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
node3.next = node4
node4.next = node5
node5.next = node1

def loop(self):
    curr = self
    first = True
    if first is True:
        first_node = curr
        first = False
    while curr is not None:
        if curr.next is first_node:
            print(first_node.value, 'is the first node') # if the next node is the 1st node stop and print it
            return f'{first_node.value}'
        print(curr.value)
        curr = curr.next
    print('done without loop')
        
loop(node1)
