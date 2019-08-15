n = 10
def fibonacci(n):
    if n == 1:
        print([0])
        return [0]
    if n == 2:
        print([0, 1])
        return [0, 1]
    sequence = [0, 1]
    
    for i in range(n):
        sum = sequence[-2] + sequence[-1]
        print(i+1, 'sum', sum)
        sequence.append(sum)
    print(sequence)
fibonacci(n)
