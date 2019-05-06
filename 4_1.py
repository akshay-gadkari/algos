""" Given a directed graph, design an algorithm to find out whether there is a route between two nodes. """

# graph dict from online
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

def find(g, a, b):
    # look at a, if the values of key a include b, return yes
    for key, value in graph.items():
        if key == a:
            for i in value:
                if i == b:
                    print('yes')
                    return
                else:
                    continue # is this right?
            for i in value:
                for key, value in graph.items():
                    if key == i:
                        print('yes', key, value)
                        for i in value:
                            if i == b:
                                print('found it!')
                            else:
                                print('not found')
                        return
                    else:
                        print('no', key, value)
                        # return
        else:
            print('no node with that name')

find(graph, 'A', 'D')
