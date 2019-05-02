""" 3.6 Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly 'first in, first out' basis. People must adopt either the 'oldest' (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in LinkedList data structure. """

queue = {'dog': 'fido', 'cat': 'e'}
# queue = {}
klist = ['dog', 'cat']
vlist = ['fido', 'catval']
def enqueue():
    key = input('dog or cat? ')
    if key is not None:
        if key != 'dog':
            if key != 'cat':
                print('must enter either dog or cat')
                return
    value = input('enter it\'s name: ')
    if value is None:
        print('must enter name')
    queue[key] = value
    klist.append(key)
    vlist.append(value)
    # print(queue)
    print(vlist)
    print(klist)
#enqueue()

def dequeueAny():
    # a = next(iter(queue.values()))
    print('adopting', klist[0], ':', vlist[0])
    klist.pop(0)
    vlist.pop(0)
    print(klist, vlist)
# dequeueAny()

def dequeueDog():
    for i in range(len(klist)):
        if klist[i] == 'dog':
            print('adopting', klist[i], ':', vlist[i])
            klist.pop(i)
            vlist.pop(i)
            return
        else:
            i += 1
dequeueDog()

def dequeueCat():
    for i in range(len(klist)):
        if klist[i] == 'cat':
            print('adopting', klist[i], ':', vlist[i])
            klist.pop(i)
            vlist.pop(i)
            return
        else:
            i += 1
dequeueCat()
