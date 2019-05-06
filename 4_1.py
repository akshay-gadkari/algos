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
                    print('true')
                    return
            # if not, search the values of those keys
            
find(graph, 'A', 'B')
