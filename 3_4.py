# Implement a queue using two stacks.

s1 = [1, 2, 3]
s2 = []

def isEmpty(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return True
    else:
        return False

def size(s1, s2):
    size = len(s1) + len(s2)
    return size
print(size(s1, s2))

def enqueue(e):
    s1.append(e)

def dequeue():
    if len(s2) == 0:
        while len(s1 != 0):
            s2.append(s1[0])
            s1.pop(0)
    return s2.pop

# enqueue(4)
print(s1)
