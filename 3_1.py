""" 3.1 Three in One: Describe how you could use a single array to implement three stacks. """

array = [1, 2, 3, 4, 5, 6, 7]
# array.append(6)
# array.append(7)
#stack.pop()

if len(array) >= 3:
    stacklen = int(len(array) / 3)

stack1 = array[0:stacklen]
print(stack1)

stack2 = array[stacklen:stacklen*2]
print(stack2)

stack3 = array[stacklen*2:len(array)]
print(stack3)

def inputstack1(insert):
    array.insert(stacklen, insert)
inputstack1('hi')
print(array)

def popstack1():
    del array[stacklen]
popstack1()
print(array)

def inputstack2(insert):
    array.insert(stacklen*2, insert)
inputstack2('hi')

def popstack2():
    del array[stacklen*2]
#popstack2()

def inputstack3(insert):
    array.insert(len(array), insert)
#inputstack3('hi')

def popstack3():
    array.pop()
#popstack3()
