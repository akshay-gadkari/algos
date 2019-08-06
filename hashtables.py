# hash(k, m) - m is size of hash table
# add(key, value) - if key already exists, update value
# exists(key)
# get(key)
# remove(key)

table = {'person': 'B', 'car': 'tesla'}

# def add(table, k, v):
#     print(table)
#     table[k] = v
#     print(table)
# add('ADD', table, 'person', 'A')

# def exists(table, k):
#     if k in table:
#         print('EXISTS', True)
#     else:
#         print('EXISTS', False)
# exists(table, 'person')

# def get(table, k):
#     if k in table:
#         print('GET', k)
#     else:
#         print('GET', 'key not found')
# get(table, 'person')

def remove(table, k):
    if k in table:
        del table[k]
    else:
        print('key not found')
    print(table)
    
remove(table, 'car')
