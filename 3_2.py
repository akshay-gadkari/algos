""" 3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in O(1) time. """

# You would want to implement your Stack from a custom LinkedList class where each Node has a next_min property and the LinkedList has a min property so that, when a node that is the minimum is pushed from the stack, it would update the stack min. Take into account how you deal with doubles.

array = [1, 2, 3, 4, 5, 6, 7]

if len(array) >= 3:
    stacklen = int(len(array) / 3)

def pushsstack1(insert):
    array.insert(stacklen, insert)
    stacklen += stacklen
pushsstack1('hi')
print(array)

def popstack1():
    del array[stacklen]
popstack1()
print(array)

def minstack1():
    return min(array[0:stacklen])
print(minstack1)

def pushsstack2(insert):
    stacklen2 = stacklen*2
    array.insert(stacklen2, insert)
    stacklen2 += 1

pushsstack2('hi')

def popstack2():
    del array[stacklen2]
#popstack2()

def minstack2():
    return min(array[stacklen:stacklen2])
print(minstack2)

def pushsstack3(insert):
    array.insert(len(array), insert)
#pushsstack3('hi')

def popstack3():
    array.pop()
#popstack3()

def minstack3():
    return min(array[stacklen2:])
print(minstack3)
