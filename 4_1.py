""" Given a directed graph, design an algorithm to find out whether there is a route between two nodes. """

# graph dict from online
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

def find(graph, a, b, path=[]):
    # look at a, if the values of key a include b, return yes
    path = path + [a]
    if a == b:
        return path
    for key, value in graph.items():
        # if key == a and :
        #     return None
    for node in graph[a]:
        if node not in path:
            new_path = find(graph, node, b, path)
            if new_path:
                print(new_path)
                return new_path
    return None
    # for key, value in graph.items():
    #     if key == a:
    #         for i in value:
    #             if i == b:
    #                 print('yes')
    #                 return
    #             else:
    #                 continue # is this right?
    #         for i in value:
    #             for key, value in graph.items():
    #                 if key == i:
    #                     print('yes', key, value)
    #                     for j in value:
    #                         if j == b:
    #                             print('found it!', j)
    #                         else:
    #                             print('not found', j)
    #                     return
    #                 else:
    #                     print('no', key, value)
    #                     # return
    #     else:
    #         print('no node with that name')

print(find(graph, 'A', 'E'))
